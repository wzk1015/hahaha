import numpy as np
import cv2

import os
import pkg_resources


PACKAGE_NAME = "hahaha"
template_path = "template-imgs/"


def get_path(path):
    return pkg_resources.resource_filename(PACKAGE_NAME, path)


def check_file(path):
    assert os.path.exists(path), "file '" + path + "' not exists"


def read(path) -> np.ndarray:
    p = get_path(path)
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
