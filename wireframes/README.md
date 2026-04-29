# Wireframes (Low-Fidelity)

Low-fidelity wireframes showing the redesigned IRCTC booking flow. These focus on structure and information hierarchy without visual design details.

## Redesigned Booking Flow (5 Steps)

### Before: 12 Steps → After: 5 Steps

| Step | Before | After |
|------|--------|-------|
| 1 | Login (CAPTCHA + OTP) | Login (OTP only, trusted devices) |
| 2 | Navigate to "Plan My Journey" | **Search** (single prominent search bar) |
| 3 | Enter source/destination | **Select Train** (filtered results, max 10) |
| 4 | Select date + class | **Passenger Details** (saved passengers, quick add) |
| 5 | Click "Find Trains" | **Payment** (UPI, cards, wallets) |
| 6 | Scroll 50+ results | **Done** (ticket confirmation) |
| 7 | Select train + quota | — |
| 8 | Enter passenger details | — |
| 9 | Enter CAPTCHA (again) | — |
| 10 | Payment redirects | — |
| 11 | Download ticket | — |
| 12 | — | — |

## Key Wireframe Concepts

### 1. Mobile-First Search (Step 1)
```
┌─────────────────────┐
│  IRCTC Redesign     │
├─────────────────────┤
│                     │
│  From: [Delhi ─────]│
│  To:   [Mumbai ────]│
│                     │
│  Date: [📅 Apr 30 ] │
│  Class: [Sleeper ▼] │
│                     │
│  [🔍 Search Trains] │
│                     │
│  Quick: [Recent]    │
│  [Saved] [Popular]  │
└─────────────────────┘
```

### 2. Simplified Results (Step 2)
```
┌─────────────────────┐
│  ← Delhi → Mumbai   │
│  5 trains found     │
├─────────────────────┤
│ ✓ 12951 Mumbai Raj  │
│   16:35 → 08:15     │
│   SL ₹580  │ 3A ₹1.5K│
│   [Book Now →]      │
├─────────────────────┤
│   12953 Aug Kranti  │
│   17:20 → 10:45     │
│   SL ₹580  │ 3A ₹1.5K│
│   [Book Now →]      │
└─────────────────────┘
```

### 3. Quick Passenger Entry (Step 3)
```
┌─────────────────────┐
│  Passenger Details  │
├─────────────────────┤
│  Saved Passengers:  │
│  ☑ Rajesh Kumar     │
│  ☑ Priya Kumar      │
│                     │
│  + Add New Passenger│
│                     │
│  Contact: 98765...  │
│                     │
│  [← Back] [Pay →]   │
└─────────────────────┘
```

## Design Principles Applied

1. **Progressive Disclosure** — Show only what's needed at each step
2. **Saved Preferences** — Remember frequent routes and passengers
3. **Clear Hierarchy** — One primary action per screen
4. **Error Prevention** — Warnings before session timeout
5. **Mobile-First** — All wireframes designed at 375px first

## Differences from Current IRCTC

| Element | Current | Redesigned |
|---------|---------|------------|
| Homepage | 42 elements | 8 elements |
| Search | 2 dropdowns (7000+ items) | Typeahead with top 20 |
| Results | 50+ trains, no default sort | Top 10, sorted by relevance |
| Passengers | Manual entry every time | Saved passengers + quick add |
| Payment | 3 redirects | Single page, 1 click |

---

**Next**: [High-Fidelity Prototype →](hi-fi-prototype.md)
