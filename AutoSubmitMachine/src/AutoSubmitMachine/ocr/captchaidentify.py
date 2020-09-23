#oding = utf-8
# -*- coding:utf-8 -*-
#https://github.com/tesseract-ocr
import sys
import os

from PIL import Image, ImageDraw, ImageFilter
from pyocr import pyocr
#二值判断,如果确认是噪声,用改点的上面一个点的灰度进行替换
#该函数也可以改成RGB判断的,具体看需求如何
def getPixel(image,x,y,G,N):
    L = image.getpixel((x,y))
    if L > G:
        L = True
    else:
        L = False

    nearDots = 0
    if L == (image.getpixel((x - 1,y - 1)) > G):
        nearDots += 1
    if L == (image.getpixel((x - 1,y)) > G):
        nearDots += 1
    if L == (image.getpixel((x - 1,y + 1)) > G):
        nearDots += 1
    if L == (image.getpixel((x,y - 1)) > G):
        nearDots += 1
    if L == (image.getpixel((x,y + 1)) > G):
        nearDots += 1
    if L == (image.getpixel((x + 1,y - 1)) > G):
        nearDots += 1
    if L == (image.getpixel((x + 1,y)) > G):
        nearDots += 1
    if L == (image.getpixel((x + 1,y + 1)) > G):
        nearDots += 1

    if nearDots < N:
        return image.getpixel((x,y-1))
    else:
        return None

# 降噪
# 根据一个点A的RGB值，与周围的8个点的RBG值比较，设定一个值N（0 <N <8），当A的RGB值与周围8个点的RGB相等数小于N时，此点为噪点
# G: Integer 图像二值化阀值
# N: Integer 降噪率 0 <N <8
# Z: Integer 降噪次数
# 输出
#  0：降噪成功
#  1：降噪失败
def clearNoise(image,G,N,Z):
    draw = ImageDraw.Draw(image)
    for i in xrange(0,Z):
        for x in xrange(1,image.size[0] - 1):
            for y in xrange(1,image.size[1] - 1):
                color = getPixel(image,x,y,G,N)
                if color != None:
                    draw.point((x,y),color)

def prepare_image(img):
    """Transform image to greyscale and blur it"""
    img = img.filter(ImageFilter.SMOOTH_MORE)
    img = img.filter(ImageFilter.SMOOTH_MORE)
    if 'L' != img.mode:
        img = img.convert('L')
    return img

def remove_noise(img, pass_factor):
    for column in range(img.size[0]):
        for line in range(img.size[1]):
            value = remove_noise_by_pixel(img, column, line, pass_factor)
            img.putpixel((column, line), value)
    return img

def remove_noise_by_pixel(img, column, line, pass_factor):
    if img.getpixel((column, line)) < pass_factor:
        return (0)
    return (255)

#测试代码
def main():
    image = Image.open("d:/validate_code.png")
    #将图片转换成灰度图片
    image = image.convert("L")
    # #去噪,G = 50,N = 4,Z = 4
    #clearNoise(image,50,4,4)
    # #保存图片
    image.save("d:/result.png")
    tools = pyocr.get_available_tools()[:]
    if len(tools) == 0:
        print("No OCR tool found")
        sys.exit(1)
    print("Using '%s'" % (tools[0].get_name()))
    print(tools[0].get_version())
    print("Using '%s'" % (tools[0].get_available_languages()))
    print(tools[0].image_to_string(Image.open('d:/result.png'), lang='eng'))
    #print tools[0].image_to_string(Image.open('D:/234.png'),lang='chi_sim')

if __name__ == '__main__':
    main()




