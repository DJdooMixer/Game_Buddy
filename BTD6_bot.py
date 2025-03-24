import pyautogui
import time
import numpy as np
import random
from PIL import ImageGrab
import keyboard
import threading
from place_dart_monkey import place_dart_monkey

# Bot activation toggle
bot_running = False
start_time = None

def bot_loop():
    global bot_running, start_time

    while True:
        if bot_running:
            if start_time is None:
                start_time = time.time()

            elapsed_time = round(time.time() - start_time)
            print(f"⏳ Running: {elapsed_time // 60}:{elapsed_time % 60:02d}")

            place_dart_monkey()
            time.sleep(2)
        else:
            time.sleep(1)

def toggle_bot():
    global bot_running, start_time
    bot_running = not bot_running

    if bot_running:
        print("🚀 Bot Started")
        start_time = time.time()
    else:
        elapsed_time = round(time.time() - start_time) if start_time else 0
        print(f"🛑 Bot Stopped. Ran for {elapsed_time // 60} minutes and {elapsed_time % 60:02d} seconds.")

keyboard.add_hotkey("F2", toggle_bot)

bot_thread = threading.Thread(target=bot_loop, daemon=True)
bot_thread.start()

print("Bot is waiting for activation... Press F2 to start.")
keyboard.wait("esc")
