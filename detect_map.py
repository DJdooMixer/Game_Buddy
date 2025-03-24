import cv2
import numpy as np
import pyautogui
import os

MAPS_FOLDER = "maps/"

def capture_current_map():
    screenshot = pyautogui.screenshot(region=(200, 100, 600, 400))  # Adjust as needed
    return np.array(screenshot)

def match_map():
    current_img = cv2.cvtColor(capture_current_map(), cv2.COLOR_BGR2GRAY)

    for map_file in os.listdir(MAPS_FOLDER):
        map_path = os.path.join(MAPS_FOLDER, map_file)
        saved_img = cv2.imread(map_path, cv2.IMREAD_GRAYSCALE)

        if saved_img is None:
            continue

        result = cv2.matchTemplate(current_img, saved_img, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, _ = cv2.minMaxLoc(result)

        if max_val > 0.8:
            return os.path.splitext(map_file)[0]

    return "Unknown Map"
