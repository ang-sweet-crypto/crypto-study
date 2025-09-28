import tkinter as tk
from tkinter import ttk, messagebox
import random
import time
from PIL import Image, ImageTk
import os
import math
import urllib.request
from io import BytesIO


class GenshinTrueCharacterLottery:
    def __init__(self, root):
        self.root = root
        self.root.title("原神英雄抽签")
        self.root.geometry("1000x700")
        self.root.resizable(True, True)
        self.root.configure(bg="#0a0e17")

        # 确保中文字体正常显示
        self.font_family = "Microsoft YaHei"

        # 原神风格颜色配置
        self.colors = {
            "bg": "#0a0e17",  # 深色背景
            "card_back": "#c89b3c",  # 卡片背面金色
            "card_front": "#1e293b",  # 卡片正面深色
            "text": "#f0e6d2",  # 文本颜色
            "accent": "#fbbf24",  # 金色强调
            "border": "#475569",  # 边框颜色
            "five_star": "#ffd700",  # 五星金色
            "four_star": "#9370db"  # 四星紫色
        }

        # 名字与原神角色图片对应（使用原神角色图片）
        self.name_data = {
            "喻悦": {"name":"七七", "url": "https://mmbiz.qpic.cn/mmbiz_png/P6EPC2coAe3uW9icfBkCqN5vfZKFLIqpIjazdrByzXbDModSxKLt6zI7obzY8NQlBINJx0mtsYVIfITpW42v3iaA/640?wx_fmt=png&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=0", "star": 5},
            "贺苹": {"name": "迪卢克", "url": "https://mmbiz.qpic.cn/mmbiz_png/P6EPC2coAe3uW9icfBkCqN5vfZKFLIqpIu00jyOwGPddHNmjbXHSvibFyy7WibpoibSJN252ssQnV4hhTHaKJzKh6g/640?wx_fmt=png&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=1", "star": 5},
            "杨甜": {"name": "刻晴", "url": "https://mmbiz.qpic.cn/mmbiz_png/P6EPC2coAe3uW9icfBkCqN5vfZKFLIqpI9XEBNiaX4Ilibmy8ic4GbkAsnDM2JJfWPY33RX5gJgHhUFibIWhqZJus0g/640?wx_fmt=png&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=2", "star": 5},
            "彭鑫雨": {"name": "荧", "url": "https://mmbiz.qpic.cn/mmbiz_png/P6EPC2coAe3uW9icfBkCqN5vfZKFLIqpIQ4pLt7QMO6BQfmlHicX0p4yyibicOvvRsHqEo3BveDGliaiawKG7cxbqsDw/640?wx_fmt=png&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=3", "star": 5},
            "刘鲛": {"name": "莫娜", "url": "https://mmbiz.qpic.cn/mmbiz_png/P6EPC2coAe3uW9icfBkCqN5vfZKFLIqpIQgdKialdwUxhvAnSXPI8licj35s31UMibPGFe6tH3nicJcOpnriccpCcsMQ/640?wx_fmt=png&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=4", "star": 5},
            "孙雯雯": {"name": "温迪", "url": "https://mmbiz.qpic.cn/mmbiz_png/P6EPC2coAe3uW9icfBkCqN5vfZKFLIqpImW6FlHnuSJZcicaNicLRh0ib31Jhk31F5OicSc1OBPw2RE4m9rQV24iamgg/640?wx_fmt=png", "star": 5},
            "何柳月": {"name": "可莉", "url": "https://mmbiz.qpic.cn/mmbiz_png/P6EPC2coAe3uW9icfBkCqN5vfZKFLIqpImH13YrUMzutU7y37d6E7w9I2xicpZf3ZHjy8Lg8mp4PCBE95KI0Ogcg/640?wx_fmt=png", "star": 5},
            "戴瑶": {"name": "魈", "url": "https://mmbiz.qpic.cn/mmbiz_png/P6EPC2coAe3uW9icfBkCqN5vfZKFLIqpI5DoWZBN2iaB1UibgT5ukpMpGcar7x1rELlqBmkzRMNaL5X2ibaWBhiaq4w/640?wx_fmt=png", "star": 5},
            "任舒阳": {"name": "林尼", "url": "https://mmbiz.qpic.cn/mmbiz_png/P6EPC2coAe3uW9icfBkCqN5vfZKFLIqpIP4mj3jxDdyedGvSktX7HEfn7J3XKbeB5ickibt0yxRTP7QAG3bDRQZyQ/640?wx_fmt=png", "star": 4},
            "许钰涵": {"name": "那维莱特", "url": "https://mmbiz.qpic.cn/mmbiz_png/P6EPC2coAe3uW9icfBkCqN5vfZKFLIqpIuWjSmMvOtvm9lPMeuXYjkHm8TuG36GBB6s9Od8bms0fFUIvym03NKQ/640?wx_fmt=png", "star": 4},
            "李铭语": {"name": "赛诺", "url": "https://mmbiz.qpic.cn/mmbiz_png/P6EPC2coAe3uW9icfBkCqN5vfZKFLIqpIw9C8JE51lPibzDqhGN0GOVIzEeJFcY6NzMHJ4Ks5VXojf3LrEKzSneg/640?wx_fmt=png", "star": 4},
            "杨宣嘉": {"name": "神里绫华", "url": "https://mmbiz.qpic.cn/mmbiz_png/P6EPC2coAe3uW9icfBkCqN5vfZKFLIqpIsoU3Nm2eBpxR77m8RKpURQLMwodlsSJnNC08ic0W4RrUFORqyeo3ibyA/640?wx_fmt=png", "star": 4},
            "黄先慷": {"name": "达达利亚", "url": "https://mmbiz.qpic.cn/mmbiz_png/P6EPC2coAe3uW9icfBkCqN5vfZKFLIqpIJ0xOibliacZSPVhJrzlebb0dvDic8jnqHauEUBVSJScialVxicJu14gS7qA/640?wx_fmt=png", "star": 4},
            "彭泽楠": {"name": "钟离", "url": "https://mmbiz.qpic.cn/mmbiz_png/P6EPC2coAe3uW9icfBkCqN5vfZKFLIqpIkuk8PWENy3Ku8De3IpvCyqrEsyJBTQ9sH4cIqkA8S7JGS3icasGYjIA/640?wx_fmt=png", "star": 4},
            "石承鑫": {"name": "空", "url": "https://mmbiz.qpic.cn/mmbiz_png/P6EPC2coAe3uW9icfBkCqN5vfZKFLIqpIu7MUJ2obibtQTVBNLSlHTDSUmlxJGs6joj3ToAPJ67x3CjoOr1UXStQ/640?wx_fmt=png", "star": 4},
            "林佳星": {"name": "纳西妲", "url": "https://mmbiz.qpic.cn/mmbiz_png/P6EPC2coAe3uW9icfBkCqN5vfZKFLIqpImTNeabdmBxATf7frrEfgy6kc0GV0rIsVO9iaVLpNFPSwO3wSaicO2zYw/640?wx_fmt=png", "star": 4},
            "佘金友": {"name": "甘雨", "url": "https://mmbiz.qpic.cn/mmbiz_png/P6EPC2coAe3uW9icfBkCqN5vfZKFLIqpINo02LTp63bBzzWIzhCZnIG8XLgKkfSgWoZMV6prlNM7TvRkgDThayw/640?wx_fmt=png", "star": 4},
            "罗一航": {"name": "妮露", "url": "https://mmbiz.qpic.cn/mmbiz_png/P6EPC2coAe3uW9icfBkCqN5vfZKFLIqpIg4lSbdqTBb0yib91OnG6OY4zACNaia4oxt7V0ombt6kRTtxLK0qZHcAA/640?wx_fmt=png", "star": 4},
            "张浩": {"name": "枫原万叶", "url": "https://mmbiz.qpic.cn/mmbiz_png/P6EPC2coAe3uW9icfBkCqN5vfZKFLIqpICMic1xrl5iayiakyar5ZEpYEf7e7hqQsnYvwKQp7uE9kKeKdLYcqAibPicA/640?wx_fmt=png", "star": 4},
            "刘文滔": {"name": "胡桃", "url": "https://mmbiz.qpic.cn/mmbiz_png/P6EPC2coAe3uW9icfBkCqN5vfZKFLIqpI6iaL91J2tib8wr3LTqWxVsFKhibGTfsj4nmTicsqb0EuibFIQwOx1iaa8Mibg/640?wx_fmt=png", "star": 4},
            "罗宇昊": {"name": "派蒙", "url": "https://mmbiz.qpic.cn/mmbiz_png/P6EPC2coAe3uW9icfBkCqN5vfZKFLIqpIyLm7QKMFQKHevbB2aQRNM9CP0mibnNs6IibpHy2ibUqOGicN35fOJkKl4w/640?wx_fmt=png&from=appmsg", "star": 4},
            "张培瑞": {"name": "雷电将军", "url": "https://mmbiz.qpic.cn/mmbiz_png/P6EPC2coAe3uW9icfBkCqN5vfZKFLIqpImqaj6kH1xUBoWyo5v80iaSrZfdjYXibG6j7GPNoC26DA5SctuicDTof9g/640?wx_fmt=png", "star": 4},
            "张俊轩": {"name": "散兵", "url": "https://mmbiz.qpic.cn/mmbiz_png/P6EPC2coAe3uW9icfBkCqN5vfZKFLIqpIAPeXDQ5k5SfvmOMaYKfQvKuWoxSicakETUXNlf8kdmsIyyFyiawPMR7Q/640?wx_fmt=png", "star": 4},
            "杨印正": {"name": "宵宫", "url": "https://mmbiz.qpic.cn/mmbiz_png/P6EPC2coAe3uW9icfBkCqN5vfZKFLIqpIz44zdn1UmWFKp38H53mbv7R9RvG1Lx8y2hsee24C8X6vdVFiaicBg5DA/640?wx_fmt=png", "star": 4},
            "张子杰": {"name": "芙宁娜", "url": "https://mmbiz.qpic.cn/mmbiz_png/P6EPC2coAe3uW9icfBkCqN5vfZKFLIqpIeCDrMLicHIdhUSDm6SJaa0roEoialC1QO9YGItjLy1wiahyU1QU12qJJw/640?wx_fmt=png", "star": 4},
            "王凡": {"name": "迪希亚", "url": "https://mmbiz.qpic.cn/mmbiz_png/P6EPC2coAe3uW9icfBkCqN5vfZKFLIqpIViaQe6N4g6icJmuicRWxfH0D20knvv9ica99Lf4N0NtWrjXaibZQI4uQTiaQ/640?wx_fmt=png", "star": 4},
            "裴勇昊": {"name": "八重神子", "url": "https://mmbiz.qpic.cn/mmbiz_png/P6EPC2coAe3uW9icfBkCqN5vfZKFLIqpIHyebtoTUwXWxKOsbjmMdHDFPPjjia9qN8VP2FNBpkT78FAtiaZIKcIMQ/640?wx_fmt=png", "star": 4},
            "李鸿鹏": {"name": "艾尔海森", "url": "https://mmbiz.qpic.cn/mmbiz_png/P6EPC2coAe3uW9icfBkCqN5vfZKFLIqpIMf5N160XTeuYC1aL7wQjBWLZDcpttxTWJq6uBvO6qIibCxFAibpTthIA/640?wx_fmt=png", "star": 4},
            "朱泓屹": {"name": "夜兰", "url": "https://mmbiz.qpic.cn/mmbiz_png/P6EPC2coAe3uW9icfBkCqN5vfZKFLIqpI0pQx8Mz0Fszw0LqE2yN4BFnSvCWMoj4q5f4UnXBH95xlkbr0zvUWXg/640?wx_fmt=png", "star": 4},
            "范宇轩": {"name": "申鹤", "url": "https://mmbiz.qpic.cn/mmbiz_png/P6EPC2coAe3uW9icfBkCqN5vfZKFLIqpIllezibztIKlA8xf1VdUpI8Ds4LeJACyboqqeeKOIdvITjG94QmkID2Q/640?wx_fmt=png", "star": 4},
            "郝禹铭": {"name": "荒泷一斗", "url": "https://mmbiz.qpic.cn/mmbiz_png/P6EPC2coAe3uW9icfBkCqN5vfZKFLIqpIGUyxdd0exnMJiaztpor5sZhktjAlgrDiaxSkJkQasuzCYXY1cUBJX8xw/640?wx_fmt=png", "star": 4},
            "黄米": {"name": "神里绫人", "url": "https://mmbiz.qpic.cn/mmbiz_png/P6EPC2coAe3uW9icfBkCqN5vfZKFLIqpIjyaLJ2oz61eJ04ttHr96ZRmDkB1UGhC2D2MX9KawooUqIOZb27ZXgQ/640?wx_fmt=png", "star": 4},
            "廖元浩": {"name": "珊瑚宫心海", "url": "https://mmbiz.qpic.cn/mmbiz_png/P6EPC2coAe3uW9icfBkCqN5vfZKFLIqpI1ibicaABibiaoeP4ic7h2GhupibDNw294I2mcMJ0rgj57OA1Yc8XQ69D0Ylg/640?wx_fmt=png", "star": 4}
        }

        # 存储已加载的图片
        self.images = {}

        # 创建界面
        self.create_widgets()

        # 动画相关变量
        self.animation_running = False

    def load_image(self, name):
        """加载指定名字对应的原神角色图片"""
        if name in self.images:
            return self.images[name]

        try:
            # 获取图片URL
            url = self.name_data[name]["url"]

            # 从网络加载图片
            with urllib.request.urlopen(url) as u:
                raw_data = u.read()

            # 处理图片
            img = Image.open(BytesIO(raw_data))
            img = img.resize((200, 200), Image.LANCZOS)
            photo = ImageTk.PhotoImage(img)
            self.images[name] = photo
            return photo
        except Exception as e:
            print(f"图片加载失败: {e}")
            # 创建默认原神风格图片
            img = Image.new('RGB', (200, 200), color=self.colors["border"])
            # 添加原神元素
            draw = ImageDraw.Draw(img)
            draw.text((100, 100), "原神", fill=self.colors["accent"], anchor="mm")
            photo = ImageTk.PhotoImage(img)
            self.images[name] = photo
            return photo

    def create_widgets(self):
        """创建界面组件"""
        # 顶部标题
        header_frame = tk.Frame(self.root, bg=self.colors["bg"])
        header_frame.pack(fill=tk.X, padx=30, pady=20)

        tk.Label(
            header_frame,
            text="原神英雄抽签",
            font=(self.font_family, 28, "bold"),
            fg=self.colors["accent"],
            bg=self.colors["bg"]
        ).pack(pady=10)

        # 控制区域
        control_frame = tk.Frame(self.root, bg=self.colors["bg"])
        control_frame.pack(fill=tk.X, padx=30, pady=10)

        tk.Label(
            control_frame,
            text="抽取数量:",
            font=(self.font_family, 12),
            fg=self.colors["text"],
            bg=self.colors["bg"]
        ).pack(side=tk.LEFT, padx=(0, 10))

        self.count_var = tk.StringVar(value="35")
        count_entry = tk.Entry(
            control_frame,
            textvariable=self.count_var,
            width=5,
            font=(self.font_family, 12),
            bg=self.colors["card_front"],
            fg=self.colors["text"],
            insertbackground=self.colors["text"]
        )
        count_entry.pack(side=tk.LEFT, padx=(0, 20))

        draw_button = tk.Button(
            control_frame,
            text="开始抽签",
            command=self.start_drawing,
            font=(self.font_family, 12, "bold"),
            bg=self.colors["accent"],
            fg="#000000",
            activebackground="#d97706",
            padx=20,
            pady=5
        )
        draw_button.pack(side=tk.LEFT, padx=(0, 15))

        clear_button = tk.Button(
            control_frame,
            text="清空结果",
            command=self.clear_results,
            font=(self.font_family, 12),
            bg="#334155",
            fg=self.colors["text"],
            activebackground="#475569",
            padx=20,
            pady=5
        )
        clear_button.pack(side=tk.LEFT)

        # 卡片展示区域（中央大卡片）
        self.card_frame = tk.Frame(
            self.root,
            bg=self.colors["bg"],
            width=300,
            height=400
        )
        self.card_frame.pack(pady=20)
        self.card_frame.pack_propagate(False)

        # 创建卡片画布
        self.card_canvas = tk.Canvas(
            self.card_frame,
            width=280,
            height=380,
            bg=self.colors["bg"],
            highlightthickness=0
        )
        self.card_canvas.pack()

        # 结果列表区域
        result_frame = tk.Frame(self.root, bg=self.colors["bg"])
        result_frame.pack(fill=tk.BOTH, expand=True, padx=30, pady=10)

        # 滚动条
        scrollbar = ttk.Scrollbar(result_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # 结果画布
        self.result_canvas = tk.Canvas(
            result_frame,
            bg=self.colors["card_front"],
            bd=0,
            highlightthickness=0,
            yscrollcommand=scrollbar.set
        )
        self.result_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar.config(command=self.result_canvas.yview)

        # 结果框架
        self.results_frame = tk.Frame(self.result_canvas, bg=self.colors["card_front"])
        self.results_frame_id = self.result_canvas.create_window(
            (0, 0),
            window=self.results_frame,
            anchor="nw"
        )

        # 绑定事件
        self.results_frame.bind("<Configure>", self.on_frame_configure)
        self.result_canvas.bind("<Configure>", self.on_canvas_configure)

        # 初始提示
        self.initial_label = tk.Label(
            self.results_frame,
            text="点击「开始抽签」按钮进行抽取",
            font=(self.font_family, 14),
            fg=self.colors["text"],
            bg=self.colors["card_front"],
            pady=50
        )
        self.initial_label.pack()

        # 状态条
        self.status_var = tk.StringVar(value="等待开始...")
        status_frame = tk.Frame(self.root, height=30, bg=self.colors["bg"])
        status_frame.pack(fill=tk.X, side=tk.BOTTOM, pady=10)
        status_frame.pack_propagate(False)

        tk.Label(
            status_frame,
            textvariable=self.status_var,
            font=(self.font_family, 12),
            fg=self.colors["text"],
            bg=self.colors["bg"]
        ).pack(side=tk.LEFT, padx=30)

    def on_frame_configure(self, event):
        """更新滚动区域"""
        self.result_canvas.configure(scrollregion=self.result_canvas.bbox("all"))

    def on_canvas_configure(self, event):
        """调整画布大小"""
        self.result_canvas.itemconfig(self.results_frame_id, width=event.width)

    def draw_name(self):
        """随机抽取一个名字"""
        names = list(self.name_data.keys())
        return random.choice(names)

    def start_drawing(self):
        """开始抽签流程"""
        if self.animation_running:
            return

        # 清除初始提示
        if hasattr(self, 'initial_label') and self.initial_label.winfo_exists():
            self.initial_label.destroy()

        # 验证输入
        try:
            count = int(self.count_var.get())
            if not (1 <= count <= 100):
                messagebox.showerror("错误", "请输入1-100之间的数字")
                return
        except ValueError:
            messagebox.showerror("错误", "请输入有效数字")
            return

        # 开始抽取
        self.animation_running = True
        self.draw_multiple(count)

    def draw_multiple(self, count, index=1):
        """批量抽取名字，逐个显示"""
        if index > count:
            self.animation_running = False
            # 统计五星数量
            five_star_count = sum(1 for widget in self.results_frame.winfo_children()
                                  if hasattr(widget, 'star_rating') and widget.star_rating == 5)
            self.status_var.set(f"抽签完成！共抽取了 {count} 个角色，其中 {five_star_count} 个五星角色")
            return

        self.status_var.set(f"正在抽取第 {index}/{count} 个角色...")
        self.root.update()

        # 抽取名字
        name = self.draw_name()

        # 显示卡片动画
        self.show_card_animation(name, index, count)

    def show_card_animation(self, name, current_index, total_count):
        """显示卡片翻转动画"""
        # 清除当前卡片
        self.card_canvas.delete("all")

        # 获取角色信息
        char_info = self.name_data[name]
        star = char_info["star"]
        border_color = self.colors["five_star"] if star == 5 else self.colors["four_star"]

        # 创建卡片背面（原神风格）
        back_card = self.card_canvas.create_rectangle(
            10, 10, 270, 370,
            fill=self.colors["card_back"],
            outline=border_color,
            width=3
        )

        # 卡片背面装饰（原神标志风格）
        self.card_canvas.create_text(
            140, 150,
            text="原神",
            font=(self.font_family, 36, "bold"),
            fill="#ffffff"
        )
        self.card_canvas.create_text(
            140, 230,
            text="★" * star,
            font=(self.font_family, 48, "bold"),
            fill=border_color
        )

        # 开始翻转动画
        self.flip_card(0, name, char_info, current_index, total_count)

    def flip_card(self, angle, name, char_info, current_index, total_count):
        """卡片翻转动画"""
        if angle < 180:
            # 计算缩放比例（模拟3D翻转）
            scale = abs(math.cos(math.radians(angle)))

            # 清除当前绘制
            self.card_canvas.delete("all")

            star = char_info["star"]
            border_color = self.colors["five_star"] if star == 5 else self.colors["four_star"]

            if angle < 90:
                # 显示背面
                self.card_canvas.create_rectangle(
                    140 - 130 * scale, 10,
                    140 + 130 * scale, 370,
                    fill=self.colors["card_back"],
                    outline=border_color,
                    width=3
                )
                self.card_canvas.create_text(
                    140, 150,
                    text="原神",
                    font=(self.font_family, int(36 * scale), "bold"),
                    fill="#ffffff"
                )
                self.card_canvas.create_text(
                    140, 230,
                    text="★" * star,
                    font=(self.font_family, int(48 * scale), "bold"),
                    fill=border_color
                )
            else:
                # 显示正面（开始显示名字）
                self.card_canvas.create_rectangle(
                    140 - 130 * scale, 10,
                    140 + 130 * scale, 370,
                    fill=self.colors["card_front"],
                    outline=border_color,
                    width=3
                )

                # 绘制名字（根据角度调整大小）
                self.card_canvas.create_text(
                    140, 320,
                    text=f"{name} ({char_info['name']})",
                    font=(self.font_family, int(18 * scale), "bold"),
                    fill=border_color
                )

            # 继续动画
            self.root.after(20, self.flip_card, angle + 5, name, char_info, current_index, total_count)
        else:
            # 动画结束，显示完整卡片
            self.show_card_front(name, char_info)

            # 短暂停留后添加到结果列表
            self.root.after(1000, self.add_to_results, name, char_info, current_index, total_count)

    def show_card_front(self, name, char_info):
        """显示卡片正面，包含名字和原神角色图片"""
        self.card_canvas.delete("all")

        # 卡片边框颜色根据星级变化
        star = char_info["star"]
        border_color = self.colors["five_star"] if star == 5 else self.colors["four_star"]

        # 卡片正面
        self.card_canvas.create_rectangle(
            10, 10, 270, 370,
            fill=self.colors["card_front"],
            outline=border_color,
            width=3
        )

        # 加载并显示原神角色图片
        img = self.load_image(name)
        if img:
            self.card_canvas.create_image(140, 180, image=img)
            # 保持引用防止图片被垃圾回收
            self.card_canvas.image = img

        # 显示星级
        self.card_canvas.create_text(
            140, 30,
            text="★" * star,
            font=(self.font_family, 20),
            fill=border_color
        )

        # 显示名字和对应的原神角色名
        self.card_canvas.create_text(
            140, 320,
            text=name,
            font=(self.font_family, 24, "bold"),
            fill=self.colors["accent"]
        )

        self.card_canvas.create_text(
            140, 350,
            text=f"({char_info['name']})",
            font=(self.font_family, 14),
            fill=self.colors["text"]
        )

    def add_to_results(self, name, char_info, current_index, total_count):
        """将抽取的名字和对应的原神角色添加到结果列表"""
        # 卡片边框颜色根据星级变化
        star = char_info["star"]
        border_color = self.colors["five_star"] if star == 5 else self.colors["four_star"]

        # 创建结果项
        result_item = tk.Frame(
            self.results_frame,
            bg=self.colors["card_front"],
            highlightbackground=border_color,
            highlightthickness=2
        )
        result_item.pack(fill=tk.X, padx=10, pady=5)
        result_item.star_rating = star  # 存储星级信息

        # 序号
        tk.Label(
            result_item,
            text=f"#{current_index}",
            font=(self.font_family, 10),
            fg=self.colors["accent"],
            bg=self.colors["card_front"],
            width=5
        ).pack(side=tk.LEFT, padx=5)

        # 星级
        tk.Label(
            result_item,
            text="★" * star,
            font=(self.font_family, 10),
            fg=border_color,
            bg=self.colors["card_front"],
            width=5
        ).pack(side=tk.LEFT, padx=5)

        # 名字和原神角色名
        name_frame = tk.Frame(result_item, bg=self.colors["card_front"])
        name_frame.pack(side=tk.LEFT, padx=10)

        tk.Label(
            name_frame,
            text=name,
            font=(self.font_family, 12, "bold"),
            fg=self.colors["text"],
            bg=self.colors["card_front"],
            anchor="w",
            justify="left"
        ).pack(anchor="w")

        tk.Label(
            name_frame,
            text=f"({char_info['name']})",
            font=(self.font_family, 10),
            fg=self.colors["accent"],
            bg=self.colors["card_front"],
            anchor="w",
            justify="left"
        ).pack(anchor="w")

        # 缩略图
        img = self.load_image(name)
        if img:
            thumb_label = tk.Label(
                result_item,
                image=img,
                bg=self.colors["card_front"],
                width=50,
                height=50
            )
            thumb_label.pack(side=tk.RIGHT, padx=10)
            thumb_label.image = img  # 保持引用

        # 更新滚动区域并滚动到底部
        self.results_frame.update_idletasks()
        self.result_canvas.configure(scrollregion=self.result_canvas.bbox("all"))
        self.result_canvas.yview_moveto(1.0)

        # 继续下一个抽取
        self.draw_multiple(total_count, current_index + 1)

    def clear_results(self):
        """清空结果列表"""
        if self.animation_running:
            return

        # 清除结果
        for widget in self.results_frame.winfo_children():
            widget.destroy()

        # 清除卡片显示
        self.card_canvas.delete("all")

        # 恢复初始提示
        self.initial_label = tk.Label(
            self.results_frame,
            text="点击「开始抽签」按钮进行抽取",
            font=(self.font_family, 14),
            fg=self.colors["text"],
            bg=self.colors["card_front"],
            pady=50
        )
        self.initial_label.pack()

        self.status_var.set("等待开始...")
        self.result_canvas.configure(scrollregion=self.result_canvas.bbox("all"))


# 为了处理图片绘制（在load_image方法中使用）
from PIL import ImageDraw

if __name__ == "__main__":
    root = tk.Tk()
    app = GenshinTrueCharacterLottery(root)
    root.mainloop()
