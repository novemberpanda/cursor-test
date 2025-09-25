/* eslint-disable no-console */
const $ = (sel) => document.querySelector(sel);
const $$ = (sel) => Array.from(document.querySelectorAll(sel));

const audio = $('#audio');
const playPauseBtn = $('#playPauseBtn');
const prevBtn = $('#prevBtn');
const nextBtn = $('#nextBtn');
const seek = $('#seek');
const timeEl = $('#time');
const volume = $('#volume');
const muteBtn = $('#muteBtn');
const loopBtn = $('#loopBtn');
const shuffleBtn = $('#shuffleBtn');
const fileInput = $('#fileInput');
const folderBtn = $('#folderBtn');
const urlInput = $('#urlInput');
const addUrlBtn = $('#addUrlBtn');
const playlistEl = $('#playlist');
const lyricsEl = $('#lyrics');
const lrcInput = $('#lrcInput');
const clearLyricsBtn = $('#clearLyricsBtn');
const trackTitle = $('#trackTitle');
const trackMeta = $('#trackMeta');
const installBtn = $('#installBtn');
const themeToggle = $('#themeToggle');
const searchInput = $('#searchInput');
const sortSelect = $('#sortSelect');
const miniPrev = $('#miniPrev');
const miniPlay = $('#miniPlay');
const miniNext = $('#miniNext');
const miniSeek = $('#miniSeek');
const miniTime = $('#miniTime');
const miniTitle = $('#miniTitle');
const miniViz = document.getElementById('miniViz');
const vizCanvas = document.getElementById('vizCanvas');
const eqResetBtn = document.getElementById('eqResetBtn');
const clearHistoryBtn = document.getElementById('clearHistoryBtn');
const recentList = document.getElementById('recentList');
const openHistoryBtn = document.getElementById('openHistoryBtn');
const closeHistoryBtn = document.getElementById('closeHistoryBtn');
const recentDrawer = document.getElementById('recentDrawer');

let deferredPrompt = null;
window.addEventListener('beforeinstallprompt', (e) => {
  e.preventDefault();
  deferredPrompt = e;
  installBtn.hidden = false;
});
installBtn?.addEventListener('click', async () => {
  if (!deferredPrompt) return;
  deferredPrompt.prompt();
  await deferredPrompt.userChoice;
  installBtn.hidden = true;
  deferredPrompt = null;
});

// Theme toggle
const THEME_KEY = 'music-theme';
function applyTheme(theme) {
  document.documentElement.dataset.theme = theme;
  localStorage.setItem(THEME_KEY, theme);
}
applyTheme(localStorage.getItem(THEME_KEY) || 'dark');
themeToggle?.addEventListener('click', () => {
  const current = document.documentElement.dataset.theme || 'dark';
  applyTheme(current === 'dark' ? 'light' : 'dark');
});

const state = {
  playlist: [],
  currentIndex: -1,
  isShuffle: false,
  isLoop: false,
  lyrics: [],
  filterText: '',
  sortBy: 'added-asc',
  history: [],
};

// History persistence
const HISTORY_KEY = 'music-history-v1';
function loadHistory() {
  try { state.history = JSON.parse(localStorage.getItem(HISTORY_KEY) || '[]') || []; } catch { state.history = []; }
}
function saveHistory() { localStorage.setItem(HISTORY_KEY, JSON.stringify(state.history.slice(0, 50))); }
function pushHistory(track) {
  if (!track) return;
  // de-dupe by title+url
  state.history = state.history.filter((h) => h.url !== track.url);
  state.history.unshift({ title: track.title, url: track.url, t: Date.now() });
  state.history = state.history.slice(0, 50);
  saveHistory();
  renderHistory();
}
function renderHistory() {
  if (!recentList) return;
  recentList.innerHTML = '';
  for (const item of state.history) {
    const li = document.createElement('li');
    const title = document.createElement('div');
    title.className = 'title';
    title.textContent = item.title;
    const playBtn = document.createElement('button');
    playBtn.textContent = '播放';
    playBtn.addEventListener('click', () => {
      const idx = state.playlist.findIndex((p) => p.url === item.url);
      if (idx >= 0) playIndex(idx);
      else {
        state.playlist.unshift({ id: crypto.randomUUID(), title: item.title, url: item.url, type: 'url' });
        state.currentIndex = 0;
        renderPlaylist();
        playIndex(0);
      }
    });
    li.appendChild(title);
    li.appendChild(playBtn);
    recentList.appendChild(li);
  }
}

