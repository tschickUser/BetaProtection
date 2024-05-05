MODEL_NAME = "best.onnx"

SAVE_MODE = True

CENSOR_COLOR = (0, 0, 0)
CENSOR_SCALING = 'box'  # 'image', 'none'

CENSORED_PARTS = [
    "female_genitalia_covered",
    "face_female",
    "buttocks_exposed",
    "female_breast_exposed",
    "female_genitalia_exposed",
    "male_breast_exposed",
    "anus_exposed",
    "feet_exposed",
    "belly_covered",
    "feet_covered",
    "armpits_covered",
    "armpits_exposed",
    "face_male",
    "belly_exposed",
    "male_genitalia_exposed",
    "anus_covered",
    "female_breast_covered",
    "buttocks_covered",
]