# 🛡️ Pycord Moderation & Fun Bot

A basic but functional Discord bot built with **[Pycord](https://docs.pycord.dev)**.  
Includes moderation tools and a few fun commands!

> ⚙️ Bot created by [sgtflixy](https://bot.infiltra.xyz)  
> This is a minimal version of my main bot.

---

## ✨ Features

### 🔧 Moderation
- `/kick [member] [reason]` — Kick a user from the server.
- `/ban [member] [reason]` — Ban a user from the server.
- `/clear [amount]` — Bulk delete messages in a channel.

### 🎉 Fun
- `/ping` — Check the bot's latency.
- `/coinflip` — Flip a coin: Heads or Tails?
- `/roll` — Roll a six-sided dice.
- `/say [message]` — Make the bot say something.

---

## 🚀 Getting Started

### 1. Clone the repo

```git clone https://github.com/yourusername/yourbot.git
cd yourbot```

### 2. Install dependencies
`pip install -r requirements.txt`

### 3. Set up your bot token

Replace `BOT_TOKEN` in `bot.py` with your actual token,
or use environment variables for safer deployment (do this yourself lol)

## 📦 Requirements
`Python 3.8+`
`py-cord==2.4.1`
See `requirements.txt` for details.
