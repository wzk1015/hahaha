from hahaha.util import *


def _bang(times: int):
    src = read_template("bang2.png")
    bang = read_template("bang.png")
    width = 90 + 40 * times
    height = 80 + 40 * times
    target = np.zeros([height, width, 3])
    np.set_printoptions(threshold=np.inf)
    for i in range(80):
        for j in range(90):
            target[i][j][0] = src[i][j][0]
            target[i][j][1] = src[i][j][1]
            target[i][j][2] = src[i][j][2]
    index1 = 40
    index2 = 50
    for k in range(times):
        for i in range(80):
            for j in range(80):
                target[index1 + i][index2 + j][0] = target[index1 + i][index2 + j][0] if bang[i][j][0] == 255 else \
                    bang[i][j][0]
                target[index1 + i][index2 + j][1] = target[index1 + i][index2 + j][1] if bang[i][j][0] == 255 else \
                    bang[i][j][1]
                target[index1 + i][index2 + j][2] = target[index1 + i][index2 + j][2] if bang[i][j][0] == 255 else \
                    bang[i][j][2]

        index1 += 40
        index2 += 40
    for i in range(width):
        for j in range(height):
            target[j][i] = [255, 255, 255] if target[j][i][0] == 0 else target[j][i]
    target = target[::-1, :, :3]
    return target


def bang(*args, **kwargs):
    return wrapper(_bang, *args, **kwargs)


if __name__ == '__main__':
    bang(5, out_path="result2.jpg")