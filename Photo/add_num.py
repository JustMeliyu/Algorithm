# -*- coding: utf-8 -*- 
"""
Describe:
https://www.liaoxuefeng.com/wiki/897692888725344/966759628285152
http://effbot.org/imagingbook/
"""

__author__ = "Road36"
__date__ = "19-6-14"

import random
from PIL import Image, ImageDraw, ImageFont, ImageFilter


class PhotoProcess:
    FONT_PATH = "../Resources/font/"
    PICTURE_PATH = "../Resources/picture/"

    def __init__(self, addr):
        self._resource = addr
        # self.image = Image.open(addr)

    @classmethod
    def rndChar(cls):
        # 随即字母
        return chr(random.randint(65, 90))

    @classmethod
    def rndColor(cls):
        # 随机颜色
        return random.randint(64, 255), random.randint(64, 255), random.randint(64, 255)

    @classmethod
    def rndColor2(cls):
        # 随机颜色2
        return random.randint(32, 127), random.randint(32, 127), random.randint(32, 127)

    def generate_verification_code(self, font, name):
        width = 60 * 4
        height = 60
        im = Image.new('RGB', (width, height), (255, 255, 255))
        # 创建Font对象:
        font = ImageFont.truetype(self.FONT_PATH + font, 36)
        # 创建Draw对象:
        draw = ImageDraw.Draw(im)
        # 填充每个像素:
        for x in range(width):
            for y in range(height):
                draw.point((x, y), fill=self.rndColor())
        # 输出文字:
        for t in range(4):
            draw.text((60 * t + 10, 10), self.rndChar(), font=font, fill=self.rndColor2())
        # 模糊:
        im = im.filter(ImageFilter.BLUR)
        im.save(self.PICTURE_PATH + name, 'jpeg')


def add_num(img):
    draw = ImageDraw.Draw(img)
    myfont = ImageFont.truetype('C:/windows/fonts/Arial.ttf', size=40)
    fillcolor = "#ff0000"
    width, height = img.size
    draw.text((width - 40, 0), '99', font=myfont, fill=fillcolor)
    img.save('result.jpg', 'jpeg')

    return 0


def test(img: Image):
    w, h = img.size
    print(w, h)
    img.thumbnail((w // 2, h // 2))
    img.save('../Resources/kid2.jpg', "jpeg")


if __name__ == '__main__':
    path = '../Resources'
    # image = Image.open('../Resources/picture/kid.jpg')
    # add_num(image)
    # test(image)
    pp = PhotoProcess(path)
    pp.generate_verification_code("arial.ttf", "test.jpg")

