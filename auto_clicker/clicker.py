"""
Auto Clicker Script
====================
A simple auto-clicker that simulates mouse clicks at random intervals.

Usage:
- Press 'o' to start or stop the auto-clicker.
- Press 'p' to stop the program and log click data.

"""

import time
import threading
import random
import os
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, KeyCode
from datetime import datetime


class AutoClicker:
    """Handles the auto-clicker functionality."""
    def __init__(self, delay_min=0.001, delay_max=0.003, log_folder="logs"):
        self.delay_min = delay_min
        self.delay_max = delay_max
        self.total_clicks = 0
        self.click_event = threading.Event()
        self.mouse = Controller()
        self.button = Button.left
        self.log_folder = os.path.join(os.path.dirname(__file__), "..", "logs")
        self.log_file = os.path.join(log_folder, "click_log.txt")
        os.makedirs(self.log_folder, exist_ok=True)

    def clicker(self):
        """Continuously click the mouse while the event is set."""
        while True:
            self.click_event.wait()
            self.mouse.press(self.button)
            time.sleep(0.01)
            self.mouse.release(self.button)
            self.total_clicks += 1
            time.sleep(random.uniform(self.delay_min, self.delay_max))

    def save_log(self):
        """Save the current date and total clicks to a file."""
        current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.log_file, "a") as file:
            file.write(f"{current_date} -> Total Clicks: {self.total_clicks}\n")

    def toggle_clicking(self):
        """Toggle the clicking state."""
        if self.click_event.is_set():
            self.click_event.clear()
            print("Stopped clicking.")
        else:
            self.click_event.set()
            print("Started clicking.")

    def stop_program(self):
        """Stop clicking and save log."""
        self.click_event.clear()
        self.save_log()
        print(f"Program terminated. Total clicks: {self.total_clicks}")


def main():
    """Main function to run the auto-clicker."""
    clicker = AutoClicker()
    click_thread = threading.Thread(target=clicker.clicker, daemon=True)
    click_thread.start()

    start_stop_key = KeyCode(char='o')
    stop_key = KeyCode(char='p')

    def toggle_event(key):
        if key == start_stop_key:
            clicker.toggle_clicking()
        elif key == stop_key:
            clicker.stop_program()
            return False

    print("Auto Clicker running. Press 'o' to start/stop. Press 'p' to exit.")
    with Listener(on_press=toggle_event) as listener:
        listener.join()


if __name__ == "__main__":
    main()
