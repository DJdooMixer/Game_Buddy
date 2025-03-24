@echo off
cd /d D:\BTD6_bot
start "" D:\BTD6_bot\Winpython64-3.12.9.0dot\WPy64-31290\python\python.exe BTD6_overlay.py
timeout /t 2
start "" D:\BTD6_bot\Winpython64-3.12.9.0dot\WPy64-31290\python\python.exe BTD6_bot.py
