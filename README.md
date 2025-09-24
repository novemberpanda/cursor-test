# 儿童简笔画填色图片生成器

这是一个专门为儿童设计的简笔画填色图片生成器，可以生成A4纸张大小的高质量填色图片。

## 功能特点

- 🎨 生成多种主题的简笔画：小猫、小狗、房子、花朵、太阳、蝴蝶等
- 📄 A4纸张大小（210mm × 297mm），适合打印
- 🖨️ 300 DPI高分辨率，打印效果清晰
- ✏️ 黑白线条设计，适合儿童填色
- 🌈 多个主题场景可选

## 系统要求

- Python 3.6 或更高版本
- macOS、Windows 或 Linux

## 在 macOS 上安装和运行

### 1. 安装 Python（如果尚未安装）

```bash
# 使用 Homebrew 安装 Python（推荐）
brew install python

# 或者从 python.org 下载安装包
```

### 2. 克隆或下载项目

```bash
# 如果使用 git
git clone <repository-url>
cd coloring-book-generator

# 或者直接下载项目文件到本地文件夹
```

### 3. 安装依赖

```bash
# 在项目目录中运行
pip3 install -r requirements.txt

# 或者手动安装
pip3 install matplotlib numpy pillow
```

### 4. 运行程序

```bash
python3 coloring_book_generator.py
```

## 生成的主题

程序会自动生成以下8种主题的填色图片：

1. **小猫花园主题** (`coloring_page_cat_garden.png`) - 可爱的小猫与花朵
2. **动物朋友主题** (`coloring_page_animals.png`) - 小猫和小狗一起玩耍
3. **美丽自然主题** (`coloring_page_nature.png`) - 大树、花朵、蝴蝶和白云
4. **温馨小屋主题** (`coloring_page_house.png`) - 房子、大树和花园
5. **海洋冒险主题** (`coloring_page_ocean.png`) - 小船、波浪和小鱼（线条更少）
6. **太空探索主题** (`coloring_page_space.png`) - 火箭、月亮和星星（线条更少）
7. **交通小车主题** (`coloring_page_transport.png`) - 小汽车、道路和信号灯（线条更少）
8. **综合场景主题** (`coloring_page_mixed.png`) - 包含多种元素的丰富场景

## 输出文件

所有生成的图片会保存在 `coloring_pages` 文件夹中，包括：

- `coloring_page_cat_garden.png`
- `coloring_page_animals.png`
- `coloring_page_nature.png`
- `coloring_page_house.png`
- `coloring_page_ocean.png`
- `coloring_page_space.png`
- `coloring_page_transport.png`
- `coloring_page_mixed.png`

## 图片规格

- **尺寸**: A4纸张 (210mm × 297mm)
- **分辨率**: 300 DPI
- **格式**: PNG
- **颜色**: 黑白线条
- **线条粗细**: 3-4像素，适合儿童填色

## 打印建议

1. 使用普通A4打印纸
2. 建议使用彩色喷墨或激光打印机
3. 打印设置选择"实际大小"或"100%缩放"
4. 确保纸张方向设置为"纵向"

## 填色工具建议

- 彩色铅笔 - 适合精细填色
- 蜡笔 - 适合大面积填色
- 水彩笔 - 颜色鲜艳
- 马克笔 - 效果明显
- 水彩颜料 - 适合高年级儿童

## 适用年龄

- **推荐年龄**: 3-12岁
- **3-5岁**: 大图案，粗线条，容易填色
- **6-8岁**: 中等复杂度，培养专注力
- **9-12岁**: 丰富细节，锻炼耐心和技巧

## 教育价值

- 🎯 培养专注力和耐心
- 🌈 认识颜色和搭配
- ✋ 锻炼手眼协调能力
- 🧠 提升创造力和想象力
- 😊 放松心情，缓解压力

## 常见问题

### Q: 为什么生成的图片很大？
A: 图片使用300 DPI高分辨率，确保打印质量。如需要小文件，可以修改代码中的 `dpi` 参数。

### Q: 可以修改图片内容吗？
A: 可以！修改 `coloring_book_generator.py` 中的绘图函数来自定义图案。

### Q: 在 macOS 上遇到权限问题怎么办？
A: 确保使用 `pip3` 而不是 `pip`，必要时使用 `sudo` 或创建虚拟环境。

### Q: 如何创建虚拟环境？
```bash
python3 -m venv coloring_env
source coloring_env/bin/activate
pip install -r requirements.txt
python coloring_book_generator.py
```

## 自定义开发

### 添加新的图案

在 `ColoringBookGenerator` 类中添加新的绘图方法：

```python
def draw_new_shape(self, ax, x=5, y=7, size=1):
    # 在这里添加你的绘图代码
    pass
```

### 创建新主题

在 `generate_scene()` 方法中添加新的场景类型：

```python
elif scene_type == "my_theme":
    # 组合不同的图案创建新主题
    self.draw_cat(ax, x=3, y=8, size=1)
    self.draw_flower(ax, x=7, y=6, size=0.8)
```

## 技术说明

程序使用以下技术栈：

- **matplotlib**: 绘图库，用于创建简笔画
- **numpy**: 数值计算，用于角度和位置计算
- **Pillow**: 图像处理库，用于图片保存

主要组件：

- `ColoringBookGenerator`: 主要的生成器类
- `draw_*()` 方法: 各种图案的绘制函数
- `generate_scene()`: 场景组合函数
- `save_image()`: 图片保存函数

## 许可证

本项目采用MIT许可证，可自由使用和修改。

## 贡献

欢迎提交问题和改进建议！

---

**祝小朋友们填色愉快！** 🌈✨

## 示例输出

运行程序后，你会看到类似以下的输出：

```
==================================================
      儿童简笔画填色图片生成器
==================================================
正在生成儿童简笔画填色图片...

🎨 生成小猫花园主题...
填色图片已保存为: coloring_pages/coloring_page_cat_garden.png
🎨 生成动物朋友主题...
填色图片已保存为: coloring_pages/coloring_page_animals.png
🎨 生成美丽自然主题...
填色图片已保存为: coloring_pages/coloring_page_nature.png
🎨 生成温馨小屋主题...
填色图片已保存为: coloring_pages/coloring_page_house.png
🎨 生成综合场景主题...
填色图片已保存为: coloring_pages/coloring_page_mixed.png

==================================================
✅ 所有填色图片生成完成！
==================================================
```