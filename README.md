# BeatClashBot
A Discord bot for epic DJ battles with smack talk, random tracks, and voting!

## Setup
1. Install Python 3.8+ (https://www.python.org/downloads/).
2. Install dependencies: `pip install -r requirements.txt`.
3. Create a Discord bot and get its token:
   - Go to https://discord.com/developers/applications.
   - New Application > Name it "BeatClashBot" > Bot > Add Bot > Copy Token.
   - Invite it to your server: OAuth2 > URL Generator > Scope: `bot`, Permissions: `Send Messages`, `Connect`, `Speak`, `Add Reactions`.
4. Edit `config.py` and replace "YOUR_TOKEN_HERE" with your bot token.
5. Add at least 3 MP3 files to the `music/` folder.
6. Run the bot: `python main.py`.

## Commands
- `!dj_battle [theme]` - Start a battle with an optional theme (e.g., `!dj_battle epic`).
- `!skip` - Skip the current track (within 10 seconds).
- `!boo` - -2 hype to the current DJ.
- `!stats` - Show win stats.
- `!history` - See last 5 battles.
- `!rematch` - Replay the last battle.
- `!help` - Display this help message.
- Hype: 🔥 (+2), 👍 (+1), 👎 (-1) in chat or reactions.

## Features
- 6 DJs battle with 25 unique smack-talk lines.
- Random tracks from your `music/` folder.
- Vote with 🟥, 🟦, 🟩—hype boosts the score!
- Bold smack talk, underlined song titles, bold+underlined winners.

## Support
Love BeatClash? Toss a coin to the creator:

- Dogecoin (DOGE): DLemAFGPYEdSPxMAnc2k9zc8WKvxo7i71i 

## License
MIT License - Free to use, modify, and share. Give a shoutout if you dig it!