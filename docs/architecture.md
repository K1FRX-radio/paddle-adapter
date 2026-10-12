# Architecture

## Rev 0

```text
                     KB2040
3.5 mm TRS          (RP2040)                USB host
-----------        -----------             -----------
Tip / DIT  ------> D2   |
Ring / DAH ------> D3   | -> debounce -> USB keyboard HID
Sleeve     ------> GND  |
```

The KB2040 internal pull-ups hold both inputs high. Closing either paddle connects its input to ground.

Current prototype behavior:

- released = HIGH
- pressed = LOW
- 10 ms software debounce
- DIT reports keyboard key A
- DAH reports keyboard key B

This mapping is a compatibility test, not the final product protocol.

## Intended Rev A architecture

```text
USB-C
  |
  +-- ESD / USB protection
  |
MCU + flash / power
  |
  +-- DIT input protection/filtering --+
  |                                     +-- 3.5 mm TRS
  +-- DAH input protection/filtering ---+
  |
  +-- status indication
  |
  +-- programming/debug/test pads
```

## Design principles

1. Preserve raw contact timing.
2. Keep Morse decoding on the host for the base product.
3. Keep transport concerns separate from keying semantics.
4. Treat mobile-browser compatibility as a first-class requirement.
5. Use the breadboard only to retire architecture risk; move to a custom PCB quickly.
