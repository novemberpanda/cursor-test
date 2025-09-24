#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
儿童简笔画填色图片生成器
生成A4纸张大小的简笔画图片，适合儿童填色

使用方法：
1. 安装依赖：pip install matplotlib numpy pillow
2. 运行程序：python coloring_book_generator.py
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import Circle, Rectangle, Polygon, Ellipse, Arc
import numpy as np
import random
import os

class ColoringBookGenerator:
    def __init__(self):
        """初始化生成器，设置A4纸张尺寸"""
        # A4纸张尺寸 (210mm x 297mm)
        self.width_mm = 210
        self.height_mm = 297
        
    def create_figure(self):
        """创建A4大小的画布"""
        # 转换为英寸 (1英寸 = 25.4mm)
        fig_width = self.width_mm / 25.4
        fig_height = self.height_mm / 25.4
        
        fig, ax = plt.subplots(figsize=(fig_width, fig_height))
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 14.14)  # 保持A4比例
        ax.set_aspect('equal')
        ax.axis('off')
        
        # 设置白色背景
        fig.patch.set_facecolor('white')
        ax.set_facecolor('white')
        
        return fig, ax
    
    def draw_cat(self, ax, x=5, y=7, size=1):
        """绘制小猫简笔画"""
        # 头部（圆形）
        head = Circle((x, y), size, fill=False, edgecolor='black', linewidth=4)
        ax.add_patch(head)
        
        # 耳朵
        ear1 = patches.Polygon([
            (x-0.7*size, y+0.5*size), 
            (x-0.3*size, y+1.2*size), 
            (x-0.1*size, y+0.7*size)
        ], fill=False, edgecolor='black', linewidth=4)
        ear2 = patches.Polygon([
            (x+0.1*size, y+0.7*size), 
            (x+0.3*size, y+1.2*size), 
            (x+0.7*size, y+0.5*size)
        ], fill=False, edgecolor='black', linewidth=4)
        ax.add_patch(ear1)
        ax.add_patch(ear2)
        
        # 眼睛
        eye1 = Circle((x-0.3*size, y+0.2*size), 0.15*size, fill=False, edgecolor='black', linewidth=4)
        eye2 = Circle((x+0.3*size, y+0.2*size), 0.15*size, fill=False, edgecolor='black', linewidth=4)
        ax.add_patch(eye1)
        ax.add_patch(eye2)
        
        # 鼻子（小三角形）
        nose = patches.Polygon([
            (x, y-0.1*size), 
            (x-0.1*size, y-0.3*size), 
            (x+0.1*size, y-0.3*size)
        ], fill=False, edgecolor='black', linewidth=4)
        ax.add_patch(nose)
        
        # 嘴巴（W形状）
        ax.plot([x-0.2*size, x, x+0.2*size], [y-0.5*size, y-0.4*size, y-0.5*size], 
                'k-', linewidth=4)
        ax.plot([x-0.1*size, x-0.3*size], [y-0.45*size, y-0.6*size], 'k-', linewidth=4)
        ax.plot([x+0.1*size, x+0.3*size], [y-0.45*size, y-0.6*size], 'k-', linewidth=4)
        
        # 胡须
        ax.plot([x-0.8*size, x-0.5*size], [y, y+0.1*size], 'k-', linewidth=3)
        ax.plot([x-0.8*size, x-0.5*size], [y-0.2*size, y-0.1*size], 'k-', linewidth=3)
        ax.plot([x+0.5*size, x+0.8*size], [y+0.1*size, y], 'k-', linewidth=3)
        ax.plot([x+0.5*size, x+0.8*size], [y-0.1*size, y-0.2*size], 'k-', linewidth=3)
        
        # 身体（椭圆形）
        body = Ellipse((x, y-2*size), 1.4*size, 1.8*size, fill=False, edgecolor='black', linewidth=4)
        ax.add_patch(body)
        
        # 腿
        for i, leg_x in enumerate([x-0.6*size, x-0.1*size, x+0.3*size, x+0.8*size]):
            leg = Rectangle((leg_x-0.15*size, y-3.2*size), 0.3*size, 0.8*size, 
                           fill=False, edgecolor='black', linewidth=4)
            ax.add_patch(leg)
            # 爪子
            paw = Circle((leg_x, y-3.4*size), 0.2*size, fill=False, edgecolor='black', linewidth=4)
            ax.add_patch(paw)
        
        # 尾巴
        tail = Arc((x+1.2*size, y-1*size), 1*size, 2*size, angle=45, theta1=0, theta2=180, 
                  linewidth=4, color='black', fill=False)
        ax.add_patch(tail)
    
    def draw_dog(self, ax, x=5, y=7, size=1):
        """绘制小狗简笔画"""
        # 头部（椭圆形）
        head = Ellipse((x, y), 1.4*size, 1.2*size, fill=False, edgecolor='black', linewidth=4)
        ax.add_patch(head)
        
        # 耳朵（垂下的）
        ear1 = Ellipse((x-0.6*size, y+0.3*size), 0.4*size, 0.8*size, 
                      fill=False, edgecolor='black', linewidth=4)
        ear2 = Ellipse((x+0.6*size, y+0.3*size), 0.4*size, 0.8*size, 
                      fill=False, edgecolor='black', linewidth=4)
        ax.add_patch(ear1)
        ax.add_patch(ear2)
        
        # 眼睛
        eye1 = Circle((x-0.3*size, y+0.1*size), 0.15*size, fill=False, edgecolor='black', linewidth=4)
        eye2 = Circle((x+0.3*size, y+0.1*size), 0.15*size, fill=False, edgecolor='black', linewidth=4)
        ax.add_patch(eye1)
        ax.add_patch(eye2)
        
        # 鼻子
        nose = Circle((x, y-0.3*size), 0.1*size, fill=True, color='black')
        ax.add_patch(nose)
        
        # 嘴巴
        mouth = Arc((x, y-0.6*size), 0.6*size, 0.4*size, angle=0, theta1=0, theta2=180, 
                   linewidth=4, color='black', fill=False)
        ax.add_patch(mouth)
        
        # 舌头
        tongue = Ellipse((x, y-0.8*size), 0.2*size, 0.3*size, fill=False, edgecolor='black', linewidth=4)
        ax.add_patch(tongue)
        
        # 身体
        body = Ellipse((x, y-2*size), 1.6*size, 1.8*size, fill=False, edgecolor='black', linewidth=4)
        ax.add_patch(body)
        
        # 腿
        for i, leg_x in enumerate([x-0.6*size, x-0.2*size, x+0.2*size, x+0.6*size]):
            leg = Rectangle((leg_x-0.125*size, y-3.2*size), 0.25*size, 0.8*size, 
                           fill=False, edgecolor='black', linewidth=4)
            ax.add_patch(leg)
            # 爪子
            paw = Circle((leg_x, y-3.4*size), 0.15*size, fill=False, edgecolor='black', linewidth=4)
            ax.add_patch(paw)
        
        # 尾巴（摇摆的）
        tail = Arc((x+1*size, y-1.5*size), 0.8*size, 1.5*size, angle=30, theta1=0, theta2=120, 
                  linewidth=4, color='black', fill=False)
        ax.add_patch(tail)
    
    def draw_flower(self, ax, x=5, y=7, size=1):
        """绘制花朵简笔画"""
        # 花心
        center = Circle((x, y), 0.3*size, fill=False, edgecolor='black', linewidth=4)
        ax.add_patch(center)
        
        # 花瓣（5片）
        for i in range(5):
            angle = i * 72 * np.pi / 180
            petal_x = x + 0.7*size * np.cos(angle)
            petal_y = y + 0.7*size * np.sin(angle)
            petal = Ellipse((petal_x, petal_y), 0.5*size, 0.8*size, 
                           angle=np.degrees(angle), fill=False, edgecolor='black', linewidth=4)
            ax.add_patch(petal)
        
        # 花茎
        ax.plot([x, x], [y-0.8*size, y-3*size], 'k-', linewidth=4)
        
        # 叶子
        leaf1_x = [x-0.3*size, x-0.8*size, x-0.2*size, x-0.3*size]
        leaf1_y = [y-1.5*size, y-1.8*size, y-2.2*size, y-1.5*size]
        leaf1 = patches.Polygon(list(zip(leaf1_x, leaf1_y)), fill=False, edgecolor='black', linewidth=4)
        ax.add_patch(leaf1)
        
        leaf2_x = [x+0.3*size, x+0.8*size, x+0.2*size, x+0.3*size]
        leaf2_y = [y-2*size, y-2.3*size, y-2.7*size, y-2*size]
        leaf2 = patches.Polygon(list(zip(leaf2_x, leaf2_y)), fill=False, edgecolor='black', linewidth=4)
        ax.add_patch(leaf2)
    
    def draw_house(self, ax, x=5, y=7, size=1):
        """绘制房子简笔画"""
        # 房屋主体
        house_body = Rectangle((x-1.5*size, y-2*size), 3*size, 2.5*size, 
                              fill=False, edgecolor='black', linewidth=4)
        ax.add_patch(house_body)
        
        # 屋顶
        roof = patches.Polygon([
            (x-1.8*size, y+0.5*size), 
            (x, y+1.5*size), 
            (x+1.8*size, y+0.5*size),
            (x-1.8*size, y+0.5*size)
        ], fill=False, edgecolor='black', linewidth=4)
        ax.add_patch(roof)
        
        # 门
        door = Rectangle((x-0.3*size, y-2*size), 0.6*size, 1.2*size, 
                        fill=False, edgecolor='black', linewidth=4)
        ax.add_patch(door)
        
        # 门把手
        handle = Circle((x+0.15*size, y-1.4*size), 0.05*size, fill=True, color='black')
        ax.add_patch(handle)
        
        # 窗户
        window1 = Rectangle((x-1.2*size, y-0.5*size), 0.6*size, 0.6*size, 
                           fill=False, edgecolor='black', linewidth=4)
        window2 = Rectangle((x+0.6*size, y-0.5*size), 0.6*size, 0.6*size, 
                           fill=False, edgecolor='black', linewidth=4)
        ax.add_patch(window1)
        ax.add_patch(window2)
        
        # 窗户十字
        ax.plot([x-0.9*size, x-0.9*size], [y-0.8*size, y-0.2*size], 'k-', linewidth=3)
        ax.plot([x-1.2*size, x-0.6*size], [y-0.5*size, y-0.5*size], 'k-', linewidth=3)
        ax.plot([x+0.9*size, x+0.9*size], [y-0.8*size, y-0.2*size], 'k-', linewidth=3)
        ax.plot([x+0.6*size, x+1.2*size], [y-0.5*size, y-0.5*size], 'k-', linewidth=3)
        
        # 烟囱
        chimney = Rectangle((x+0.8*size, y+0.8*size), 0.4*size, 0.8*size, 
                           fill=False, edgecolor='black', linewidth=4)
        ax.add_patch(chimney)
        
        # 烟雾
        for i, (smoke_x, smoke_y) in enumerate([
            (x+1*size, y+1.6*size), 
            (x+1.2*size, y+1.9*size), 
            (x+0.9*size, y+2.2*size)
        ]):
            smoke = Circle((smoke_x, smoke_y), 0.1*size, fill=False, edgecolor='black', linewidth=3)
            ax.add_patch(smoke)
    
    def draw_sun(self, ax, x=8, y=12, size=0.8):
        """绘制太阳简笔画"""
        # 太阳主体
        sun_body = Circle((x, y), size, fill=False, edgecolor='black', linewidth=4)
        ax.add_patch(sun_body)
        
        # 太阳光芒
        ray_length = 0.6*size
        for i in range(8):
            angle = i * 45 * np.pi / 180
            start_x = x + (size + 0.1) * np.cos(angle)
            start_y = y + (size + 0.1) * np.sin(angle)
            end_x = x + (size + ray_length) * np.cos(angle)
            end_y = y + (size + ray_length) * np.sin(angle)
            ax.plot([start_x, end_x], [start_y, end_y], 'k-', linewidth=4)
        
        # 笑脸
        eye1 = Circle((x-0.3*size, y+0.2*size), 0.1*size, fill=True, color='black')
        eye2 = Circle((x+0.3*size, y+0.2*size), 0.1*size, fill=True, color='black')
        ax.add_patch(eye1)
        ax.add_patch(eye2)
        
        mouth = Arc((x, y-0.2*size), 0.6*size, 0.4*size, angle=0, theta1=0, theta2=180, 
                   linewidth=4, color='black', fill=False)
        ax.add_patch(mouth)
    
    def draw_tree(self, ax, x=2, y=5, size=1):
        """绘制树木简笔画"""
        # 树干
        trunk = Rectangle((x-0.2*size, y-2*size), 0.4*size, 2*size, 
                         fill=False, edgecolor='black', linewidth=4)
        ax.add_patch(trunk)
        
        # 树冠（三个圆形重叠）
        crown1 = Circle((x, y+1*size), 1*size, fill=False, edgecolor='black', linewidth=4)
        crown2 = Circle((x-0.7*size, y+0.3*size), 0.8*size, fill=False, edgecolor='black', linewidth=4)
        crown3 = Circle((x+0.7*size, y+0.3*size), 0.8*size, fill=False, edgecolor='black', linewidth=4)
        ax.add_patch(crown1)
        ax.add_patch(crown2)
        ax.add_patch(crown3)
        
        # 苹果（装饰）
        apple_positions = [
            (x-0.3*size, y+0.8*size),
            (x+0.4*size, y+1.2*size),
            (x-0.6*size, y+0.5*size),
            (x+0.2*size, y+0.6*size)
        ]
        for apple_x, apple_y in apple_positions:
            apple = Circle((apple_x, apple_y), 0.12*size, fill=False, edgecolor='black', linewidth=3)
            ax.add_patch(apple)
    
    def draw_butterfly(self, ax, x=7, y=10, size=0.5):
        """绘制蝴蝶简笔画"""
        # 身体
        ax.plot([x, x], [y-size, y+size], 'k-', linewidth=4)
        
        # 触角
        ax.plot([x, x-0.2*size], [y+size, y+1.3*size], 'k-', linewidth=3)
        ax.plot([x, x+0.2*size], [y+size, y+1.3*size], 'k-', linewidth=3)
        
        # 触角末端
        ax.plot([x-0.2*size], [y+1.3*size], 'ko', markersize=4)
        ax.plot([x+0.2*size], [y+1.3*size], 'ko', markersize=4)
        
        # 翅膀
        wing1 = Ellipse((x-0.6*size, y+0.3*size), 0.8*size, 1.2*size, 
                       fill=False, edgecolor='black', linewidth=4)
        wing2 = Ellipse((x+0.6*size, y+0.3*size), 0.8*size, 1.2*size, 
                       fill=False, edgecolor='black', linewidth=4)
        wing3 = Ellipse((x-0.5*size, y-0.5*size), 0.6*size, 0.8*size, 
                       fill=False, edgecolor='black', linewidth=4)
        wing4 = Ellipse((x+0.5*size, y-0.5*size), 0.6*size, 0.8*size, 
                       fill=False, edgecolor='black', linewidth=4)
        
        ax.add_patch(wing1)
        ax.add_patch(wing2)
        ax.add_patch(wing3)
        ax.add_patch(wing4)
        
        # 翅膀装饰
        for wing_x in [x-0.6*size, x+0.6*size]:
            for wing_y in [y+0.5*size, y+0.1*size]:
                spot = Circle((wing_x, wing_y), 0.1*size, fill=False, edgecolor='black', linewidth=3)
                ax.add_patch(spot)
    
    def add_grass(self, ax):
        """添加草地装饰"""
        grass_y = 2.5
        for x_pos in np.linspace(0.5, 9.5, 25):
            grass_height = random.uniform(0.2, 0.6)
            # 草的形状更自然
            grass_curve = random.uniform(-0.1, 0.1)
            ax.plot([x_pos, x_pos + grass_curve], [grass_y, grass_y + grass_height], 
                   'k-', linewidth=3)
    
    def add_clouds(self, ax):
        """添加云朵装饰"""
        cloud_positions = [(1.5, 11.5, 0.8), (3.5, 12, 0.6), (6, 11.8, 0.7)]
        
        for cloud_x, cloud_y, cloud_size in cloud_positions:
            # 云朵由多个圆组成
            cloud_circles = [
                (cloud_x, cloud_y, cloud_size),
                (cloud_x + 0.7*cloud_size, cloud_y, 0.8*cloud_size),
                (cloud_x + 1.2*cloud_size, cloud_y + 0.2*cloud_size, 0.6*cloud_size),
                (cloud_x + 0.3*cloud_size, cloud_y + 0.3*cloud_size, 0.7*cloud_size)
            ]
            
            for cx, cy, cs in cloud_circles:
                cloud = Circle((cx, cy), cs, fill=False, edgecolor='black', linewidth=3)
                ax.add_patch(cloud)
    
    def generate_scene(self, scene_type="mixed"):
        """生成完整的填色场景"""
        fig, ax = self.create_figure()
        
        if scene_type == "animals":
            # 动物主题
            self.draw_cat(ax, x=3, y=10, size=1.2)
            self.draw_dog(ax, x=7, y=10, size=1.2)
            self.draw_sun(ax, x=8.5, y=12.5, size=0.8)
            self.draw_butterfly(ax, x=5, y=12, size=0.6)
            self.add_grass(ax)
            
        elif scene_type == "nature":
            # 自然主题
            self.draw_tree(ax, x=2, y=8, size=1.5)
            self.draw_flower(ax, x=5, y=6, size=1.2)
            self.draw_flower(ax, x=7.5, y=5.5, size=0.9)
            self.draw_butterfly(ax, x=6.5, y=8.5, size=0.7)
            self.draw_sun(ax, x=8.5, y=12.5, size=0.8)
            self.add_grass(ax)
            self.add_clouds(ax)
            
        elif scene_type == "house":
            # 房屋主题
            self.draw_house(ax, x=5, y=8, size=1.2)
            self.draw_tree(ax, x=1.5, y=6, size=1)
            self.draw_sun(ax, x=8.5, y=12.5, size=0.8)
            self.draw_flower(ax, x=8, y=4.5, size=0.8)
            self.add_grass(ax)
            self.add_clouds(ax)
            
        elif scene_type == "cat_garden":
            # 小猫花园主题
            self.draw_cat(ax, x=5, y=9, size=1.5)
            self.draw_flower(ax, x=2, y=5, size=1)
            self.draw_flower(ax, x=8, y=4.5, size=0.9)
            self.draw_butterfly(ax, x=7, y=7, size=0.6)
            self.draw_sun(ax, x=8.5, y=12.5, size=0.8)
            self.add_grass(ax)
            
        else:  # mixed - 综合主题
            # 混合主题 - 最丰富的场景
            self.draw_house(ax, x=5, y=9, size=1)
            self.draw_cat(ax, x=2.5, y=6, size=0.9)
            self.draw_tree(ax, x=8, y=7, size=1.1)
            self.draw_flower(ax, x=7, y=4.5, size=0.7)
            self.draw_butterfly(ax, x=6, y=11, size=0.5)
            self.draw_sun(ax, x=8.5, y=12.5, size=0.8)
            self.add_grass(ax)
        
        return fig
    
    def save_image(self, fig, filename, dpi=300):
        """保存图片为高质量PNG格式"""
        # 确保输出目录存在
        output_dir = "coloring_pages"
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        filepath = os.path.join(output_dir, filename)
        fig.savefig(filepath, dpi=dpi, bbox_inches='tight', 
                   facecolor='white', edgecolor='none', pad_inches=0.2)
        plt.close(fig)
        print(f"填色图片已保存为: {filepath}")
        return filepath

