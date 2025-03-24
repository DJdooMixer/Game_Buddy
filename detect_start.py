import cv2
import numpy as np
import pyautogui
import time

def find_start_button():
    """Searches for the Start button and clicks it if found."""
    screenshot = pyautogui.screenshot()
    screenshot = np.array(screenshot)

    # Load the Start button image
    button_template = cv2.imread("D:/BTD6_bot/images/start_button.png", cv2.IMREAD_GRAYSCALE)
    screenshot_gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)

    # Match template
    result = cv2.matchTemplate(screenshot_gray, button_template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    if max_val > 0.8:  # Confidence threshold (adjust if needed)
        x, y = max_loc
        pyautogui.click(x, y)
        print("✅ Clicked Start Button!")
        return True
    else:
        print("⚠️ Start button not found.")
        return False

if __name__ == "__main__":
    time.sleep(2)  # Give time to switch to game
    find_start_button()