function formatTime(sec) {
  if (!isFinite(sec)) return '00:00';
  const m = Math.floor(sec / 60);
  const s = Math.floor(sec % 60);
  return `${String(m).padStart(2, '0')}:${String(s).padStart(2, '0')}`;
}

function updateTimeUI() {
  const cur = audio.currentTime || 0;
  const dur = audio.duration || 0;
  timeEl.textContent = `${formatTime(cur)} / ${formatTime(dur)}`;
  seek.max = dur || 0;
  if (!seek.dragging) seek.value = String(cur);
  miniTime.textContent = `${formatTime(cur)} / ${formatTime(dur)}`;
  miniSeek.max = dur || 0;
  if (!miniSeek.dragging) miniSeek.value = String(cur);
  syncLyrics(cur);
}

function getSortedFilteredIndices() {
  const indices = state.playlist.map((_, i) => i);
  const text = state.filterText.trim().toLowerCase();
  const filtered = text ? indices.filter((i) => (state.playlist[i].title || '').toLowerCase().includes(text)) : indices;
  const sort = state.sortBy;
  const arr = [...filtered];
  arr.sort((a, b) => {
    if (sort === 'added-desc') return b - a;
    if (sort === 'title-asc') return (state.playlist[a].title || '').localeCompare(state.playlist[b].title || '');
    if (sort === 'title-desc') return (state.playlist[b].title || '').localeCompare(state.playlist[a].title || '');
    return a - b; // added-asc
  });
  return arr;
}

function renderPlaylist() {
  playlistEl.innerHTML = '';
  const indices = getSortedFilteredIndices();
  const isDefaultOrder = state.filterText.trim() === '' && state.sortBy === 'added-asc';
  indices.forEach((realIdx, viewIdx) => {
    const t = state.playlist[realIdx];
    const li = document.createElement('li');
    li.className = realIdx === state.currentIndex ? 'active' : '';
    li.draggable = isDefaultOrder;
    li.dataset.index = String(realIdx);
    const title = document.createElement('div');
    title.className = 'title';
    title.textContent = t.title;
    title.title = t.title;
    const playBtn = document.createElement('button');
    playBtn.textContent = realIdx === state.currentIndex && !audio.paused ? '暂停' : '播放';
    playBtn.addEventListener('click', () => {
      if (realIdx === state.currentIndex) {
        togglePlay();
      } else {
        playIndex(realIdx);
      }
    });
    const removeBtn = document.createElement('button');
    removeBtn.textContent = '删除';
    removeBtn.addEventListener('click', () => {
      removeIndex(realIdx);
    });
    li.appendChild(title);
    li.appendChild(playBtn);
    li.appendChild(removeBtn);
    li.addEventListener('dblclick', () => playIndex(realIdx));
    // drag events
    if (isDefaultOrder) {
      li.addEventListener('dragstart', (e) => { e.dataTransfer.setData('text/plain', String(realIdx)); li.classList.add('dragging'); });
      li.addEventListener('dragend', () => li.classList.remove('dragging'));
      li.addEventListener('dragover', (e) => { e.preventDefault(); li.classList.add('dragover'); });
      li.addEventListener('dragleave', () => li.classList.remove('dragover'));
      li.addEventListener('drop', (e) => {
        e.preventDefault();
        li.classList.remove('dragover');
        const from = Number(e.dataTransfer.getData('text/plain'));
        const to = Number(li.dataset.index);
        if (!Number.isFinite(from) || !Number.isFinite(to) || from === to) return;
        const [moved] = state.playlist.splice(from, 1);
        state.playlist.splice(to, 0, moved);
        if (state.currentIndex === from) state.currentIndex = to;
        else if (from < state.currentIndex && to >= state.currentIndex) state.currentIndex -= 1;
        else if (from > state.currentIndex && to <= state.currentIndex) state.currentIndex += 1;
        renderPlaylist();
      });
    }
    playlistEl.appendChild(li);
  });
}

