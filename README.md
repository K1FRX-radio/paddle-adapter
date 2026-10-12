# K1FRX Paddle Adapter

Compact USB-C interface for connecting a Morse straight key or iambic paddle to phones and computers.

The project starts with an Adafruit KB2040 breadboard prototype and is intended to progress to a custom manufacturable PCB, enclosure, and production-ready firmware.

## Current status

**Rev 0 breadboard proof of concept**

Validated hardware path:

```text
Begali paddle -> 3.5 mm TRS jack -> KB2040 GPIO -> debounce -> USB HID -> host
```

Current prototype mapping:

- Tip: left paddle / DIT
- Ring: right paddle / DAH
- Sleeve: common ground
- DIT GPIO: D2
- DAH GPIO: D3
- Debounce: 10 ms software debounce
- USB compatibility mapping: DIT = `A`, DAH = `B`

The A/B keyboard mapping is intentionally temporary. It exists to validate phone/browser compatibility before the final USB interface is selected.

## Project goals

- 3.5 mm TRS input for straight keys and iambic paddles
- USB-C
- Driverless operation where practical
- Phone, tablet, and desktop compatibility
- Low and deterministic input latency
- Raw press/release event fidelity
- Compact portable enclosure
- Custom KiCad PCB suitable for small-batch manufacturing
- Testable firmware and production test strategy

## Repository layout

```text
firmware/    Prototype and production firmware
hardware/    KiCad schematic, PCB, libraries, and fabrication notes
mechanical/  Enclosure and mechanical interface files
docs/        Requirements, architecture, bring-up, and validation
bom/         BOM and sourcing information
test/        Hardware and firmware test procedures
```

## Development phases

1. **Rev 0 — Breadboard**
   - Validate paddle electrical interface
   - Characterize debounce
   - Validate USB HID behavior on desktop and mobile browsers
2. **Rev A — Custom PCB**
   - MCU, USB-C, TRS input, ESD protection, filtering, status indication
   - Bring-up and compatibility testing
3. **Rev B — Product prototype**
   - DFM, enclosure, manufacturing test, BOM optimization, regulatory planning

The companion browser integration lives in the
[K1FRX Morse Trainer](https://github.com/K1FRX-radio/morse-trainer).
