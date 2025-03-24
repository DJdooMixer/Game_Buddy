import tkinter as tk
import keyboard
import time
import threading

bot_running = False
start_time = None

# Create overlay window
root = tk.Tk()
root.attributes('-topmost', True)
root.geometry("350x250")
root.title("BTD6 Bot Overlay")
root.configure(bg="#1e1e1e")

# Timer + Status Label
status_label = tk.Label(root, text="Press F2 or click Start", font=("Arial", 12), fg="white", bg="#1e1e1e")
status_label.pack(pady=(10, 5))

# Log Output (like terminal)
# --- Future Improvement: Replace this terminal-style logger with a modern chat-style UI
# showing timestamps, message bubbles, and user-friendly layout for better UX.
log_output = tk.Text(root, height=8, width=45, bg="black", fg="lime", font=("Consolas", 10))
log_output.pack(pady=(5, 5))
log_output.insert(tk.END, "🧠 Bot overlay initialized...\n")
log_output.config(state=tk.DISABLED)

def log_message(message):
    log_output.config(state=tk.NORMAL)
    log_output.insert(tk.END, f"{message}\n")
    log_output.see(tk.END)
    log_output.config(state=tk.DISABLED)

# Toggle function

def toggle_bot():
    global bot_running, start_time
    if not bot_running:
        bot_running = True
        start_time = time.time()
        status_label.config(text="Running: 0:00", fg="lime")
        log_message("🚀 Bot Started")
        update_timer()
    else:
        bot_running = False
        elapsed_time = int(time.time() - start_time)
        minutes, seconds = divmod(elapsed_time, 60)
        status_label.config(text=f"Ran for: {minutes}:{seconds:02d}", fg="red")
        log_message(f"🛑 Bot Stopped. Ran for {minutes}:{seconds:02d}")

# Timer updater

def update_timer():
    if bot_running:
        elapsed_time = int(time.time() - start_time)
        minutes, seconds = divmod(elapsed_time, 60)
        status_label.config(text=f"Running: {minutes}:{seconds:02d}")
        root.after(1000, update_timer)

# Start/Stop Button
start_button = tk.Button(root, text="Start/Stop Bot (F2)", command=toggle_bot, font=("Arial", 11), bg="gray20", fg="white", relief="raised")
start_button.pack(pady=(0, 10))

# Keyboard shortcut
keyboard.add_hotkey("F2", toggle_bot)

# Start the UI
root.mainloop()