function setNowPlaying(metaTitle, metaSub) {
  trackTitle.textContent = metaTitle || '未选择歌曲';
  trackMeta.textContent = metaSub || '';
}

function updateMediaSession(track) {
  if (!('mediaSession' in navigator)) return;
  try {
    navigator.mediaSession.metadata = new MediaMetadata({
      title: track?.title || '音乐',
      artist: '',
      album: '',
      artwork: [
        { src: './icons/icon-192.png', sizes: '192x192', type: 'image/png' },
        { src: './icons/icon-512.png', sizes: '512x512', type: 'image/png' },
      ],
    });
    navigator.mediaSession.setActionHandler('play', () => play());
    navigator.mediaSession.setActionHandler('pause', () => pause());
    navigator.mediaSession.setActionHandler('previoustrack', () => prev());
    navigator.mediaSession.setActionHandler('nexttrack', () => next());
    navigator.mediaSession.setActionHandler('seekto', (e) => {
      if (typeof e.seekTime === 'number') {
        audio.currentTime = e.seekTime;
      }
    });
  } catch (err) {}
}

function parseLRC(lrcText) {
  const lines = lrcText.split(/\r?\n/).filter(Boolean);
  const out = [];
  const timeTag = /\[(\d{1,2}):(\d{1,2})(?:\.(\d{1,3}))?\]/g;
  for (const line of lines) {
    let match;
    const text = line.replace(timeTag, '').trim();
    while ((match = timeTag.exec(line))) {
      const m = parseInt(match[1], 10) || 0;
      const s = parseInt(match[2], 10) || 0;
      const ms = parseInt((match[3] || '0').padEnd(3, '0'), 10) || 0;
      const timeSec = m * 60 + s + ms / 1000;
      out.push({ timeSec, text });
    }
  }
  out.sort((a, b) => a.timeSec - b.timeSec);
  return out;
}

function renderLyrics() {
  lyricsEl.innerHTML = '';
  state.lyrics.forEach((l, i) => {
    const div = document.createElement('div');
    div.className = 'lyrics-line';
    div.dataset.idx = String(i);
    const ts = document.createElement('span');
    ts.className = 'timestamp';
    ts.textContent = formatTime(l.timeSec);
    const text = document.createElement('span');
    text.textContent = l.text || '\u00A0';
    div.appendChild(ts);
    div.appendChild(text);
    lyricsEl.appendChild(div);
  });
}

function syncLyrics(cur) {
  if (!state.lyrics.length) return;
  let idx = state.lyrics.findIndex((l, i) => {
    const next = state.lyrics[i + 1];
    return cur >= l.timeSec && (!next || cur < next.timeSec);
  });
  if (idx < 0) idx = state.lyrics.length - 1;
  $$('.lyrics-line').forEach((el) => el.classList.remove('active'));
  const active = $(`.lyrics-line[data-idx="${idx}"]`);
  if (active) {
    active.classList.add('active');
    active.scrollIntoView({ behavior: 'smooth', block: 'center' });
  }
}

function addToPlaylist(items) {
  for (const t of items) {
    state.playlist.push({
      id: crypto.randomUUID(),
      title: t.title,
      url: t.url,
      type: t.type,
      file: t.file,
      size: t.size,
    });
  }
  renderPlaylist();
}

async function handleFiles(fileList) {
  const items = [];
  for (const file of fileList) {
    if (!file.type.startsWith('audio') && !/\.(mp3|flac|wav|ogg)$/i.test(file.name)) continue;
    const url = URL.createObjectURL(file);
    items.push({ title: file.name, url, type: 'file', file, size: file.size });
  }
  addToPlaylist(items);
  if (state.currentIndex === -1 && state.playlist.length) playIndex(0);
}

