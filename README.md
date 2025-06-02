# Discord Auto level up Join My chanel Telegram : https://t.me/AIRDROPRSIND123

A Discord bot script for auto level up using multiple tokens. It automatically sends random messages to a channel to simulate activity.

---

## ✨ Features

* ✅ Supports multiple tokens
* 🔁 Auto-delete messages after sending (optional)
* ⏳ Detects timeout & slowmode
* 🛡️ Handles rate limits & errors
* 💬 Includes 75+ random chat phrases
* 🖥️ Works on both PC and Termux
- ✅ Supports multiple tokens
- 🔁 Auto-delete messages after sending (optional)
- ⏳ Detects timeout & slowmode
- 🛡️ Handles rate limits & errors
- 💬 Includes 250+ random chat phrases
- 🖥️ Works on both PC and Termux

---

## 📋 Requirements

* Python 3.7+
* `discord.py` 1.7.3
* `asyncio`
* `colorama`
* `pyfiglet` (for banner display)

All dependencies are included in the `requirements.txt`. However, make sure `pyfiglet` is installed successfully before running the script.

---

## 💻 Installation - Windows / PC

### 📅 Step 1: Clone the repository

```bash
git clone https://github.com/Berachain1/discord-auto-chat.git
cd discord-auto-chat
```

### 🛠️ Step 2: Setup Python & install dependencies

```bash
python3 -m venv venv
```

```bash
venv\Scripts\activate
```

```bash
pip install -r requirements.txt
```

If you encounter an error about `pyfiglet`, install it manually:

```bash
pip install pyfiglet
```

### 🚀 Step 3: Run the script

```bash
python annisa.py
```

---

## 📱 Installation - Termux (Android) / Linux / Ubuntu

### 📅 Step 1: Clone the repository

```bash
pkg update && pkg upgrade
```

```bash
pkg install git python
```

```bash
git clone https://github.com/Berachain1/discord-auto-chat.git
cd discord-auto-chat
```

### 🛠️ Step 2: Setup Python & install dependencies

```bash
python3 -m venv venv
```

```bash
source venv/bin/activate
```

```bash
pip install -r requirements.txt
```

If you encounter an error about `pyfiglet`, install it manually:

```bash
pip install pyfiglet
```

### 🚀 Step 3: Run the script

```bash
python annisa.py
```

---

## 📋 Usage Instructions

1. **Add your Discord tokens** to a file named `token.txt` (1 token per line):

```
TOKEN1  
TOKEN2
```

2. **Run the script** and follow the prompts:

   * Enter channel ID
   * Number of messages to send
   * Delay between messages (recommended: 10 seconds)

---

## 🔑 How to Get Your Discord Token

⚠️ Use at your own risk — self-bots are against Discord's TOS.

1. Open Discord in a browser
2. Press `F12` to open Developer Tools
3. Go to the **Network** tab
4. Look for a request with `authorization` in the headers
5. Copy your token from there

---

## 📺 How to Get Channel ID

1. Open your Discord settings
2. Enable **Developer Mode**
3. Right-click on the desired channel
4. Click **"Copy ID"**

---

## ⚠️ Warning

> Using self-bots violates Discord's Terms of Service. Use this script at your own risk.

* I take no responsibility for any account bans or misuse.
* By using this script, **you agree** to take full responsibility.
* Use it wisely and ethically.

---

## 🧠 Troubleshooting

* ❌ **Invalid Token**: Replace the token with an active one in `token.txt`
* ⚠️ **Rate Limited**: The script will automatically wait
* ⏱️ **Timeout or Slowmode**: Will be detected and handled
* 🔐 **Permission Issues**: Make sure the token has permission to send/delete messages
* 🔇 **Voice Channel?**: The script will notify you

---

## 💡 Tips for Safe Use

* Always use a delay of **10 seconds or more** between messages
* Use an **alt account**, not your main account
* Do not spam too much in one server

---

## 🙏 Support Me

If you like this script and want to support its development:

**💸 Tip me (EVM Address):**
`0x47e33cec17c1faec718481ef5937d24f9318c031`

Thank you so much for your support! ❤️

