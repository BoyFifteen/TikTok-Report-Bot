<img width="1920" height="1078" alt="image" src="https://github.com/user-attachments/assets/83744297-6705-4b6a-982c-776da2f60d05" />
# 🛡️ TikTok Report Bot

![Python](https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge&logo=python)
![Speed](https://img.shields.io/badge/Speed-Extreme-red?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Operational-brightgreen?style=for-the-badge)

A high-performance automated tool designed for mass reporting and feedback simulation on TikTok. Built for researchers and developers to test platform moderation response times through high-concurrency API requests.

---

## ⚡ Core Capabilities

* **Zero-Latency Execution:** Optimized for speed with removed sleep cycles for maximum request flooding.
* **Dynamic Identity Generation:** Each request uses a unique `device_id`, `install_id`, and `openudid` based on 2026 fingerprinting standards.
* **Automated Reason Rotation:** Randomly cycles through multiple report categories (Spam, Harassment, Sexual Content, etc.) to maximize moderation impact.
* **Silent Error Handling:** Automatically skips failed requests or proxy timeouts without interrupting the attack flow.
* **Advanced Multi-Threading:** Support for high-thread counts (50+) to achieve massive throughput.
* **Signature Integration:** Fully compatible with custom `Argus`, `Ladon`, and `Gorgon` signing algorithms.

---

## 🛠️ Technical Architecture

The bot communicates directly with the Feedback API endpoints using optimized headers:
- **Host:** `api16-normal-c-alisg.tiktokv.com`
- **Identity Prefix:** `759xxx` (2026 Hardware Emulation)
- **User-Agent:** Sophisticated Android 12 simulation on Samsung flagship hardware.

---

## 💻 Setup & Usage

1. **Clone the Repo:**
   ```bash
   git clone [https://github.com/BoyFifteen/TikTok-Report-Bot.git](https://github.com/BoyFifteen/TikTok-Report-Bot.git)
   cd TikTok-Report-Bot

```

2. **Install Requirements:**
```bash
pip install requests urllib3

```


3. **Configure Proxies (Optional):**
Add your HTTP/S proxies to `proxies.txt` for IP rotation.
4. **Launch:**
```bash
python main.py

```



---

## 📊 Logging Guide

| Status | Interpretation |
| --- | --- |
| `[SUCCESS]` | Report successfully acknowledged by the server. |
| `[SILENT]` | Any failure (Proxy/Network) is skipped to maintain speed. |

---

## ⚠️ Disclaimer

This project is strictly for **educational purposes** and security research. The developer (@WHI3PER) does not encourage or support the misuse of this tool against the platform's Terms of Service.

---

## 👨‍💻 Developer

Developed and Maintained by **[@WHI3PER](https://t.me/WHI3PER)**.
