#  Network Authentication Monitor (SOC Capstone Project)

## Overview
The **Network Authentication Monitor** is a Security Operations Center (SOC) tool designed to detect, log, and alert against brute-force authentication attacks in real-time. It uses a sliding window rate-limiting algorithm to identify anomalous login patterns from specific IP addresses.
**author:**Aditya Tiwari

## Features Implemented
* **Real-time Credential Validation:** Verifies incoming authentication requests against a secure backend store (`aditya78_root` / `aditya123`).
* **Sliding Window Algorithm:** Tracks failed login attempts dynamically using `collections.deque` over a strict time threshold (5 failed attempts within 120 seconds).
* **Automated SOC Alerting:** Instantly triggers critical security logs and dashboard alerts upon threshold breach.
* **Interactive Dashboard UI:** Built with Flask and Bootstrap 5, featuring a high-contrast dark blue corporate theme for monitoring.

## Tech Stack
* **Backend:** Python, Flask, Collections (deque, defaultdict), Logging
* **Frontend:** HTML5, Bootstrap 5, JavaScript (Fetch API)

## How to Run
1. Install Flask: `pip install flask`
2. Run the application: `python app.py`
3. Open your browser and go to: `http://127.0.0.1:5000`