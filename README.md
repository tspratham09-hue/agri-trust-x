# 🌾 AgriTrustX: The Complete Farmer Operating System

![Python Version](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28%2B-FF4B4B?logo=streamlit)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Maintained](https://img.shields.io/badge/Maintained%3F-yes-brightgreen.svg)

**AgriTrustX** is a resilient, AI-powered agricultural Super App designed to bring enterprise-grade technology to grassroots farmers. Built to solve the critical breakpoints of rural connectivity and language barriers, this platform operates with a zero-downtime architecture to ensure continuous access to essential farming data.

<p align="center">
  <!-- NOTE: Upload one of your dashboard screenshots to your repo and replace the link below -->
  <img src="https://via.placeholder.com/800x400?text=Insert+AgriTrustX+Dashboard+Screenshot+Here" alt="AgriTrustX Dashboard">
</p>

---

## 🚀 The Problem We Solve
Current AgTech solutions often fail grassroots farmers due to three major breakpoints:
1. **Connectivity Failures:** Heavy reliance on fragile live APIs and external image servers causes applications to crash in low-bandwidth rural areas.
2. **Language Barriers:** English-only interfaces alienate the vast majority of local agricultural workers.
3. **Fragmented Ecosystems:** Farmers are forced to use scattered, disconnected apps for weather, market prices, and financial tracking.

## ✨ Key Features & Modules

* **📊 Market Intelligence (100+ Crops):** An offline-resilient market engine utilizing high-res native vector emojis. This guarantees zero broken images and instant load times, even on 2G networks.
* **🌤️ AI Weather Shield:** Contextual atmospheric analysis that translates raw temperature and humidity data into actionable farming advice.
* **🩺 AI Crop Doctor:** A computer-vision module for instant pathogen detection and localized treatment plans.
* **📜 Gov Schemes Engine:** A profile-based eligibility matcher to connect farmers with financial subsidies.
* **📒 Smart Khata:** A digital financial ledger with automated, session-based charting for seasonal expense tracking.
* **🗣️ Instant Tri-Lingual Localization:** A seamless session-state toggle that instantly translates the entire platform into **English, Kannada, or Hindi** without requiring a server reload.

## 📂 Project Structure

```text
agri-trust-x/
├── app.py                 # Main Streamlit application & routing
├── requirements.txt       # Project dependencies
├── background.png         # Custom Glassmorphism UI background
├── logo.png               # Application branding
├── components/            # UI components and core modules
│   ├── auth.py            # Login and session handling
│   ├── crop_doctor.py     # AI disease detection UI
│   ├── khata.py           # Financial ledger interface
│   ├── market.py          # Offline market intelligence module
│   ├── schemes.py         # Gov scheme eligibility engine
│   └── weather.py         # Dynamic weather and AI advisor
└── utils/                 # Helper functions and logic engines
    └── market_engine.py   # Fallback data processors
