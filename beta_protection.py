import os
from tkinter import *

import tkinter as tk
from tkinter import filedialog

from NudeDetector import NudeDetector
from config import SAVE_MODE


def select_files():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    file_paths = filedialog.askopenfilenames(
        title="Select files",
        filetypes=(("Image files", "*.jpg;*.jpeg;*.png"), ("All files", "*.*"))
    )

    if file_paths:
        return file_paths
    else:
        print("No files selected.")



if __name__ == "__main__":
    file_paths = select_files()
    for file_path in file_paths:
        detector = NudeDetector()
        print(detector.detect(file_path))
        detector.censor(file_path)
        if not SAVE_MODE:
            os.remove(file_path)