async function handleDirectory() {
  if (!('showDirectoryPicker' in window)) { alert('该浏览器不支持文件夹导入'); return; }
  const dir = await window.showDirectoryPicker();
  const items = [];
  for await (const entry of dir.values()) {
    if (entry.kind === 'file') {
      const file = await entry.getFile();
      if (!file.type.startsWith('audio') && !/\.(mp3|flac|wav|ogg)$/i.test(file.name)) continue;
      const url = URL.createObjectURL(file);
      items.push({ title: file.name, url, type: 'file', file, size: file.size });
    }
  }
  addToPlaylist(items);
  if (state.currentIndex === -1 && state.playlist.length) playIndex(0);
}

function playIndex(idx) {
  if (idx < 0 || idx >= state.playlist.length) return;
  state.currentIndex = idx;
  const track = state.playlist[idx];
  audio.src = track.url;
  audio.loop = state.isLoop;
  audio.play().catch(console.error);
  renderPlaylist();
  setNowPlaying(track.title, track.size ? `${(track.size / 1024 / 1024).toFixed(2)} MB` : track.url);
  miniTitle.textContent = track.title;
  updateMediaSession(track);
  clearLyrics();
  pushHistory(track);
}

function removeIndex(idx) {
  if (idx < 0 || idx >= state.playlist.length) return;
  const [removed] = state.playlist.splice(idx, 1);
  if (removed?.type === 'file' && removed.url) URL.revokeObjectURL(removed.url);
  if (state.currentIndex === idx) {
    if (state.playlist.length) {
      state.currentIndex = Math.min(idx, state.playlist.length - 1);
      playIndex(state.currentIndex);
    } else {
      state.currentIndex = -1;
      audio.removeAttribute('src');
      setNowPlaying();
      renderPlaylist();
    }
  } else if (idx < state.currentIndex) {
    state.currentIndex -= 1;
    renderPlaylist();
  } else {
    renderPlaylist();
  }
}

function togglePlay() { if (audio.paused) play(); else pause(); }
function play() { audio.play().catch(console.error); playPauseBtn.textContent = '⏸ 暂停'; miniPlay.textContent = '⏸'; }
function pause() { audio.pause(); playPauseBtn.textContent = '▶️ 播放'; miniPlay.textContent = '▶️'; }
function prev() {
  if (!state.playlist.length) return;
  if (state.isShuffle) return playIndex(Math.floor(Math.random() * state.playlist.length));
  const idx = state.currentIndex - 1 < 0 ? state.playlist.length - 1 : state.currentIndex - 1;
  playIndex(idx);
}
function next() {
  if (!state.playlist.length) return;
  if (state.isShuffle) return playIndex(Math.floor(Math.random() * state.playlist.length));
  const idx = (state.currentIndex + 1) % state.playlist.length;
  playIndex(idx);
}

function clearLyrics() { state.lyrics = []; renderLyrics(); }
function loadLRCFromFile(file) { const r = new FileReader(); r.onload = () => { state.lyrics = parseLRC(String(r.result||'')); renderLyrics(); }; r.readAsText(file, 'utf-8'); }
async function loadLRCFromURL(url) { const res = await fetch(url); const text = await res.text(); state.lyrics = parseLRC(text); renderLyrics(); }

playPauseBtn.addEventListener('click', togglePlay);
prevBtn.addEventListener('click', prev);
nextBtn.addEventListener('click', next);
loopBtn.addEventListener('click', () => { state.isLoop = !state.isLoop; loopBtn.classList.toggle('active', state.isLoop); loopBtn.setAttribute('aria-pressed', String(state.isLoop)); audio.loop = state.isLoop; });
shuffleBtn.addEventListener('click', () => { state.isShuffle = !state.isShuffle; shuffleBtn.classList.toggle('active', state.isShuffle); shuffleBtn.setAttribute('aria-pressed', String(state.isShuffle)); });

