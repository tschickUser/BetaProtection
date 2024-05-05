import math

import cv2

from config import CENSOR_COLOR, CENSOR_SCALING


def censor_scale(image, feature_w, feature_h):
    if CENSOR_SCALING == 'none':
        return 1
    if CENSOR_SCALING == 'box':
        return min(feature_w, feature_h) / 100
    if CENSOR_SCALING == 'image':
        img_h, img_w = image.shape[:2]
        return max(img_h, img_w) / 1000


def pixelate_image(image, x, y, w, h, factor):  # factor 10 means 100x100 area becomes 10x10
    factor *= censor_scale(image, w, h)
    new_w = math.ceil(w / factor)
    new_h = math.ceil(h / factor)
    image[y:y + h, x:x + w] = cv2.resize(
        cv2.resize(image[y:y + h, x:x + w], (new_w, new_h), interpolation=cv2.BORDER_DEFAULT), (w, h),
        interpolation=cv2.INTER_NEAREST)
    return image


def blur_image(image, x, y, w, h, factor):
    factor = 2 * math.ceil(factor * censor_scale(image, w, h) / 2) + 1
    image[y:y + h, x:x + w] = cv2.blur(image[y:y + h, x:x + w], (factor, factor), cv2.BORDER_DEFAULT)
    return image


def bar_image(image, x, y, w, h, color=None):
    if color is None:
        color = CENSOR_COLOR
    image[y: y + h, x: x + w] = color
    return image
