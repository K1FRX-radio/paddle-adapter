import time
import board
import digitalio
import usb_hid

from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

DEBOUNCE_S = 0.010

dit = digitalio.DigitalInOut(board.D2)
dit.direction = digitalio.Direction.INPUT
dit.pull = digitalio.Pull.UP

dah = digitalio.DigitalInOut(board.D3)
dah.direction = digitalio.Direction.INPUT
dah.pull = digitalio.Pull.UP

keyboard = Keyboard(usb_hid.devices)

last_raw_dit = dit.value
last_raw_dah = dah.value
stable_dit = last_raw_dit
stable_dah = last_raw_dah

dit_changed_at = time.monotonic()
dah_changed_at = time.monotonic()

while True:
    now = time.monotonic()

    raw_dit = dit.value
    raw_dah = dah.value

    if raw_dit != last_raw_dit:
        last_raw_dit = raw_dit
        dit_changed_at = now

    if raw_dit != stable_dit and (now - dit_changed_at) >= DEBOUNCE_S:
        stable_dit = raw_dit
        if stable_dit:
            keyboard.release(Keycode.A)
        else:
            keyboard.press(Keycode.A)

    if raw_dah != last_raw_dah:
        last_raw_dah = raw_dah
        dah_changed_at = now

    if raw_dah != stable_dah and (now - dah_changed_at) >= DEBOUNCE_S:
        stable_dah = raw_dah
        if stable_dah:
            keyboard.release(Keycode.B)
        else:
            keyboard.press(Keycode.B)

    time.sleep(0.0005)