seek.addEventListener('input', () => { seek.dragging = true; timeEl.textContent = `${formatTime(Number(seek.value))} / ${formatTime(audio.duration||0)}`; });
seek.addEventListener('change', () => { audio.currentTime = Number(seek.value); seek.dragging = false; });
miniSeek.addEventListener('input', () => { miniSeek.dragging = true; miniTime.textContent = `${formatTime(Number(miniSeek.value))} / ${formatTime(audio.duration||0)}`; });
miniSeek.addEventListener('change', () => { audio.currentTime = Number(miniSeek.value); miniSeek.dragging = false; });

volume.value = '1';
volume.addEventListener('input', () => { audio.volume = Number(volume.value); });
muteBtn.addEventListener('click', () => { audio.muted = !audio.muted; muteBtn.textContent = audio.muted ? '🔈 取消静音' : '🔇 静音'; });

audio.addEventListener('timeupdate', updateTimeUI);
audio.addEventListener('durationchange', updateTimeUI);
audio.addEventListener('play', () => { playPauseBtn.textContent = '⏸ 暂停'; });
audio.addEventListener('pause', () => { playPauseBtn.textContent = '▶️ 播放'; });
audio.addEventListener('play', () => { miniPlay.textContent = '⏸'; });
audio.addEventListener('pause', () => { miniPlay.textContent = '▶️'; });
audio.addEventListener('ended', () => { if (!state.isLoop) next(); });

fileInput.addEventListener('change', (e) => handleFiles(e.target.files));
folderBtn.addEventListener('click', handleDirectory);
addUrlBtn.addEventListener('click', () => {
  const url = urlInput.value.trim();
  if (!url) return;
  addToPlaylist([{ title: url.split('/').pop() || url, url, type: 'url' }]);
  if (state.currentIndex === -1) playIndex(0);
  urlInput.value = '';
});

lrcInput.addEventListener('change', (e) => { const file = e.target.files?.[0]; if (file) loadLRCFromFile(file); });
clearLyricsBtn.addEventListener('click', clearLyrics);

document.addEventListener('keydown', (e) => {
  if (['INPUT', 'TEXTAREA'].includes(e.target?.tagName)) return;
  if (e.code === 'Space') { e.preventDefault(); togglePlay(); }
  if (e.code === 'ArrowRight') audio.currentTime = Math.min((audio.currentTime||0) + 5, audio.duration||0);
  if (e.code === 'ArrowLeft') audio.currentTime = Math.max((audio.currentTime||0) - 5, 0);
});

// Mini bar controls
miniPrev.addEventListener('click', prev);
miniPlay.addEventListener('click', () => { if (audio.paused) play(); else pause(); });
miniNext.addEventListener('click', next);

audio.addEventListener('loadedmetadata', async () => {
  const src = audio.currentSrc;
  try {
    const u = new URL(src);
    const base = u.pathname.replace(/\.[^/.]+$/, '');
    const lrcUrl = `${u.origin}${base}.lrc`;
    const res = await fetch(lrcUrl, { method: 'GET' });
    if (res.ok) { const text = await res.text(); state.lyrics = parseLRC(text); renderLyrics(); }
  } catch (_) {}
});

// Web Audio API: EQ + Visualizer
let audioCtx; let srcNode; let analyser; let eqNodes = []; let gainNodes = [];
const EQ_FREQS = [60, 170, 350, 1000, 3500];
function ensureAudioGraph() {
  if (audioCtx) return;
  audioCtx = new (window.AudioContext || window.webkitAudioContext)();
  srcNode = audioCtx.createMediaElementSource(audio);
  analyser = audioCtx.createAnalyser();
  analyser.fftSize = 2048;
  eqNodes = EQ_FREQS.map((f) => {
    const biquad = audioCtx.createBiquadFilter();
    biquad.type = 'peaking';
    biquad.frequency.value = f;
    biquad.Q.value = 1.0;
    biquad.gain.value = 0;
    return biquad;
  });
  // connect: src -> eq -> analyser -> destination
  let last = srcNode;
  for (const n of eqNodes) { last.connect(n); last = n; }
  last.connect(analyser);
  analyser.connect(audioCtx.destination);
}

