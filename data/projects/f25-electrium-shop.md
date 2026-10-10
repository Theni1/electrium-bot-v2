---
name: Electrium Shop
term: Fall 2025
term_code: F25
leads: [Bryan Kuang]
aliases: [Electrium Mobility Shop]
---

## Description

The Electrium Mobility Shop is an online storefront to showcase and sell Electrium's personal electric vehicles and accessories. In Fall 2025 the platform was significantly refactored to improve responsiveness, user experience, and functionality. Key updates include a full UI/UX overhaul with dark mode, a product review system, improved checkout with PayPal integration, and major performance optimizations.

## Features

### UI/UX

- Dark mode variants for all color classes and semantic theme variables
- Loading spinners and buttons across the app (checkout, profile, dashboard, cart, login, signup)
- Route progress indicator for smoother navigation
- Standardized button styles, hover states, padding, and margins, with hardcoded colors replaced by theme variables

### Payment and Checkout

- PayPal payment verification and an improved payment flow
- Shipping form auto-filled from the user's profile
- Fixed shipping cost calculation and display

### Product Reviews

- Mock data replaced with a working Reviews API (GET/POST)
- Logged-in users can rate products and leave comments on the product page
- Product page layout updated to integrate reviews

### Shopping Cart

- Improved input handling and validation when adding items
- Price displays show rental rates for rentable items
- Default cart quantity set to 1

### Dashboard and Profile

- Redesigned dashboard with improved stats, readability, and layout
- Improved styling for the profile page

### Orders and Rentals

- Dedicated rental history section on the orders page
- Improved tracking and display of past orders

### Performance and Technical

- Server components migrated to client components for a smoother UX
- Error handling and retry logic for fetching bike data
- Dependency conflicts resolved by adjusting versions (e.g. glob)
- Unused imports and variables removed
