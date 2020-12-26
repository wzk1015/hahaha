import numpy as np
import cv2
from PIL import Image, ImageDraw, ImageFont
import os
import pkg_resources

FONT_PATH = "font/方正兰亭中黑简体.TTF"
PACKAGE_NAME = "hahaha"
template_path = "template-imgs/"


def add_text(img, text, left, top, color=(0, 0, 0), size=20):
    if isinstance(img, np.ndarray):  #判断是否OpenCV图片类型
        img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(img)
    font_text = ImageFont.truetype(FONT_PATH, size, encoding="utf-8")
    draw.text((left, top), text, color, font=font_text)
    return cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)


def check_file(path):
    assert os.path.exists(path), "file '" + path + "' not exists"


def read(path) -> np.ndarray:
    p = pkg_resources.resource_filename(PACKAGE_NAME, path)
    check_file(p)
    return cv2.imread(p)


def read_template(path) -> np.ndarray:
    return read(os.path.join(template_path, path))


def save(path, img):
    cv2.imwrite(path, img)
    print("saved to", path)


def show(name, img):
    print("showing")
    cv2.imshow(name, img)
    cv2.waitKey(0)


def wrapper(f, *args, **kwargs):
    new_kwargs = kwargs.copy()
    if "out_path" in kwargs.keys():
        del new_kwargs["out_path"]
        save(kwargs["out_path"], f(*args, **new_kwargs))
    else:
        show("result", f(*args, **new_kwargs))