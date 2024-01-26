import os
import keyboard

def play_sound():
    os.system('play -n synth 0.1 sine 880')
def play_sound2():
    os.system('play -n synth 0.2 sine 400')
def play_sound3():
    os.system('play -n synth 0.8 sine 250')

keyboard.add_hotkey('F1', play_sound, args=(), suppress=False, trigger_on_release=False)
keyboard.add_hotkey('F2', play_sound2, args=(), suppress=False, trigger_on_release=False)
keyboard.add_hotkey('F4', play_sound3, args=(), suppress=False, trigger_on_release=False)
keyboard.wait('esc')  # Keep the script running until the 'esc' key is pressed
