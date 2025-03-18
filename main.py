import discord
from discord.ext import commands
import asyncio
import os
import random
from config import TOKEN  # Import token from config.py

intents = discord.Intents.default()
intents.voice_states = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)
bot.remove_command("help")  # Remove default help command

# DJs and stats
djs = ["DJ Neuralix", "DJ Synthra", "DJ Vortex", "DJ Blaze", "DJ Echo", "DJ Pulse"]
battle_stats = {dj: 0 for dj in djs}
battle_history = []
current_track = None
hype_counts = {}
skipped_djs = set()

# Taunts - 25 spicy lines
taunts = [
    "{dj}: {opp}’s beats are stuck in the last century!",
    "{dj}: Time to school {opp} in real rhythm!",
    "{dj}: {opp} can’t handle this fire—step off!",
    "{dj}: {opp}’s tracks are a snooze fest!",
    "{dj}: Watch {opp} crash and burn against my beats!",
    "{dj}: {opp}’s mixing is a straight-up disaster!",
    "{dj}: I’m dropping bombs, {opp}’s just dropping the ball!",
    "{dj}: {opp} thinks they’re hot—cool story, bro!",
    "{dj}: {opp}’s sound is weaker than a wet noodle!",
    "{dj}: I’m the king, {opp}’s just a court jester!",
    "{dj}: {opp}’s beats couldn’t hype a ghost town!",
    "{dj}: Time for {opp} to eat my dust—spin that!",
    "{dj}: {opp}’s tracks are pure elevator music!",
    "{dj}: {opp}’s got no flow, just a flatline!",
    "{dj}: I’m the storm, {opp}’s just a drizzle!",
    "{dj}: {opp}’s beats are trash—recycle bin’s that way!",
    "{dj}: {opp} can’t touch this—hands off the decks!",
    "{dj}: I’m spitting bars, {opp}’s just spitting garbage!",
    "{dj}: {opp}’s sound is a one-way ticket to snoozeville!",
    "{dj}: {opp}’s got no game—back to the kiddie pool!",
    "{dj}: I’m the maestro, {opp}’s just off-key noise!",
    "{dj}: {opp}’s beats are flatter than yesterday’s soda!",
    "{dj}: {opp}’s out of their league—stick to karaoke!",
    "{dj}: I’m the pulse, {opp}’s just a faint beep!",
    "{dj}: {opp}’s tracks are a remix of pure failure!"
]

@bot.event
async def on_ready():
    print(f"BeatClash online as {bot.user}")

@bot.command()
async def dj_battle(ctx, *, theme="classic"):
    global current_track, hype_counts, skipped_djs
    hype_counts = {dj: 0 for dj in djs}
    skipped_djs = set()
    
    music_folder = "music"
    if not os.path.exists(music_folder):
        await ctx.send("No 'music' folder found! Create one and add some MP3s.")
        return
    try:
        mp3_files = [f for f in os.listdir(music_folder) if f.endswith(".mp3")]
        if len(mp3_files) < 3:
            await ctx.send("Need at least 3 MP3s in the 'music' folder!")
            return
    except Exception as e:
        await ctx.send(f"Error reading music folder: {e}")
        return
    
    battle_djs = random.sample(djs, 3)
    tracks = random.sample(mp3_files, 3)
    
    await ctx.send(f"BeatClash: {', '.join(battle_djs)} - {theme} elimination showdown!")
    if not ctx.author.voice:
        await ctx.send("Yo, join a voice channel first!")
        return
    
    try:
        voice_channel = ctx.author.voice.channel
        vc = await voice_channel.connect()
    except Exception as e:
        await ctx.send(f"Failed to join voice channel: {e}")
        return
    
    await ctx.send("BeatClash is in the house - spinning soon...")

    # Play each DJ’s track
    for dj, track in zip(battle_djs, tracks):
        opp = random.choice([d for d in battle_djs if d != dj])
        taunt = random.choice(taunts).format(dj=dj, opp=opp)
        await ctx.send(f"**{taunt}**\n__{dj} drops {track}!__ (Type !skip in 10s, 🔥 [+2], 👍 [+1], 👎 [-1], !boo [-2] in chat or reactions)")
        current_track = dj
        try:
            vc.play(discord.FFmpegPCMAudio(os.path.join(music_folder, track)))
            await asyncio.sleep(10)
            if not vc.is_playing():
                await ctx.send(f"{dj} got skipped - weak vibes!")
                skipped_djs.add(dj)
            else:
                while vc.is_playing():
                    await asyncio.sleep(1)
        except Exception as e:
            await ctx.send(f"Error playing {track}: {e}")
            continue
    
    # Voting
    if vc.is_connected():
        vote_msg = await ctx.send(f"Vote for the champ: 🟥 {battle_djs[0]}, 🟦 {battle_djs[1]}, 🟩 {battle_djs[2]}! (20 seconds)")
        await vote_msg.add_reaction("🟥")
        await vote_msg.add_reaction("🟦")
        await vote_msg.add_reaction("🟩")
        await asyncio.sleep(20)
        
        try:
            vote_msg = await ctx.channel.fetch_message(vote_msg.id)
            votes = {
                battle_djs[0]: sum(r.count for r in vote_msg.reactions if str(r.emoji) == "🟥") - 1,
                battle_djs[1]: sum(r.count for r in vote_msg.reactions if str(r.emoji) == "🟦") - 1,
                battle_djs[2]: sum(r.count for r in vote_msg.reactions if str(r.emoji) == "🟩") - 1
            }
        except Exception as e:
            await ctx.send(f"Error counting votes: {e}")
            await vc.disconnect()
            return
        
        # Combine votes and hype, exclude skipped DJs
        final_scores = {}
        for dj in battle_djs:
            if dj not in skipped_djs:
                final_scores[dj] = votes[dj] + hype_counts[dj]
            else:
                final_scores[dj] = 0
        
        # Find winner
        if all(score == 0 for score in final_scores.values()):
            winner = "No champ - all skipped or no votes!"
            battle_stats["Ties"] = battle_stats.get("Ties", 0) + 1
        else:
            winner = max(final_scores, key=final_scores.get)
            battle_stats[winner] += 1
        
        score_text = "\n".join(f"{dj}: {votes[dj]} votes + {hype_counts[dj]} hype = {final_scores[dj]}" for dj in battle_djs)
        await ctx.send(f"**__Winner: {winner}__**\n{score_text}")
        battle_history.append({"djs": battle_djs, "tracks": tracks, "winner": winner, "theme": theme})
    
    if vc.is_connected():
        await vc.disconnect()

