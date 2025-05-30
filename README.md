# Discord Auto level up

A Discord bot script for auto level up using multiple tokens. It automatically sends random messages to a channel to simulate activity.

---

## ✨ Features

- ✅ Supports multiple tokens
- 🔁 Auto-delete messages after sending (optional)
- ⏳ Detects timeout & slowmode
- 🛡️ Handles rate limits & errors
- 💬 Includes 75+ random chat phrases
- 🖥️ Works on both PC and Termux

---

## 📋 Requirements

- Python 3.7+
- `discord.py` 1.7.3
- `asyncio`
- `colorama`
- `pyfiglet` (for banner display)

All dependencies are included in the `requirements.txt`.

---

## 💻 Installation - Windows / PC

### 📥 Step 1: Clone the repository
```bash
git clone https://github.com/Berachain1/discord-auto-chat.git
cd discord-auto-chat
```

### 🛠️ Step 2: Setup Python & install dependencies
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### 🚀 Step 3: Run the script
```bash
python annisa.py
```

---

## 📱 Installation - Termux (Android)

### 📥 Step 1: Clone the repository
```bash
pkg update && pkg upgrade
pkg install git python
https://github.com/Berachain1/discord-auto-chat.git
cd discord-auto-chat
```

### 🛠️ Step 2: Install dependencies
```bash
pip install -r requirements.txt
```

### 🚀 Step 3: Run the script
```bash
python annisa.py
```

---

## 📌 Usage Instructions

1. **Add your Discord tokens** to a file named `token.txt` (1 token per line):
```
TOKEN1
TOKEN2
```

2. **Run the script** and follow the prompts:
- Input channel ID
- Number of messages to send
- Delay between messages (recommended: 10 seconds)

---

## 🔑 How to Get Your Discord Token

> ⚠️ Use at your own risk — self-bots are against Discord's TOS.

1. Open Discord in your browser
2. Press `F12` to open Developer Tools
3. Go to the **Network** tab
4. Find a request with `authorization` in headers
5. Copy your token from the request headers

---

## 📺 How to Get Channel ID

1. Go to Discord settings
2. Enable **Developer Mode**
3. Right-click the channel you want
4. Click **"Copy ID"**

---

## ⚠️ Warning

> Using self-bots violates Discord's Terms of Service. Use this script at your own risk.

- I take no responsibility for any account bans or misuse.
- By using this script, **you agree** to take full responsibility.
- Use it wisely and ethically.

---

## 🧠 Troubleshooting

- ❌ **Invalid Token**: Replace with a working one in `token.txt`
- ⚠️ **Rate Limited**: Script will automatically wait
- ⏱️ **Timeout or Slowmode**: Will detect and handle it
- 🔒 **Permission Issues**: Make sure tokens have permission to send/delete messages
- 🔇 **Voice Channel?**: Script will warn you

---

## 💡 Tips for Safe Use

- Always use a **10-second delay** or more to avoid detection
- Use **alt accounts**, never your main
- Avoid overusing on one server

---

## 🙏 Support Me

If you appreciate my work and want to support future scripts:

**💸 Tip me (EVM Adress):**  
`0x47e33cec17c1faec718481ef5937d24f9318c031`

Any amount helps and keeps me motivated 💖

---


# discord-auto-chat
