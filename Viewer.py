import cv2
import numpy as np


ant_img = cv2.imread('ant.png')
bug_img = cv2.imread('bug.png')


def draw(env):
    img = np.ones((env.blocks.shape[1] * 50, env.blocks.shape[0] * 50, 3), dtype=np.uint8) * 255
    for i in range(env.blocks.shape[0]):
        for j in range(env.blocks.shape[1]):
            if env.blocks[i][j] is not None:
                img[j * 50:(j + 1) * 50, i * 50:(i + 1) * 50] = ant_img if env.blocks[i][j].__class__.__name__ == 'Ant' else bug_img
    return img
