# High-Fidelity Prototype

## Design System

### Colors
| Role | Color | Hex Code | Usage |
|------|-------|----------|-------|
| Primary Neon | Cyan | `#00f5ff` | Buttons, links, active states |
| Secondary Neon | Pink | `#ff00ff` | Gradients, highlights |
| Success | Green | `#39ff14` | Confirmations, after states |
| Error | Red | `#ff4757` | Before states, errors |
| Background | Dark Blue | `#0a0e17` | Page background |
| Card Background | Navy | `#131a2b` | Cards, modals |
| Text | Light Gray | `#e0e0e0` | Primary text |
| Text Dim | Gray | `#888888` | Secondary text |

### Typography
- **Headings**: Segoe UI / System UI, Bold, 1.5-2rem
- **Body**: Segoe UI, Regular, 0.9-1rem
- **Small Text**: 0.75-0.8rem for labels and metadata

### Spacing Scale
- **4px**: Borders, tight spacing
- **8px**: Small gaps between elements
- **16px**: Standard padding inside cards
- **24px**: Spacing between sections
- **32px**: Page margins

### Component Styles

#### Buttons
```css
/* Primary Button */
background: linear-gradient(90deg, #00f5ff, #ff00ff);
color: #0a0e17;
padding: 0.875rem 2rem;
border-radius: 8px;
border: none;
font-weight: bold;
cursor: pointer;
transition: transform 0.2s;

/* Secondary Button */
background: rgba(0, 245, 255, 0.1);
border: 1px solid #00f5ff;
color: #00f5ff;
```

#### Input Fields
```css
background: rgba(255, 255, 255, 0.05);
border: 1px solid #2a3a5c;
border-radius: 8px;
padding: 0.75rem;
color: #e0e0e0;
font-size: 0.9rem;
```

#### Cards
```css
background: #131a2b;
border: 1px solid #2a3a5c;
border-radius: 12px;
padding: 1.25rem;
box-shadow: 0 0 30px rgba(0, 245, 255, 0.1);
```

## Visual Hierarchy (After)

### Homepage
1. **Logo + Header** (gradient cyan-pink)
2. **Search Card** (prominent, centered, neon border)
3. **Quick Tags** (recent routes, popular destinations)
4. **Footer** (minimal, legal links only)

### Search Results
1. **Train Cards** (sorted by departure time)
2. **Class Availability** (color-coded: green=available, red=full)
3. **Book Now Button** (neon gradient, pulsing animation)
4. **Filters** (collapsible, top-right corner)

### Booking Flow
1. **Step Indicator** (1/5, 2/5... at top)
2. **Progress Bar** (neon gradient fill)
3. **Form Fields** (one per screen, no scrolling)
4. **Navigation** (Back | Continue)

## Animation & Interaction

### Micro-Interactions
- **Button Hover**: Scale up 2% + glow effect
- **Input Focus**: Neon border glow (0 0 10px rgba(0,245,255,0.2))
- **Success State**: Green flash + checkmark animation
- **Loading**: Neon pulse animation (not spinning wheel)

### Page Transitions
- **Slide Left**: Moving to next step
- **Slide Right**: Going back
- **Fade**: Modal open/close

## Responsive Breakpoints

| Device | Width | Changes |
|--------|-------|---------|
| Mobile | 375px | Single column, full-width buttons |
| Tablet | 768px | Two-column results, larger touch targets |
| Desktop | 1440px | Three-column layout, sidebar filters |

## Accessibility Features

- **Contrast Ratio**: 4.5:1 minimum (WCAG AA)
- **Touch Targets**: 44px minimum
- **Focus Indicators**: Neon glow on keyboard navigation
- **Alt Text**: All images and icons
- **ARIA Labels**: All form elements
- **Font Size**: 16px minimum (prevents iOS zoom on focus)

---

**Next**: [Final Screens →](final-screens.md)
