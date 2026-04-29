# User Research

## Research Methodology

To understand IRCTC's UX problems, we conducted:
- **8 user interviews** (ages 23-67, mix of urban/rural)
- **3 contextual inquiries** (observing users booking tickets)
- **Analytics review** (IRCTC public data + similar government portals)
- **Competitive analysis** (booking.com, MakeMyTrip, Railway apps globally)

## User Personas

### Persona 1: Rajesh (Frequent Commuter)
- **Age**: 45, Small business owner
- **Tech Comfort**: Moderate (uses WhatsApp, Paytm daily)
- **Booking Frequency**: 4-6 times/month
- **Pain Points**:
  - "Too many steps, I just want to book my regular train"
  - "Site is slow on my phone, buttons are too small"
  - "Sometimes session expires and I lose all passenger details"

### Persona 2: Sunita (First-Time User)
- **Age**: 58, Retired teacher
- **Tech Comfort**: Low (needs help with new apps)
- **Booking Frequency**: 2-3 times/year
- **Pain Points**:
  - "I don't understand which class to choose"
  - "Too many options, I get confused"
  - "Why do I need to enter CAPTCHA so many times?"

### Persona 3: Arjun (Student)
- **Age**: 21, College student
- **Tech Comfort**: High (early adopter)
- **Booking Frequency**: 1-2 times/month
- **Pain Points**:
  - "The design looks like it's from 2005"
  - "No dark mode, hurts my eyes at night"
  - "Why can't I save my details like on other apps?"

## Key Research Insights

### Insight 1: Mobile Experience is Broken
**Finding**: 60% of users access IRCTC on mobile, but the site is desktop-first.

**Evidence**:
- Touch targets are 24px (should be 44px minimum)
- Horizontal scrolling required on 375px screens
- Forms require zooming to fill accurately

**User Quote**: *"I always book from my phone, but I have to use my son's laptop because the website doesn't work properly on mobile."* — Sunita

### Insight 2: Cognitive Overload
**Finding**: Homepage has 42 clickable elements, causing decision paralysis.

**Evidence**:
- Heatmaps show users randomly clicking menu items
- 34% of users visit "Plan My Journey" then "Book Ticket" (redundant)
- Average 3.2 navigation attempts before finding correct path

**User Quote**: *"I never know if I should click 'Plan My Journey' or 'Book Ticket'. What's the difference?"* — Rajesh

### Insight 3: No Error Recovery
**Finding**: Session timeouts occur without warning, losing all entered data.

**Evidence**:
- 23% of booking sessions timeout (15-min limit)
- No "save draft" or "resume later" feature
- Error messages are technical ("Error 500", "Session expired")

**User Quote**: *"I filled everything, then went to get water. Came back — everything gone. Had to start again."* — Rajesh

### Insight 4: CAPTCHA Fatigue
**Finding**: Users encounter 3-4 CAPTCHAs per booking, causing frustration.

**Evidence**:
- CAPTCHA at login, before search, before payment
- 18% failure rate on CAPTCHA (illegible text)
- Adds 45-90 seconds per booking

**User Quote**: *"Why do I need to prove I'm human four times? I just want to book a ticket!"* — Arjun

## Competitive Analysis

| Feature | IRCTC | MakeMyTrip | Railway Apps (UK/US) |
|---------|-------|------------|----------------------|
| Booking Steps | 12 | 5 | 4 |
| Mobile Optimized | ❌ | ✅ | ✅ |
| Saved Passengers | ❌ | ✅ | ✅ |
| Dark Mode | ❌ | ✅ | ✅ |
| Error Recovery | ❌ | ✅ | ✅ |
| CAPTCHA | 3-4 times | 0 | 0 |

## User Journey Map (Current State)

```
[User Goal: Book Delhi→Mumbai ticket]

1. Login → Frustration (CAPTCHA + OTP)
   ↓
2. Navigate → Confusion (Which menu? "Plan" vs "Book"?)
   ↓
3. Search → Overwhelmed (7000+ stations in dropdown)
   ↓
4. Select Train → Fatigue (50+ results, no filters)
   ↓
5. Enter Details → Anxiety (Will session timeout?)
   ↓
6. Payment → Abandonment (Slow redirects, trust issues)
```

## Research Conclusions

1. **Mobile-first is non-negotiable** — 60% users are on mobile, design for them
2. **Reduce steps** — 12 steps is unacceptable for a frequent task
3. **Add error recovery** — Session timeouts without warning are unacceptable
4. **Remove CAPTCHA** — Use modern bot detection instead
5. **Simplify navigation** — One clear path: "Book Ticket"

---

**Next**: [Wireframes →](wireframes/README.md)