def main():
    """主函数"""
    print("=" * 50)
    print("      儿童简笔画填色图片生成器")
    print("=" * 50)
    
    generator = ColoringBookGenerator()
    
    # 生成不同主题的填色图片
    themes = {
        "cat_garden": "小猫花园主题",
        "animals": "动物朋友主题",
        "nature": "美丽自然主题", 
        "house": "温馨小屋主题",
        "mixed": "综合场景主题"
    }
    
    print("正在生成儿童简笔画填色图片...")
    print()
    
    generated_files = []
    
    for theme, description in themes.items():
        print(f"🎨 生成{description}...")
        try:
            fig = generator.generate_scene(theme)
            filename = f"coloring_page_{theme}.png"
            filepath = generator.save_image(fig, filename)
            generated_files.append(filepath)
        except Exception as e:
            print(f"❌ 生成{description}时出错: {e}")
    
    print()
    print("=" * 50)
    print("✅ 所有填色图片生成完成！")
    print()
    print("📋 图片规格信息：")
    print("   • 尺寸：A4纸张大小 (210mm × 297mm)")
    print("   • 分辨率：300 DPI（适合高质量打印）")
    print("   • 格式：PNG，黑白线条")
    print("   • 线条粗细：适合儿童填色")
    print()
    print("📁 生成的文件：")
    for filepath in generated_files:
        print(f"   • {filepath}")
    print()
    print("💡 使用建议：")
    print("   • 可直接打印在A4纸上")
    print("   • 适合3-12岁儿童填色")
    print("   • 建议使用彩色笔、蜡笔或水彩笔")
    print("   • 线条粗细适中，易于填色")
    print("=" * 50)

if __name__ == "__main__":
    main()