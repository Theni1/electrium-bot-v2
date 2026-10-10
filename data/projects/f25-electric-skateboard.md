---
name: Electric Skateboard
term: Fall 2025
term_code: F25
leads: [Leopoldo Mendoza]
members:
  Mechanical: [Zahran Mohammad, Christopher Wong, Divit Gawri, Nina Matthew, Evana Trinh, Junaid Haque, Ali Asif, Abdullah Atif]
  Electrical: [Mike Yao, Arnav Shah, Catherine Huang, Haris Niaz, BingBing Zheng, Kashan Khan, Dhyey Patel, Leopoldo Mendoza]
  Firmware: [Ethan Sun, Dhyey Patel, Kashan Khan, Minh Nguyen, Daniel Zheng, Leopoldo Mendoza]
aliases: [F25 Skateboard]
---

## Description

An electric skateboard with the battery pack, longboard deck, and electronics enclosure built in house. On top of the core vehicle, the team designed its own power distribution, telemetry, and lighting systems. Members developed skills across CAD in SolidWorks, schematic capture and PCB layout in KiCad, and embedded C on ESP32 and AVR.

## Features

### Longboard Deck

9-layer maple veneer, vacuum pressed with a foam mold. The deck and mold were modelled in SolidWorks before fabrication.

### Electronics Enclosure

3D printed after optimizing the SolidWorks model to meet height and weight clearances while housing all electronics, including the battery pack, VESC, power distribution, telemetry, and wiring harness.

### Battery Pack

12S2P with nominal specs of 43.2V, 5600mAh, 242Wh. Equipped with a BMS to safely power all other electronics.

### Power Distribution

Two-stage power delivery using buck converters with a robust input protection circuit. It steps the battery voltage down from 43.2V to 12V to 3.3V, feeding the head and tail lights and the lighting control and telemetry MCUs. PCB designed in KiCad.

### Telemetry

An ESP32 shows key vehicle metrics in real time on an onboard OLED display and on a phone over BLE. It communicates with the VESC and BMS over UART. PCB designed in KiCad.

### Lighting

Vehicle-grade head and tail lights controlled by an ATmega328P programmed in bare-metal C. Each unit has multiple lighting modes, including accelerometer-guided brake lights.
