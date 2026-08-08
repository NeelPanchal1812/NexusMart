# 🛒 NEXUS MART — Next-Gen Full-Stack E-Commerce Platform

![Django](https://img.shields.io/badge/Django-5.2-092E20?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)
![UI/UX](https://img.shields.io/badge/UI/UX-Glassmorphism-violet?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Production%20Ready-success?style=for-the-badge)

**NEXUS MART** is a feature-rich, high-performance E-Commerce platform built with **Django** and modern **Vanilla CSS Glassmorphism**. Designed for ultra-smooth user experience, it features zero-reload AJAX cart/wishlist management, real-time instant search autocomplete, persistent viewport-fixed AI Shopping Assistant, responsive 4-column product grid, and interactive price filtering.

---

## 🌟 Key Platform Features

### 🚀 1. Zero-Reload SPA Performance (AJAX Engine)
- **Instant Shopping Actions**: Add to Cart, Wishlist toggling, and Cart Quantity (+/-) operate seamlessly without full-page reloads.
- **Dynamic Cart Badges & Toasts**: Instant real-time updates to cart counter badges and 3D animated toast notifications.

### 🔍 2. Real-Time Instant Search & Autocomplete
- **Live Search Dropdown**: Interactive preview box directly below search bar showing product thumbnails, titles, category badges, and prices (`₹`).
- **Click-Outside & Re-Focus Restore**: Preserves typed input query when clicking outside, and instantly re-opens search preview when re-focusing on the search bar.
- **Search Results Banner & Auto-Scroll**: Active search query tags with 1-click removal and smooth automatic scrolling to search results below the filter panel.

### 🤖 3. Persistent Viewport-Fixed AI Shopping Assistant
- **Pinned Assistant Drawer**: Fixed bottom-right positioning (`position: fixed !important; z-index: 99999 !important;`) isolated from page transforms.
- **Always Accessible**: Remains statically pinned to screen across all scroll positions and route navigation transitions.

### 🎨 4. Modern Glassmorphism Design System
- **Dark/Light Mode Theme Engine**: Smooth dark mode toggle with high-contrast text styling across all inputs, tables, cards, and dropdowns.
- **Responsive 4-Column Product Grid**: Optimized grid layout (`col-xl-3 col-lg-4 col-sm-6`) replacing vertical sidebar empty spaces.
- **3D Bounce Animated Toast System**: Custom glassmorphic alert notifications with 5-second progress bar timer.
- **Interactive Price Filtering**: Live price display slider, preset quick chips (Under ₹10k, ₹10k - ₹30k, ₹30k - ₹75k, ₹75k+), and currency input badges.

### ❤️ 5. Synchronized Database-to-UI Wishlist State
- **Persistent Heart Status**: User wishlist product IDs are queried in Django views (`wishlist_product_ids`), ensuring heart icons remain filled red (`text-danger`) across page refreshes and detail views.
- **Full-Card Click Navigation**: Clicking anywhere on product cards (`data-url`) opens detail pages while preserving individual action buttons.

### ⬅️ 6. Universal Navigation & Back Buttons
- Glassmorphic **`← Back`** buttons integrated across Product Detail, Shopping Cart, Checkout, Orders, Order Details, Payment, Profile, Wishlist, and Analytics pages.

---

## 🐛 Resolved Issues & Technical Changelog

| Issue # | Reported Issue | Technical Resolution |
| :--- | :--- | :--- |
| `#1` | **Tall Empty Sidebar & Dark Mode Text Visibility** | Removed vertical sidebar in favor of a horizontal Category Pills Bar. Expanded grid to 4-column responsive layout. Enforced `#f8fafc` text contrast in dark theme. |
| `#2` | **Full Page Reloads on Clicks** | Implemented global JS event delegation intercepting Add to Cart, Wishlist, and Quantity (+/-) links, returning Django `JsonResponse`. |
| `#3` | **Alert System Animations** | Built a custom 3D spring entrance/slide-out exit Toast Notification system with 5s progress bar timer. |
| `#4` | **Price Filter UI Polish** | Added Quick Preset Price Chips (`Under ₹10k`, `₹10k - ₹30k`, `₹30k - ₹75k`, `₹75k+`), currency badges, and live display. |
| `#5` | **Search Results Display Location** | Added an active Search Query & Filter Status Banner right below filter panel with smooth `scrollIntoView()` auto-scroll. |
| `#6` | **AI Chatbot Screen Drift** | Isolated CSS `transform` from `body` onto `.page-content-wrapper` so `position: fixed` chatbot widget stays statically pinned to viewport window. |
| `#7` | **Full-Card Click Navigation** | Implemented `data-url` event delegation on `.product-card-premium` cards while protecting action buttons. |
| `#8` | **Missing Back Navigation** | Added glassmorphic `← Back` buttons across all secondary and detail views. |
| `#9` | **Wishlist Database-to-UI State Sync** | Queried `wishlist_product_ids` in Django `home` and `detail` views so wishlisted items remain filled red (`text-danger`) on page refresh. |
| `#10` | **Search Box Blur & Re-Focus Behavior** | Preserved typed search text on click-outside and restored autocomplete dropdown upon re-focusing search input. |
| `#11` | **3D Logo & Hero Showcase Banner** | Generated futuristic 3D NEXUS MART brand logo and embedded right-side Welcome showcase banner into home page grid. |

---

## 🛠️ Technology Stack

- **Backend**: Python 3.11+, Django 4.2+ / 5.2
- **Frontend**: HTML5, Vanilla JavaScript (ES6+), Bootstrap 5.3, Vanilla CSS3 (Glassmorphism, Animations)
- **Icons & Fonts**: FontAwesome 6 Free, Plus Jakarta Sans (Google Fonts)
- **Database**: SQLite (Development) / PostgreSQL (Production)
- **Static Assets**: WhiteNoise Static File Storage

---

## 💻 Installation & Local Development Setup

### 1. Clone Repository
```bash
git clone https://github.com/NeelPanchal1812/NexusMart.git
cd NexusMart
```

### 2. Create & Activate Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run Migrations & Setup Database
```bash
python manage.py migrate
```

### 5. Create Superuser (Optional Admin Access)
```bash
python manage.py createsuperuser
```

### 6. Start Development Server
```bash
python manage.py runserver
```
Visit `http://127.0.0.1:8000/` in your browser!

---

## 👤 Author & Maintainer

- **Developer**: Neel Panchal
- **Repository**: [https://github.com/NeelPanchal1812/NexusMart](https://github.com/NeelPanchal1812/NexusMart)
- **License**: MIT License
