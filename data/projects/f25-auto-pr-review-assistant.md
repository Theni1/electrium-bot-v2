---
name: Auto PR Review Assistant
term: Fall 2025
term_code: F25
leads: [Bryan Kuang]
members:
  Team: [Samiksha S., Nathan, Raymond Z, Anushka]
aliases: [Auto PR Reviewer, PR Bot]
---

## Description

A Discord bot that automates code review by connecting directly to GitHub. It gives developers instant feedback on pull requests, including line-change metrics and AI-generated summaries. The project involved significant architectural optimization, moving from blocking requests to a fully asynchronous event loop to handle high volumes of repository events.

## Features

- AI-driven summaries: Formatted commit summaries generated with Deepseek AI.
- Automated metrics: Total lines added and removed for every contributor and pull request.
- Recommendation scoring: An AI-generated score (0 to 100) to help leads prioritize reviews.
- Smart filtering: Mock data and binary files are excluded from AI analysis to save tokens.
- Async optimization: Uses aiohttp and removes nested asyncio.run calls for better performance.