@bot.command()
async def skip(ctx):
    global current_track
    if not ctx.voice_client or not ctx.voice_client.is_playing():
        await ctx.send("Nothing’s playing to skip!")
        return
    if current_track:
        ctx.voice_client.stop()
        await ctx.send(f"{current_track} got skipped - weak vibes!")

@bot.command()
async def boo(ctx):
    global current_track
    if current_track and ctx.voice_client and ctx.voice_client.is_playing():
        hype_counts[current_track] -= 2
        await ctx.send(f"{current_track} got booed! -2 hype!")

@bot.command()
async def stats(ctx):
    stats_text = "BeatClash v1.0 Stats:\n" + "\n".join(f"{dj}: {battle_stats.get(dj, 0)} wins" for dj in djs) + f"\nTies: {battle_stats.get('Ties', 0)}\nSupport the creator: [Your Ko-Fi/PayPal link here]"
    await ctx.send(stats_text)

@bot.command()
async def history(ctx):
    if not battle_history:
        await ctx.send("No battles yet!")
        return
    history_text = "Recent Battles:\n" + "\n".join(
        f"{i+1}. {h['djs'][0]} vs {h['djs'][1]} vs {h['djs'][2]} ({h['theme']}) - Winner: {h['winner']}"
        for i, h in enumerate(battle_history[-5:])
    )
    await ctx.send(history_text)

@bot.command()
async def rematch(ctx):
    if not battle_history:
        await ctx.send("No battle to rematch!")
        return
    last_battle = battle_history[-1]
    await dj_battle(ctx, theme=f"Rematch: {last_battle['theme']}")

@bot.command()
async def help(ctx):
    help_text = (
        "BeatClash v1.0 Commands:\n"
        "- `!dj_battle [theme]` - Start a DJ battle (e.g., `!dj_battle epic`).\n"
        "- `!skip` - Skip the current track (first 10s).\n"
        "- `!boo` - -2 hype to the current DJ.\n"
        "- `!stats` - Show win stats.\n"
        "- `!history` - See last 5 battles.\n"
        "- `!rematch` - Replay the last battle.\n"
        "- `!help` - This list.\n"
        "- Hype: 🔥 (+2), 👍 (+1), 👎 (-1) in chat or reactions."
    )
    await ctx.send(help_text)

@bot.event
async def on_reaction_add(reaction, user):
    global current_track
    if user.bot or not current_track or reaction.message.author != bot.user:
        return
    if reaction.emoji == "🔥":
        hype_counts[current_track] += 2
        await reaction.message.channel.send(f"{current_track} got some 🔥 hype! +2")
    elif reaction.emoji == "👍":
        hype_counts[current_track] += 1
        await reaction.message.channel.send(f"{current_track} got a 👍! +1")
    elif reaction.emoji == "👎":
        hype_counts[current_track] -= 1
        await reaction.message.channel.send(f"{current_track} got a 👎! -1")

@bot.event
async def on_message(message):
    global current_track
    if message.author.bot:
        return
    await bot.process_commands(message)
    if current_track and message.content in ["🔥", "👍", "👎"]:
        if message.content == "🔥":
            hype_counts[current_track] += 2
            await message.channel.send(f"{current_track} got some 🔥 hype! +2")
        elif message.content == "👍":
            hype_counts[current_track] += 1
            await message.channel.send(f"{current_track} got a 👍! +1")
        elif message.content == "👎":
            hype_counts[current_track] -= 1
            await message.channel.send(f"{current_track} got a 👎! -1")

bot.run(TOKEN)