# BeatClashBot 🌶️
🎧 BeatClashBot 🔥 6 DJs roast 💬 25x, spin 🎵 tracks, & clash! 🎮 Vote 🟥🟦🟩, hype 🔥👍👎

## Download 📥
- Click the green "Code" button > "Download ZIP" 📦 on this page.
- Unzip to a folder (e.g., `C:\BeatClashBot`) & follow the steps! 🚀

## Setup (Windows) 🖥️
Tested on Windows—here’s how to get it bumping! 🎉

### 1. Install Python 🐍
- Grab Python 3.8+ from [python.org/downloads](https://www.python.org/downloads/).
- Run installer: Check "Add Python to PATH" ✅ > Install Now > Finish.
- Verify in Command Prompt (`cmd`): `python --version`
  - See `Python 3.x.x`? You’re golden! 🌟

### 2. Install Dependencies 📚
- In your bot folder: `cd C:\Path\To\BeatClashBot` then `pip install -r requirements.txt`
  - Gets `discord.py`—the bot’s backbone! 💪

### 3. Install FFmpeg 🔊
- For audio vibes:
  - Download from [ffmpeg.org/download.html](https://ffmpeg.org/download.html) (Windows build, e.g., gyan.dev).
  - Extract to `C:\ffmpeg`.
  - Add to PATH: Search "Edit system environment variables" > System variables > Path > Edit > New > `C:\ffmpeg\bin` > OK all.
- Verify: `ffmpeg -version`
  - Version pops up? Audio’s ready! 🎵

### 4. Install PyNaCl 🎙️
- Voice boost: `pip install PyNaCl`

### 5. Setup Bot Token 🤖
- Make a Discord bot:
  - [discord.com/developers/applications](https://discord.com/developers/applications) > New App > "BeatClashBot" > Bot > Add Bot > Copy Token.
  - Invite: OAuth2 > URL Generator > Scope: `bot`, Permissions: `Send Messages`, `Connect`, `Speak`, `Add Reactions` > Copy URL > Open in browser > Add to server.
- Edit `config.py`: Swap `YOUR_TOKEN_HERE` with your token ✂️.

### 6. Add Music 🎶
- Drop 3+ MP3s into `music/` (e.g., `track1.mp3`) 📂.

### 7. Run It! 🎉
- In Command Prompt: `python main.py`
- Bot’s live—type `!dj_battle` to jam! 🎤

## Commands 🎛️
- `!dj_battle [theme]` - Kick off a battle (e.g., `!dj_battle epic`) 🎵
- `!skip` - Ditch a track (10s window) ⏱️
- `!boo` - -2 hype 👎
- `!stats` - Win stats 📊
- `!history` - Last 5 battles 🕰️
- `!rematch` - Replay the last clash 🔄
- `!help` - This list ℹ️
- Hype: 🔥 (+2), 👍 (+1), 👎 (-1) in chat/reactions 🎉

## Features 🌟
- 6 DJs w/ 25 smack-talk lines 💬
- Random tracks from `music/` 🎵
- Vote 🟥🟦🟩—hype boosts scores! 🔥
- Bold roasts, underlined tracks, bold+underlined winners 🎤

## Support 💖
Love it? Toss a coin:
- Dogecoin (DOGE): `DLemAFGPYEdSPxMAnc2k9zc8WKvxo7i71i`

## License 📜
MIT - Free to use, mod, share. Shoutout if you vibe! ✌️