function setEqGain(bandIndex, db) {
  ensureAudioGraph();
  if (eqNodes[bandIndex]) eqNodes[bandIndex].gain.value = db;
}

function resetEq() {
  ensureAudioGraph();
  eqNodes.forEach((n) => { n.gain.value = 0; });
  document.querySelectorAll('.eq input[type="range"]').forEach((el) => { el.value = '0'; });
}

function startVisualizer() {
  ensureAudioGraph();
  const bigCanvas = vizCanvas; if (!bigCanvas) return;
  const bigCtx = bigCanvas.getContext('2d');
  const miniCanvas = miniViz; const miniCtx = miniCanvas ? miniCanvas.getContext('2d') : null;
  const bufferLength = analyser.frequencyBinCount;
  const dataArray = new Uint8Array(bufferLength);
  function draw() {
    requestAnimationFrame(draw);
    analyser.getByteFrequencyData(dataArray);
    // big viz
    const { width: bw, height: bh } = bigCanvas;
    bigCtx.clearRect(0, 0, bw, bh);
    const barCount = 64; const step = Math.floor(bufferLength / barCount); const barWidth = bw / barCount;
    for (let i = 0; i < barCount; i++) {
      const v = dataArray[i * step] / 255; const h = v * bh;
      bigCtx.fillStyle = `rgba(124,156,255,${0.5 + v * 0.5})`;
      bigCtx.fillRect(i * barWidth + 1, bh - h, barWidth - 2, h);
    }
    // mini viz
    if (miniCtx && miniCanvas) {
      const { width: mw, height: mh } = miniCanvas;
      miniCtx.clearRect(0, 0, mw, mh);
      const mCount = 32; const mStep = Math.floor(bufferLength / mCount); const mBarW = mw / mCount;
      for (let i = 0; i < mCount; i++) {
        const v = dataArray[i * mStep] / 255; const h = v * mh;
        miniCtx.fillStyle = `rgba(34,211,238,${0.4 + v * 0.6})`;
        miniCtx.fillRect(i * mBarW + 1, mh - h, mBarW - 2, h);
      }
    }
  }
  draw();
}

// Bind EQ sliders
document.querySelectorAll('.eq input[type="range"]').forEach((el) => {
  el.addEventListener('input', (e) => {
    const band = Number(e.target.dataset.band);
    const val = Number(e.target.value);
    setEqGain(band, val);
  });
});
eqResetBtn?.addEventListener('click', resetEq);
clearHistoryBtn?.addEventListener('click', () => { state.history = []; saveHistory(); renderHistory(); });

audio.addEventListener('play', () => { ensureAudioGraph(); startVisualizer(); });

// init
loadHistory();
renderHistory();

// Tabs logic
document.querySelectorAll('.tab-btn').forEach((btn) => {
  btn.addEventListener('click', () => {
    document.querySelectorAll('.tab-btn').forEach((b) => b.classList.remove('active'));
    document.querySelectorAll('.tab-panel').forEach((p) => p.classList.remove('active'));
    btn.classList.add('active');
    const id = btn.dataset.tab;
    const panel = document.getElementById(id);
    if (panel) panel.classList.add('active');
  });
});

// Recent drawer
openHistoryBtn?.addEventListener('click', () => { recentDrawer?.setAttribute('aria-hidden', 'false'); });
closeHistoryBtn?.addEventListener('click', () => { recentDrawer?.setAttribute('aria-hidden', 'true'); });

// Search and sort
searchInput?.addEventListener('input', () => { state.filterText = searchInput.value || ''; renderPlaylist(); });
sortSelect?.addEventListener('change', () => { state.sortBy = sortSelect.value || 'added-asc'; renderPlaylist(); });


