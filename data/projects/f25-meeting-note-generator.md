---
name: Meeting Note Generator
term: Fall 2025
term_code: F25
leads: [Bryan Kuang]
members:
  Team: [Tanish S., Vishal]
aliases: [Meeting Note Bot]
---

## Description

An automation tool that documents team meetings. It captures voice, transcribes it to text, and automatically compiles the results into a central knowledge base without manual work.

## Features

- Deepgram transcription: High-accuracy voice-to-text.
- Google Docs integration: Appends meeting summaries to specific Google Docs without overwriting existing content.
- Configurable environment: Hardcoded paths replaced with configurable lookups for Opus DLLs, making the bot easier to deploy on different systems.
