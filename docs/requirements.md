# Product Requirements

## Product intent

A compact adapter that connects a conventional Morse straight key or iambic paddle to a USB host for CW training and other key-input applications.

## Rev 0 requirements

- Accept a 3.5 mm TRS paddle connection.
- Detect DIT and DAH closures independently.
- Preserve both press and release edges.
- Support simultaneous paddle closures.
- Debounce mechanical contacts without materially harming keying feel.
- Enumerate as a driverless USB input device.
- Work on a desktop browser.
- Be testable with an Android phone/browser over USB-C.

## Product requirements

### Electrical

- USB-C device connector.
- 3.3 V logic domain.
- Protected paddle inputs suitable for repeated external connection.
- ESD protection at user-accessible connectors.
- Input filtering sized for Morse timing rather than generic push-button UI.
- No unsafe current through key contacts.
- Support straight-key and dual-paddle operation.

### USB / protocol

- No vendor-specific desktop driver.
- Host must receive deterministic key state transitions.
- Avoid decoding Morse in the adapter unless a future keyer mode explicitly requires it.
- Final transport must be selected based on desktop and mobile-browser compatibility testing.
- Keyboard-HID fallback may be retained if it materially improves mobile compatibility.

### Mechanical

- Portable enclosure.
- USB-C and TRS connectors accessible without pigtails.
- Cable insertion/removal must not load solder joints excessively.
- PCB mounting and enclosure strategy must support small-batch assembly.

### Productization

- KiCad source files under version control.
- BOM with manufacturer part numbers.
- Programming/debug access on the PCB.
- Manufacturing test points or equivalent production-test interface.
- Defined bring-up and acceptance test.
- Firmware version identification.
- Design should consider EMC/ESD and applicable regulatory requirements before production release.

## Open decisions

- Final MCU: RP2040, RP2350, or another USB-capable MCU.
- Final USB transport: keyboard HID, custom HID, MIDI, composite device, or a combination.
- Whether hardware RC filtering is necessary in addition to firmware debounce.
- Straight-key detection/configuration strategy.
- Status LED requirements.
- Firmware update path.
