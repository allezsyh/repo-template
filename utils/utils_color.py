"""
日期： 2025.2.12
作者： Harvey Shi
功能： 一些用于生成随机颜色的函数。
1. `_random_green()`：生成随机绿色的十六进制颜色代码，红色和蓝色分量为0，绿色分量在100到255之间随机选择。
2. `_random_red()`：生成随机红色的十六进制颜色代码，绿色和蓝色分量为0，红色分量在100到255之间随机选择。
3. `_random_blue()`：生成随机蓝色的十六进制颜色代码，红色和绿色分量为0，蓝色分量在100到255之间随机选择。
4. `_random_yellow()`：生成随机黄色的十六进制颜色代码，红色和绿色分量较高，蓝色分量较低，生成的颜色呈现黄色调。
5. `_random_dark()`：生成随机深色的十六进制颜色代码，红色、绿色和蓝色分量较低，生成的颜色较暗。
6. `generate_random_color()`：生成一个完全随机的十六进制颜色代码，所有RGB分量均在0到255之间随机选择。

这些函数可以帮助您轻松生成各种颜色，并以十六进制的形式返回，以便在前端开发或图形处理中使用。
"""
import random


def _random_green():
    """
    生成随机颜色的函数
    """
    g = random.randint(100, 255)
    return "#{:02x}{:02x}{:02x}".format(0, g, 0)  # 将 RGB 转换为十六进制颜色值

def _random_red():
    """
    生成随机颜色的函数
    """
    r = random.randint(100, 255)
    return "#{:02x}{:02x}{:02x}".format(r, 0, 0)  # 将 RGB 转换为十六进制颜色值

def _random_blue():
    """
    生成随机颜色的函数
    """
    b = random.randint(100, 255)
    return "#{:02x}{:02x}{:02x}".format(0, 0, b)  # 将 RGB 转换为十六进制颜色值


def _random_yellow():
    """
    生成随机黄色颜色的函数
    """
    r = random.randint(200, 255)  # 高红色分量
    g = random.randint(200, 255)  # 高绿色分量
    b = random.randint(0, 100)    # 低蓝色分量
    return "#{:02x}{:02x}{:02x}".format(r, g, b)  # 将 RGB 转换为十六进制颜色值

def _random_dark():
    """
    生成随机深色颜色的函数
    """
    r = random.randint(0, 100)    # 低红色分量
    g = random.randint(0, 100)    # 低绿色分量
    b = random.randint(0, 100)    # 低蓝色分量
    return "#{:02x}{:02x}{:02x}".format(r, g, b)  # 将 RGB 转换为十六进制颜色值

def generate_random_color():
    """
    生成随机颜色代码
    """
    color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
    return color