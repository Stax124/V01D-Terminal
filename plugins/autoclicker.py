import time
import sys
import threading
from prompt_toolkit import print_formatted_text
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, KeyCode

class ClickMouse(threading.Thread):
    def __init__(self, delay, button, mouse):
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.mouse = mouse
        self.button = button
        self.running = False
        self.program_running = True

    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_running = False

    def run(self):
        print_formatted_text("[E]xit, [S]tart | [S]top")
        while self.program_running:
            while self.running:
                self.mouse.click(self.button)
                time.sleep(self.delay)
            time.sleep(0.1)




class Autoclicker(object):
    def on_press(self,key):
        if key == self.start_stop_key:
            if self.click_thread.running:
                self.click_thread.stop_clicking()
            else:
                self.click_thread.start_clicking()
        elif key == self.exit_key:
            self.click_thread.exit()
            self.listener.stop()

    def __init__(self,button,delay):
        super().__init__()
        self.mouse = Controller()
        self.delay = delay
        self.button = button
        self.click_thread = ClickMouse(delay, button, self.mouse)
        self.click_thread.start()
        self.start_stop_key = KeyCode(char='s')
        self.exit_key = KeyCode(char='e')
        self.listener = Listener(on_press=self.on_press)
        self.listener.start()

    def start(self):
        self.listener.join()