from hahaha.util import *


def _dog(src: str, my_thing: str, dog_action: str, dog_word: str):
    assert len(dog_word) <= 17, "狗的话太长了！"
    assert len(my_thing) <= 9, "宁的事太长了！"
    assert len(my_thing) <= 13, "狗的事太长了！"
    tpl_img = read_template("my-dog-that-very-night.png")
    source = read(src)
    shape = tpl_img.shape
    source = cv2.resize(source, (shape[1], shape[0]))
    tpl_v = np.array([[0, 0], [0, shape[1] - 1], [shape[0] - 1, 0], [shape[0] - 1, shape[1] - 1]], dtype = np.float32)
    dst_v = np.array([[55, 46], [44, 190], [211, 94], [208, 210]], dtype=np.float32)
    M = cv2.getPerspectiveTransform(tpl_v, dst_v)
    warped = cv2.warpPerspective(source, M, (shape[1], shape[0]))
    warped |= tpl_img

    if len(dog_word) <= 9:
        img1 = add_text(warped, dog_word, 180, 40, size=25)
    else:
        pos = dog_word.index("？") if "？" in dog_word \
            else dog_word.index("?") if "?" in dog_word \
            else int(len(dog_word)/2)
        img_ = add_text(warped, dog_word[:pos+1], 180, 35, size=25)
        img1 = add_text(img_, dog_word[pos+1:], 205, 65, size=25)

    sentence1 = "我家狗听说我" + my_thing
    sentence2 = "连夜" + dog_action
    x1 = 204 - 25 * len(sentence1) / 2
    x2 = 204 - 25 * len(sentence2) / 2

    img2 = add_text(img1, sentence1, x1, 380, size=25)
    img3 = add_text(img2, sentence2, x2, 415, size=25)

    return img3


def dog(*args, **kwargs):
    return wrapper(_dog, *args, **kwargs)


if __name__ == '__main__':
    dog("melon.jpeg", my_thing="复习机器学习", dog_action="帮我把ppt删了", dog_word="机器学习？狗都不学！", out_path="result.jpg")
