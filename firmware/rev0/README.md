# Rev 0 KB2040 Firmware

Breadboard compatibility firmware for the Adafruit KB2040.

## Wiring

| Paddle / jack | KB2040 |
| --- | --- |
| Tip / left paddle / DIT | D2 |
| Ring / right paddle / DAH | D3 |
| Sleeve / common | GND |

The two switched contacts on the Adafruit breadboard-friendly TRS jack are unused.

## Setup

1. Install CircuitPython on the KB2040.
2. Copy the `adafruit_hid` library directory into `CIRCUITPY/lib/`.
3. Copy `code.py` to the root of `CIRCUITPY`.
4. Open a text field and test:
   - DIT -> A
   - DAH -> B

## Notes

The 10 ms debounce value is empirical and intentionally easy to tune.

The A/B HID mapping is temporary. Rev 0 is intended to validate raw dual-paddle operation and browser/mobile compatibility before the final USB protocol is selected.
