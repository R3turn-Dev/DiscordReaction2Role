from discord.ext.commands import AutoShardedBot as Bot
import os


bot = Bot(command_prefix="e;r ")
bot.load_extension("cogs.reaction_role")

bot.run(os.environ["DISCORD_ACCESS_TOKEN"])
