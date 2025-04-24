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

```
git clone https://github.com/sgtflixy/basic-discord-bot.git
cd basic-discord-bot
```

### 2. Install dependencies
```pip install -r requirements.txt```

### 3. Set up your bot token

Replace `BOT_TOKEN` in `bot.py` with your actual token,
or use environment variables for safer deployment (do this yourself lol)

## 📦 Requirements
```
Python 3.8+
py-cord==2.4.1
```
See `requirements.txt` for details.

## 🔒 Permissions

This bot uses role-based permissions to ensure only users with the right Discord permissions can run moderation commands like ban, kick, and clear.
## 📄 License

MIT License — feel free to fork, edit, and build on it.
Credit appreciated if you use parts of this project.

