import json
import random
import pyautogui
import time
import os
from detect_map import match_map

PLACEMENTS_FILE = "placements.json"

def load_placements():
    if os.path.exists(PLACEMENTS_FILE):
        with open(PLACEMENTS_FILE, "r") as f:
            return json.load(f)
    return {}

def save_placements(data):
    with open(PLACEMENTS_FILE, "w") as f:
        json.dump(data, f, indent=4)

def place_dart_monkey():
    map_name = match_map()
    print(f"🗺 Using placements for: {map_name}")

    placements = load_placements()

    if map_name not in placements:
        placements[map_name] = {"valid": [], "invalid": []}

    dart_monkey = pyautogui.locateOnScreen("dart_monkey.png", confidence=0.7)

    if not dart_monkey:
        print("⚠️ Dart Monkey button not found!")
        return

    x, y = dart_monkey.left + dart_monkey.width // 2, dart_monkey.top + dart_monkey.height // 2
    pyautogui.click(x, y)
    time.sleep(0.5)

    # Try valid spots first
    for pos in placements[map_name]["valid"]:
        pyautogui.click(pos["x"], pos["y"])
        time.sleep(0.5)

        if not pyautogui.locateOnScreen("placement_failed.png", confidence=0.8):
            print(f"✅ Placed Dart Monkey at {pos} on {map_name}!")
            return

    print(f"🤖 Learning new placements for {map_name}...")
    for _ in range(10):
        px = random.randint(700, 900)
        py = random.randint(400, 600)

        if {"x": px, "y": py} in placements[map_name]["invalid"]:
            continue

        pyautogui.click(px, py)
        time.sleep(0.5)

        if not pyautogui.locateOnScreen("placement_failed.png", confidence=0.8):
            print(f"✅ Learned placement at ({px}, {py}) for {map_name}")
            placements[map_name]["valid"].append({"x": px, "y": py})
            save_placements(placements)
            return
        else:
            print(f"❌ Failed at ({px}, {py}), avoiding in future.")
            placements[map_name]["invalid"].append({"x": px, "y": py})
            save_placements(placements)

    print(f"❌ No valid placements found on {map_name}.")
