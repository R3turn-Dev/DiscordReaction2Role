from discord.ext.commands import AutoShardedBot as Bot


bot = Bot(command_prefix="e;r ")
bot.load_extension("cogs.reaction_role")

bot.run("")
