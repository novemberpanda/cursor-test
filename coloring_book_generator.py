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
from matplotlib.patches import Circle, Rectangle, Polygon, Ellipse, Arc, FancyBboxPatch
import numpy as np
import random
import os

class ColoringBookGenerator:
    def __init__(self):
        """初始化生成器，设置A4纸张尺寸"""
        # A4纸张尺寸 (210mm x 297mm)
        self.width_mm = 210
        self.height_mm = 297
        # 简约卡通风格：主线更粗，细节更细；线端圆角
        self.lw_main = 4.5
        self.lw_detail = 3.0
        plt.rcParams['lines.solid_capstyle'] = 'round'
        plt.rcParams['lines.solid_joinstyle'] = 'round'
        
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

    def draw_frame(self, ax):
        """绘制圆角页面边框（柔和卡通风）"""
        frame = FancyBboxPatch((0.25, 0.25), 9.5, 13.64,
                               boxstyle="round,pad=0.15,rounding_size=0.35",
                               fill=False, edgecolor='black', linewidth=self.lw_detail)
        ax.add_patch(frame)
    
    def draw_cat(self, ax, x=5, y=7, size=1):
        """绘制小猫简笔画"""
        # 头部（圆形）
        head = Circle((x, y), size, fill=False, edgecolor='black', linewidth=self.lw_main)
        ax.add_patch(head)
        
        # 耳朵
        ear1 = patches.Polygon([
            (x-0.7*size, y+0.5*size), 
            (x-0.3*size, y+1.2*size), 
            (x-0.1*size, y+0.7*size)
        ], fill=False, edgecolor='black', linewidth=self.lw_main)
        ear2 = patches.Polygon([
            (x+0.1*size, y+0.7*size), 
            (x+0.3*size, y+1.2*size), 
            (x+0.7*size, y+0.5*size)
        ], fill=False, edgecolor='black', linewidth=self.lw_main)
        ax.add_patch(ear1)
        ax.add_patch(ear2)
        
        # 眼睛
        eye1 = Circle((x-0.3*size, y+0.2*size), 0.15*size, fill=False, edgecolor='black', linewidth=self.lw_detail)
        eye2 = Circle((x+0.3*size, y+0.2*size), 0.15*size, fill=False, edgecolor='black', linewidth=self.lw_detail)
        ax.add_patch(eye1)
        ax.add_patch(eye2)
        
        # 鼻子（小三角形）
        nose = patches.Polygon([
            (x, y-0.1*size), 
            (x-0.1*size, y-0.3*size), 
            (x+0.1*size, y-0.3*size)
        ], fill=False, edgecolor='black', linewidth=self.lw_detail)
        ax.add_patch(nose)
        
        # 嘴巴（简化）
        ax.plot([x-0.2*size, x+0.2*size], [y-0.5*size, y-0.5*size], 'k-', linewidth=self.lw_detail)
        
        # 胡须（减少数量）
        ax.plot([x-0.8*size, x-0.5*size], [y-0.1*size, y-0.1*size], 'k-', linewidth=self.lw_detail)
        ax.plot([x+0.5*size, x+0.8*size], [y-0.1*size, y-0.1*size], 'k-', linewidth=self.lw_detail)
        
        # 身体（椭圆形）
        body = Ellipse((x, y-2*size), 1.4*size, 1.8*size, fill=False, edgecolor='black', linewidth=self.lw_main)
        ax.add_patch(body)
        
        # 腿
        for i, leg_x in enumerate([x-0.6*size, x-0.1*size, x+0.3*size, x+0.8*size]):
            leg = Rectangle((leg_x-0.15*size, y-3.2*size), 0.3*size, 0.8*size, 
                           fill=False, edgecolor='black', linewidth=self.lw_main)
            ax.add_patch(leg)
            # 爪子
            paw = Circle((leg_x, y-3.4*size), 0.2*size, fill=False, edgecolor='black', linewidth=self.lw_detail)
            ax.add_patch(paw)
        
        # 尾巴
        tail = Arc((x+1.2*size, y-1*size), 1*size, 2*size, angle=45, theta1=0, theta2=180, 
                  linewidth=self.lw_detail, color='black', fill=False)
        ax.add_patch(tail)
    
    def draw_dog(self, ax, x=5, y=7, size=1):
        """绘制小狗简笔画"""
        # 头部（椭圆形）
        head = Ellipse((x, y), 1.4*size, 1.2*size, fill=False, edgecolor='black', linewidth=self.lw_main)
        ax.add_patch(head)
        
        # 耳朵（垂下的）
        ear1 = Ellipse((x-0.6*size, y+0.3*size), 0.4*size, 0.8*size, 
                      fill=False, edgecolor='black', linewidth=self.lw_main)
        ear2 = Ellipse((x+0.6*size, y+0.3*size), 0.4*size, 0.8*size, 
                      fill=False, edgecolor='black', linewidth=self.lw_main)
        ax.add_patch(ear1)
        ax.add_patch(ear2)
        
        # 眼睛
        eye1 = Circle((x-0.3*size, y+0.1*size), 0.15*size, fill=False, edgecolor='black', linewidth=self.lw_detail)
        eye2 = Circle((x+0.3*size, y+0.1*size), 0.15*size, fill=False, edgecolor='black', linewidth=self.lw_detail)
        ax.add_patch(eye1)
        ax.add_patch(eye2)
        
        # 鼻子
        nose = Circle((x, y-0.3*size), 0.1*size, fill=True, color='black')
        ax.add_patch(nose)
        
        # 嘴巴
        mouth = Arc((x, y-0.6*size), 0.6*size, 0.4*size, angle=0, theta1=0, theta2=180, 
                   linewidth=self.lw_detail, color='black', fill=False)
        ax.add_patch(mouth)
        
        # 舌头（省略以减少线条）
        
        # 身体
        body = Ellipse((x, y-2*size), 1.6*size, 1.8*size, fill=False, edgecolor='black', linewidth=self.lw_main)
        ax.add_patch(body)
        
        # 腿
        for i, leg_x in enumerate([x-0.6*size, x-0.2*size, x+0.2*size, x+0.6*size]):
            leg = Rectangle((leg_x-0.125*size, y-3.2*size), 0.25*size, 0.8*size, 
                           fill=False, edgecolor='black', linewidth=self.lw_main)
            ax.add_patch(leg)
            # 爪子
            paw = Circle((leg_x, y-3.4*size), 0.15*size, fill=False, edgecolor='black', linewidth=self.lw_detail)
            ax.add_patch(paw)
        
        # 尾巴（简化）
        tail = Arc((x+1*size, y-1.5*size), 0.6*size, 1.0*size, angle=30, theta1=0, theta2=100, 
                  linewidth=self.lw_detail, color='black', fill=False)
        ax.add_patch(tail)
    
    def draw_flower(self, ax, x=5, y=7, size=1):
        """绘制花朵简笔画"""
        # 花心
        center = Circle((x, y), 0.3*size, fill=False, edgecolor='black', linewidth=self.lw_main)
        ax.add_patch(center)
        
        # 花瓣（减少为4片）
        for i in range(4):
            angle = i * 72 * np.pi / 180
            petal_x = x + 0.7*size * np.cos(angle)
            petal_y = y + 0.7*size * np.sin(angle)
            petal = Ellipse((petal_x, petal_y), 0.5*size, 0.8*size, 
                           angle=np.degrees(angle), fill=False, edgecolor='black', linewidth=self.lw_main)
            ax.add_patch(petal)
        
        # 花茎
        ax.plot([x, x], [y-0.8*size, y-3*size], 'k-', linewidth=self.lw_main)
        
        # 叶子
        leaf1_x = [x-0.3*size, x-0.8*size, x-0.2*size, x-0.3*size]
        leaf1_y = [y-1.5*size, y-1.8*size, y-2.2*size, y-1.5*size]
        leaf1 = patches.Polygon(list(zip(leaf1_x, leaf1_y)), fill=False, edgecolor='black', linewidth=self.lw_main)
        ax.add_patch(leaf1)
        
        leaf2_x = [x+0.3*size, x+0.8*size, x+0.2*size, x+0.3*size]
        leaf2_y = [y-2*size, y-2.3*size, y-2.7*size, y-2*size]
        leaf2 = patches.Polygon(list(zip(leaf2_x, leaf2_y)), fill=False, edgecolor='black', linewidth=self.lw_main)
        ax.add_patch(leaf2)
    
    def draw_house(self, ax, x=5, y=7, size=1):
        """绘制房子简笔画"""
        # 房屋主体
        house_body = Rectangle((x-1.5*size, y-2*size), 3*size, 2.5*size, 
                              fill=False, edgecolor='black', linewidth=self.lw_main)
        ax.add_patch(house_body)
        
        # 屋顶
        roof = patches.Polygon([
            (x-1.8*size, y+0.5*size), 
            (x, y+1.5*size), 
            (x+1.8*size, y+0.5*size),
            (x-1.8*size, y+0.5*size)
        ], fill=False, edgecolor='black', linewidth=self.lw_main)
        ax.add_patch(roof)
        
        # 门
        door = Rectangle((x-0.3*size, y-2*size), 0.6*size, 1.2*size, 
                        fill=False, edgecolor='black', linewidth=self.lw_main)
        ax.add_patch(door)
        
        # 门把手
        handle = Circle((x+0.15*size, y-1.4*size), 0.05*size, fill=True, color='black')
        ax.add_patch(handle)
        
        # 窗户
        window1 = Rectangle((x-1.2*size, y-0.5*size), 0.6*size, 0.6*size, 
                           fill=False, edgecolor='black', linewidth=self.lw_main)
        window2 = Rectangle((x+0.6*size, y-0.5*size), 0.6*size, 0.6*size, 
                           fill=False, edgecolor='black', linewidth=self.lw_main)
        ax.add_patch(window1)
        ax.add_patch(window2)
        
        # 窗户十字（每个窗户一条线，减少线条）
        ax.plot([x-1.2*size, x-0.6*size], [y-0.5*size, y-0.5*size], 'k-', linewidth=self.lw_detail)
        ax.plot([x+0.6*size, x+1.2*size], [y-0.5*size, y-0.5*size], 'k-', linewidth=self.lw_detail)
        
        # 烟囱
        chimney = Rectangle((x+0.8*size, y+0.8*size), 0.4*size, 0.8*size, 
                           fill=False, edgecolor='black', linewidth=4)
        ax.add_patch(chimney)
        
        # 烟雾（减少数量）
        for smoke_x, smoke_y in [
            (x+1*size, y+1.6*size),
            (x+1.2*size, y+1.9*size)
        ]:
            smoke = Circle((smoke_x, smoke_y), 0.1*size, fill=False, edgecolor='black', linewidth=self.lw_detail)
            ax.add_patch(smoke)
    
    def draw_sun(self, ax, x=8, y=12, size=0.8):
        """绘制太阳简笔画"""
        # 太阳主体
        sun_body = Circle((x, y), size, fill=False, edgecolor='black', linewidth=self.lw_main)
        ax.add_patch(sun_body)
        
        # 太阳光芒（减少条数）
        ray_length = 0.6*size
        for i in range(6):
            angle = i * 45 * np.pi / 180
            start_x = x + (size + 0.1) * np.cos(angle)
            start_y = y + (size + 0.1) * np.sin(angle)
            end_x = x + (size + ray_length) * np.cos(angle)
            end_y = y + (size + ray_length) * np.sin(angle)
            ax.plot([start_x, end_x], [start_y, end_y], 'k-', linewidth=self.lw_main)
        
        # 笑脸
        eye1 = Circle((x-0.3*size, y+0.2*size), 0.1*size, fill=True, color='black')
        eye2 = Circle((x+0.3*size, y+0.2*size), 0.1*size, fill=True, color='black')
        ax.add_patch(eye1)
        ax.add_patch(eye2)
        
        mouth = Arc((x, y-0.2*size), 0.6*size, 0.4*size, angle=0, theta1=0, theta2=180, 
                   linewidth=self.lw_detail, color='black', fill=False)
        ax.add_patch(mouth)
    
    def draw_tree(self, ax, x=2, y=5, size=1):
        """绘制树木简笔画"""
        # 树干
        trunk = Rectangle((x-0.2*size, y-2*size), 0.4*size, 2*size, 
                         fill=False, edgecolor='black', linewidth=self.lw_main)
        ax.add_patch(trunk)
        
        # 树冠（三个圆形重叠）
        crown1 = Circle((x, y+1*size), 1*size, fill=False, edgecolor='black', linewidth=self.lw_main)
        crown2 = Circle((x-0.7*size, y+0.3*size), 0.8*size, fill=False, edgecolor='black', linewidth=self.lw_main)
        crown3 = Circle((x+0.7*size, y+0.3*size), 0.8*size, fill=False, edgecolor='black', linewidth=self.lw_main)
        ax.add_patch(crown1)
        ax.add_patch(crown2)
        ax.add_patch(crown3)
        
        # 苹果（减少数量）
        apple_positions = [
            (x-0.3*size, y+0.8*size),
            (x+0.4*size, y+1.0*size)
        ]
        for apple_x, apple_y in apple_positions:
            apple = Circle((apple_x, apple_y), 0.12*size, fill=False, edgecolor='black', linewidth=self.lw_detail)
            ax.add_patch(apple)
    
    def draw_butterfly(self, ax, x=7, y=10, size=0.5):
        """绘制蝴蝶简笔画"""
        # 身体
        ax.plot([x, x], [y-size, y+size], 'k-', linewidth=self.lw_main)
        
        # 触角
        ax.plot([x, x-0.2*size], [y+size, y+1.3*size], 'k-', linewidth=self.lw_detail)
        ax.plot([x, x+0.2*size], [y+size, y+1.3*size], 'k-', linewidth=self.lw_detail)
        
        # 触角末端
        ax.plot([x-0.2*size], [y+1.3*size], 'ko', markersize=4)
        ax.plot([x+0.2*size], [y+1.3*size], 'ko', markersize=4)
        
        # 翅膀
        wing1 = Ellipse((x-0.6*size, y+0.3*size), 0.8*size, 1.2*size, 
                       fill=False, edgecolor='black', linewidth=self.lw_main)
        wing2 = Ellipse((x+0.6*size, y+0.3*size), 0.8*size, 1.2*size, 
                       fill=False, edgecolor='black', linewidth=self.lw_main)
        wing3 = Ellipse((x-0.5*size, y-0.5*size), 0.6*size, 0.8*size, 
                       fill=False, edgecolor='black', linewidth=self.lw_main)
        wing4 = Ellipse((x+0.5*size, y-0.5*size), 0.6*size, 0.8*size, 
                       fill=False, edgecolor='black', linewidth=self.lw_main)
        
        ax.add_patch(wing1)
        ax.add_patch(wing2)
        ax.add_patch(wing3)
        ax.add_patch(wing4)
        
        # 翅膀装饰（减少数量）
        for wing_x in [x-0.6*size, x+0.6*size]:
            spot = Circle((wing_x, y+0.3*size), 0.1*size, fill=False, edgecolor='black', linewidth=self.lw_detail)
            ax.add_patch(spot)
    
    def add_grass(self, ax):
        """添加草地装饰"""
        grass_y = 2.5
        for x_pos in np.linspace(0.5, 9.5, 12):
            grass_height = random.uniform(0.2, 0.6)
            # 草的形状更自然
            grass_curve = random.uniform(-0.1, 0.1)
            ax.plot([x_pos, x_pos + grass_curve], [grass_y, grass_y + grass_height], 
                   'k-', linewidth=3)
    
    def add_clouds(self, ax):
        """添加云朵装饰"""
        cloud_positions = [(2.0, 11.7, 0.8), (6.0, 11.8, 0.7)]
        
        for cloud_x, cloud_y, cloud_size in cloud_positions:
            # 云朵由多个圆组成
            cloud_circles = [
                (cloud_x, cloud_y, cloud_size),
                (cloud_x + 0.7*cloud_size, cloud_y, 0.8*cloud_size),
                (cloud_x + 0.3*cloud_size, cloud_y + 0.3*cloud_size, 0.7*cloud_size)
            ]
            
            for cx, cy, cs in cloud_circles:
                cloud = Circle((cx, cy), cs, fill=False, edgecolor='black', linewidth=self.lw_detail)
                ax.add_patch(cloud)
                

    # ===== 新增：简约额外图案 =====
    def draw_boat(self, ax, x=5, y=6, size=1):
        """绘制小船（简化线条）"""
        hull = patches.Polygon([
            (x-1.2*size, y), (x+1.2*size, y), (x+0.8*size, y-0.5*size), (x-0.8*size, y-0.5*size)
        ], fill=False, edgecolor='black', linewidth=self.lw_main)
        ax.add_patch(hull)
        sail = patches.Polygon([
            (x, y), (x, y+1.4*size), (x+0.9*size, y)
        ], fill=False, edgecolor='black', linewidth=self.lw_main)
        ax.add_patch(sail)

    def draw_wave_line(self, ax, x1=0.5, x2=9.5, y=3.0):
        """绘制一条简化波浪线"""
        points_x = np.linspace(x1, x2, 8)
        points_y = y + 0.2*np.sin(np.linspace(0, 2*np.pi, 8))
        ax.plot(points_x, points_y, 'k-', linewidth=self.lw_detail)

    def draw_fish(self, ax, x=3, y=4, size=0.6):
        """绘制小鱼（极简）"""
        body = Ellipse((x, y), 1.0*size, 0.6*size, fill=False, edgecolor='black', linewidth=self.lw_main)
        ax.add_patch(body)
        tail = patches.Polygon([
            (x+0.5*size, y), (x+0.9*size, y+0.3*size), (x+0.9*size, y-0.3*size)
        ], fill=False, edgecolor='black', linewidth=self.lw_main)
        ax.add_patch(tail)

    def draw_rocket(self, ax, x=5, y=7, size=1):
        """绘制火箭（简化）"""
        body = Ellipse((x, y), 0.8*size, 2.0*size, fill=False, edgecolor='black', linewidth=self.lw_main)
        ax.add_patch(body)
        nose = patches.Polygon([
            (x-0.4*size, y+1.0*size), (x+0.4*size, y+1.0*size), (x, y+1.5*size)
        ], fill=False, edgecolor='black', linewidth=self.lw_main)
        ax.add_patch(nose)
        fin_left = patches.Polygon([
            (x-0.3*size, y-0.5*size), (x-0.9*size, y-1.0*size), (x-0.3*size, y-0.9*size)
        ], fill=False, edgecolor='black', linewidth=self.lw_main)
        fin_right = patches.Polygon([
            (x+0.3*size, y-0.5*size), (x+0.9*size, y-1.0*size), (x+0.3*size, y-0.9*size)
        ], fill=False, edgecolor='black', linewidth=self.lw_main)
        ax.add_patch(fin_left)
        ax.add_patch(fin_right)

    def draw_moon(self, ax, x=8, y=12, size=0.8):
        """绘制弯月（简化）"""
        outer = Circle((x, y), size, fill=False, edgecolor='black', linewidth=self.lw_main)
        inner = Circle((x+0.3*size, y+0.2*size), 0.8*size, fill=False, edgecolor='black', linewidth=self.lw_main)
        ax.add_patch(outer)
        ax.add_patch(inner)

    def draw_star(self, ax, x=6, y=11, size=0.6):
        """绘制五角星（极简折线）"""
        angles = np.linspace(0, 2*np.pi, 6)[:-1]
        pts = [(x + size*np.cos(a), y + size*np.sin(a)) for a in angles[::2]]
        star = patches.Polygon(pts, closed=True, fill=False, edgecolor='black', linewidth=self.lw_main)
        ax.add_patch(star)

    def draw_car(self, ax, x=5, y=5, size=1):
        """绘制小汽车（简化）"""
        body = Rectangle((x-1.5*size, y-0.3*size), 3.0*size, 0.8*size, fill=False, edgecolor='black', linewidth=self.lw_main)
        top = Rectangle((x-0.8*size, y+0.3*size), 1.6*size, 0.5*size, fill=False, edgecolor='black', linewidth=self.lw_main)
        ax.add_patch(body)
        ax.add_patch(top)
        wheel1 = Circle((x-0.8*size, y-0.3*size), 0.3*size, fill=False, edgecolor='black', linewidth=self.lw_main)
        wheel2 = Circle((x+0.8*size, y-0.3*size), 0.3*size, fill=False, edgecolor='black', linewidth=self.lw_main)
        ax.add_patch(wheel1)
        ax.add_patch(wheel2)

    def draw_road(self, ax, y=4):
        """绘制一条道路（简化）"""
        ax.plot([0.5, 9.5], [y, y], 'k-', linewidth=self.lw_main)

    def draw_signal(self, ax, x=8, y=5, size=1):
        """绘制简化红绿灯"""
        pole = Rectangle((x-0.05*size, y-1.2*size), 0.1*size, 1.2*size, fill=False, edgecolor='black', linewidth=self.lw_main)
        box = Rectangle((x-0.3*size, y-1.2*size), 0.6*size, 0.9*size, fill=False, edgecolor='black', linewidth=self.lw_main)
        ax.add_patch(pole)
        ax.add_patch(box)
        light = Circle((x, y-0.6*size), 0.12*size, fill=False, edgecolor='black', linewidth=self.lw_detail)
        ax.add_patch(light)

    # ===== 新增：水果与小动物 =====
    def draw_grapes(self, ax, x=5, y=8, size=1.0, rows=5):
        """绘制一串葡萄（圆形排列+叶子+果柄）"""
        # 葡萄主簇（六边形堆叠圆）
        radius = 0.45*size
        centers = []
        for r in range(rows):
            count = rows + 1 - r
            offset_x = - (count-1) * radius * 0.9 / 2.0
            cy = y - r * radius * 0.9
            for i in range(count):
                cx = x + offset_x + i * radius * 0.9
                centers.append((cx, cy))
        # 微调下尖角的葡萄
        centers.append((x, y - rows * radius * 0.95))
        for cx, cy in centers:
            ax.add_patch(Circle((cx, cy), radius, fill=False, edgecolor='black', linewidth=self.lw_main))

        # 果柄
        stem = Rectangle((x-0.25*size, y+0.6*size), 0.5*size, 0.8*size, fill=False, edgecolor='black', linewidth=self.lw_main)
        ax.add_patch(stem)
        # 叶子（简化橡树叶造型）
        leaf = patches.Polygon([
            (x+0.2*size, y+0.6*size), (x+1.2*size, y+1.2*size), (x+1.4*size, y+1.0*size),
            (x+1.1*size, y+0.7*size), (x+1.5*size, y+0.6*size), (x+1.2*size, y+0.4*size),
            (x+1.3*size, y+0.1*size), (x+0.9*size, y+0.2*size), (x+0.7*size, y+0.0*size),
            (x+0.5*size, y+0.4*size)
        ], fill=False, edgecolor='black', linewidth=self.lw_main)
        ax.add_patch(leaf)
        # 叶脉
        ax.plot([x+0.3*size, x+1.2*size], [y+0.5*size, y+0.9*size], 'k-', linewidth=self.lw_detail)
        ax.plot([x+0.8*size, x+0.9*size], [y+0.7*size, y+1.05*size], 'k-', linewidth=self.lw_detail)

    def draw_squirrel_simple(self, ax, x=5.5, y=7.2, size=1.0):
        """绘制简化版小松鼠抱松果（线条少、圆润）"""
        # 身体/头部
        head = Ellipse((x-0.8*size, y+0.2*size), 1.0*size, 0.9*size, fill=False, edgecolor='black', linewidth=self.lw_main)
        body = Ellipse((x, y-0.6*size), 1.7*size, 1.8*size, fill=False, edgecolor='black', linewidth=self.lw_main)
        ax.add_patch(head)
        ax.add_patch(body)
        # 耳朵
        ear1 = patches.Polygon([(x-1.2*size, y+0.7*size), (x-0.9*size, y+1.2*size), (x-0.6*size, y+0.7*size)], fill=False, edgecolor='black', linewidth=self.lw_main)
        ear2 = patches.Polygon([(x-0.9*size, y+0.6*size), (x-0.6*size, y+1.0*size), (x-0.3*size, y+0.6*size)], fill=False, edgecolor='black', linewidth=self.lw_main)
        ax.add_patch(ear1)
        ax.add_patch(ear2)
        # 眼睛/鼻子/嘴
        ax.add_patch(Circle((x-0.95*size, y+0.2*size), 0.08*size, fill=True, color='black'))
        ax.plot([x-0.8*size, x-0.7*size], [y-0.05*size, y-0.0*size], 'k-', linewidth=self.lw_detail)
        ax.plot([x-0.85*size, x-0.7*size], [y-0.2*size, y-0.2*size], 'k-', linewidth=self.lw_detail)
        # 手臂与松果
        arm = patches.Polygon([(x-0.3*size, y-0.2*size), (x-0.9*size, y-0.1*size), (x-1.1*size, y-0.3*size)], fill=False, edgecolor='black', linewidth=self.lw_main)
        ax.add_patch(arm)
        nut = Ellipse((x-1.25*size, y-0.35*size), 0.5*size, 0.6*size, fill=False, edgecolor='black', linewidth=self.lw_main)
        ax.add_patch(nut)
        # 松果纹理（极简网格）
        ax.plot([x-1.45*size, x-1.05*size], [y-0.35*size, y-0.35*size], 'k-', linewidth=self.lw_detail)
        ax.plot([x-1.25*size, x-1.25*size], [y-0.6*size, y-0.1*size], 'k-', linewidth=self.lw_detail)
        # 尾巴（大而卷）
        tail = patches.Polygon([
            (x+0.7*size, y+0.2*size), (x+1.4*size, y+1.2*size), (x+1.2*size, y+2.0*size),
            (x+0.6*size, y+1.7*size), (x+0.9*size, y+1.2*size), (x+0.4*size, y+0.7*size)
        ], fill=False, edgecolor='black', linewidth=self.lw_main)
        ax.add_patch(tail)
        # 腿/脚底
        paw_l = Ellipse((x-0.3*size, y-1.4*size), 0.6*size, 0.25*size, fill=False, edgecolor='black', linewidth=self.lw_main)
        paw_r = Ellipse((x+0.5*size, y-1.4*size), 0.6*size, 0.25*size, fill=False, edgecolor='black', linewidth=self.lw_main)
        ax.add_patch(paw_l)
        ax.add_patch(paw_r)
        # 地面草线（极简）
        ax.plot([x-1.6*size, x-1.2*size, x-0.8*size], [y-1.55*size, y-1.45*size, y-1.55*size], 'k-', linewidth=self.lw_detail)
    
    def generate_scene(self, scene_type="mixed"):
        """生成完整的填色场景"""
        fig, ax = self.create_figure()
        # 添加柔和圆角边框
        self.draw_frame(ax)
        
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

        elif scene_type == "fruits_grapes":
            # 水果-葡萄主题
            self.draw_grapes(ax, x=5, y=9, size=1.2, rows=5)
            self.add_grass(ax)
            
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

        elif scene_type == "ocean":
            # 海洋主题（简约）
            self.draw_boat(ax, x=6, y=6, size=1.2)
            self.draw_fish(ax, x=3, y=4, size=0.7)
            self.draw_wave_line(ax, x1=0.8, x2=9.2, y=3.2)
            self.draw_wave_line(ax, x1=1.0, x2=8.8, y=2.8)

        elif scene_type == "space":
            # 太空主题（简约）
            self.draw_rocket(ax, x=4.5, y=7.5, size=1.2)
            self.draw_star(ax, x=7.5, y=11.5, size=0.7)
            self.draw_moon(ax, x=8.5, y=12.0, size=0.8)

        elif scene_type == "transport":
            # 交通主题（简约）
            self.draw_road(ax, y=4)
            self.draw_car(ax, x=5.5, y=4.3, size=1.0)
            self.draw_signal(ax, x=8.2, y=5.0, size=1.0)

        elif scene_type == "squirrel":
            # 小松鼠主题
            self.draw_squirrel_simple(ax, x=5.5, y=7.2, size=1.0)
            
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
        "ocean": "海洋冒险主题",
        "space": "太空探索主题",
        "transport": "交通小车主题",
        "fruits_grapes": "水果-葡萄主题",
        "squirrel": "小松鼠主题",
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