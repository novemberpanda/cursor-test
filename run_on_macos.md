# 在 macOS 上运行儿童简笔画填色图片生成器

## 快速开始指南

### 1. 检查 Python 版本

```bash
python3 --version
```

如果没有安装 Python 或版本低于 3.6，请先安装：

```bash
# 使用 Homebrew（推荐）
brew install python

# 或者从 https://www.python.org 下载安装包
```

### 2. 下载项目文件

从 GitHub 下载项目到本地：

```bash
# 方法1：使用 git clone
git clone https://github.com/novemberpanda/cursor-test.git
cd cursor-test

# 方法2：直接下载 ZIP 文件并解压
```

### 3. 安装依赖

在项目目录中运行：

```bash
pip3 install -r requirements.txt
```

如果遇到权限问题，可以使用：

```bash
pip3 install --user -r requirements.txt
```

### 4. 运行程序

```bash
python3 coloring_book_generator.py
```

### 5. 查看生成的图片

程序运行完成后，在 `coloring_pages` 文件夹中查看生成的填色图片：

```bash
open coloring_pages/
```

## 可能遇到的问题及解决方案

### 问题1：命令未找到

如果遇到 `python3: command not found`：

```bash
# 检查是否安装了 Python
which python3
which python

# 如果只有 python，可以使用
python coloring_book_generator.py
```

### 问题2：模块未找到

如果遇到 `ModuleNotFoundError`：

```bash
# 确保在正确的目录
ls -la
# 应该能看到 coloring_book_generator.py 和 requirements.txt

# 重新安装依赖
pip3 install matplotlib numpy pillow
```

### 问题3：权限问题

如果遇到权限错误：

```bash
# 使用虚拟环境（推荐）
python3 -m venv coloring_env
source coloring_env/bin/activate
pip install -r requirements.txt
python coloring_book_generator.py
```

### 问题4：图片无法显示

程序生成的是PNG文件，可以用以下方式打开：

```bash
# 在 Finder 中打开
open coloring_pages/

# 用预览应用打开特定图片
open coloring_pages/coloring_page_cat_garden.png
```

## 打印设置

1. 打开生成的 PNG 文件
2. 在预览应用中选择"文件" > "打印"
3. 设置纸张大小为 A4
4. 选择"实际大小"或"100%缩放"
5. 确保方向为"纵向"

## 生成的文件说明

| 文件名 | 主题 | 描述 |
|--------|------|------|
| `coloring_page_cat_garden.png` | 小猫花园 | 可爱小猫与花朵的温馨场景 |
| `coloring_page_animals.png` | 动物朋友 | 小猫和小狗一起玩耍 |
| `coloring_page_nature.png` | 自然风光 | 大树、花朵、蝴蝶和白云 |
| `coloring_page_house.png` | 温馨小屋 | 房子、大树和花园场景 |
| `coloring_page_mixed.png` | 综合场景 | 包含多种元素的丰富画面 |

享受填色的乐趣吧！🎨