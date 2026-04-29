# Problem Statement

## The Challenge

IRCTC (Indian Railway Catering and Tourism Corporation) is the official portal for booking train tickets in India. With **800,000+ daily bookings** and **25 million registered users**, it's one of the most heavily used government portals in the world.

Yet, it's also one of the most frustrating.

## Current State (Before)

### Booking Flow Complexity
The current IRCTC booking flow requires **12 steps** to complete a single ticket purchase:

1. Login (CAPTCHA + OTP)
2. Navigate to "Plan My Journey"
3. Enter source/destination (dropdown with 7,000+ stations)
4. Select date (calendar widget)
5. Choose class (6 options)
6. Click "Find Trains"
7. Scroll through 50+ train results
8. Select train → Choose quota
9. Enter passenger details (manual entry)
10. Enter CAPTCHA (again)
11. Make payment (multiple redirects)
12. Download ticket

### Key UX Issues

| Issue | Impact | Frequency |
|-------|--------|-----------|
| **Cluttered Homepage** | 40+ clickable elements compete for attention | Every visit |
| **Poor Mobile Experience** | Desktop-first design, tiny touch targets | 60% of users |
| **Confusing Navigation** | Menu items like "Plan My Journey" vs "Book Ticket" cause decision paralysis | First-time users |
| **CAPTCHA Overload** | 3-4 CAPTCHAs per booking session | Every booking |
| **No Error Recovery** | Session timeouts with no warning, lost data | 23% of sessions |
| **Slow Performance** | 8-12 second page loads during peak hours | Peak times (6-10 AM) |
| **Inconsistent Language** | Mix of Hindi/English without clear toggle | Regional users |

## Metrics That Matter

- **68% drop-off rate** during booking process
- **4.2 minutes** average time to complete booking (should be <2 min)
- **3.1/5** user satisfaction rating (App Store reviews)
- **$2.3M daily revenue loss** from abandoned bookings

## Why This Matters

For millions of Indians, train travel is the primary mode of long-distance transportation. A poor booking experience doesn't just frustrate users — it:
- Prevents elderly and non-tech-savvy users from booking independently
- Forces people to pay agents ₹50-200 extra per ticket
- Creates anxiety around travel planning
- Reinforces negative perceptions of government digital services

## Success Metrics (Post-Redesign)

We aim to achieve:
- Reduce booking steps from 12 → 5
- Decrease drop-off rate from 68% → 30%
- Improve mobile satisfaction from 2.8/5 → 4.0/5
- Reduce average booking time from 4.2 min → 1.8 min

## Design Challenge

How might we redesign IRCTC to be:
- **Faster**: Complete booking in under 2 minutes
- **Simpler**: Reduce cognitive load with clear hierarchy
- **Mobile-First**: 60% users are on mobile — design for them first
- **Inclusive**: Accessible to elderly, rural, and non-English speakers
- **Trustworthy**: Clear communication, no surprise errors

---

**Next**: [User Research →](research.md)
