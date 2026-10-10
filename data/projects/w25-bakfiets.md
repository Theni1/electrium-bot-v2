---
name: Bakfiets
term: Winter 2025
term_code: W25
leads: [Jerry Chen]
subteam_leads:
  Mechanical: [Jerry Chen]
  Firmware: [Patrick He]
  Electrical: [Samuel Ke]
members:
  Mechanical: [Jerry Chen, Kevin Ng, Aidan Thompson, Aiyesha Shibly, Samual Wong, Allen Lu]
  Firmware: [Patrick He, Kimberley Hoang, Alisa Wu, Aman Zaveri]
  Electrical: [Jacob Wielowieyski, Alex Liu, Samuel Ke, Suhyma Rahman]
aliases: [Bak Choy]
---

## Description

A bakfiets is a front-loading cargo bike, popular in the Netherlands for carrying groceries or bringing kids to school. Electrium's bakfiets, "Bak Choy", is an electrically assisted bakfiets with a custom-built frame, 48V electrical system, dynamic lighting, and a display interface.

## Features

- Custom frame: Tailor-made 4130 chromoly frame designed using SolidWorks Weldments, with two 26-inch wheels, disc brakes, and a suspension fork.
- Welding jig: The rear triangle is welded using Electrium's standard adjustable aluminum extrusion bike jig, while the main frame is welded using a single-use laser cut MDF jig.
- Steering system: The steering connects to the front fork through a linkage of an adjustable-length steel tube with ball joints on either end. The linkage was optimized for a natural turning rate and to clear other components. A solid linkage was chosen over a cable-driven system for simplicity and reliability.
- Kickstand: Heavy-duty spring-loaded mild steel kickstand with a lowered middle to clear the steering linkage.
- 48V electrical system: A 48V 12S3P 18650 quick-release battery pack, a 500W hub motor, and a 48V/5V power distribution board powering the undermounted LED strip and microcontroller. The team also attempted to design its own anti-spark circuit to protect the battery.
- VESC motor controller: An open-source FSESC6.7 VESC-based motor controller runs the motor and interfaces with the microcontroller.
- Display interface: An OLED display driven by an ESP32 S3 Pico shows speed, battery, and power level. The microcontroller also runs the LED strip using the FastLED library, supporting a variety of patterns and segmented turn signals.

## Goals

The goal was to improve members' mechanical, electrical, and firmware abilities. For many, it was their first time using SolidWorks weldments, designing electronics enclosures, and creating welding jigs. Members also learned machining, tube notching, and woodworking. The power distribution board and anti-spark circuit were among the team's first custom PCBs, and members learned to solder XT30/XT60 connectors and SMD components, control a VESC, and program microcontrollers to respond to user input.
