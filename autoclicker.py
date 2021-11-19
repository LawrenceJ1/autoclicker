from pynput import mouse
from pynput import mouse, keyboard
import threading
from time import sleep

mice = mouse.Controller()
start_stop_key = keyboard.KeyCode(char="s")
exit_key = keyboard.KeyCode(char="e")
button = mouse.Button.left
delay = 0.001

class ClickMouse(threading.Thread):
    def __init__(self, delay, button):
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_run = True
    
    def start_clicking(self):
        self.running = True
    
    def stop_clicking(self):
        self.running = False
        
    def exit(self):
        self.stop_clicking()
        self.program_run = False
        
    def run(self):
        while self.program_run:
            while self.running:
                mice.click(self.button)
                sleep(self.delay)
            sleep(0.1)
            
thread = ClickMouse(delay, button)
thread.start()

def on_press(key):
    if key == start_stop_key:
        if thread.running:
            thread.stop_clicking()
        else:
            thread.start_clicking()
    elif key == exit_key:
        thread.exit()
        listener.stop()
        
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()