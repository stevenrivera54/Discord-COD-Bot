import lightbulb
import hikari

plugin = lightbulb.Plugin('srs')

@plugin.command
@lightbulb.command('sr', 'parent command for SR gun challenges')
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def my_group9(ctx):
    pass

@my_group9.child
@lightbulb.command('mcpr300', 'MCPR-300 challenges')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def embed_command(ctx: lightbulb.Context) -> None:
    embed = hikari.Embed(title="__MCPR-300__", description="   ", color=0x89CFF0)
    embed.add_field("__Base Camos__", "1 (lvl 2): Get 50 kills\n\n2 (lvl 10): Get 2 kills within 10 seconds of each other 10 times\n\n3 (lvl 18): Get 30 kills while prone\n\n4 (lvl 26): Get 10 hip fire kills")
    embed.set_thumbnail("https://www.pcgamesn.com/wp-content/sites/pcgamesn/2022/11/modern-warfare-2-mcpr-300-550x309.jpg")
    embed.set_footer("")
    await ctx.respond(embed)  # or respond(embed=embed)

@my_group9.child
@lightbulb.command('signal50', 'Signal 50 challenges')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def embed_command(ctx: lightbulb.Context) -> None:
    embed = hikari.Embed(title="__Signal 50__", description="   ", color=0x89CFF0)
    embed.add_field("__Base Camos__", "1 (lvl 2): Get 50 kills\n\n2 (lvl 9): Get 2 kills within 10 seconds of each other 10 times\n\n3 (lvl 16): Get 30 kills while prone\n\n4 (lvl 23): Get 25 one-shot kills")
    embed.set_thumbnail("https://www.pcgamesn.com/wp-content/sites/pcgamesn/2022/11/modern-warfare-2-best-signal-50-loadout-550x309.jpg")
    embed.set_footer("")
    await ctx.respond(embed)  # or respond(embed=embed)

@my_group9.child
@lightbulb.command('lab330', 'LA-B 330 challenges')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def embed_command(ctx: lightbulb.Context) -> None:
    embed = hikari.Embed(title="__LA-B 330__", description="   ", color=0x89CFF0)
    embed.add_field("__Base Camos__", "1 (lvl 2): Get 50 kills\n\n2 (lvl 8): Get 2 kills within 10 seconds of each other 10 times\n\n3 (lvl 15): Get 25 one-shot kills\n\n4 (lvl 21): Get 50 kills with a suppressor")
    embed.set_thumbnail("https://charlieintel.com/wp-content/uploads/2022/11/best-modern-warfare-2-la-b-330-loadout-attachments-perks.jpg")
    embed.set_footer("")
    await ctx.respond(embed)  # or respond(embed=embed)

@my_group9.child
@lightbulb.command('spx80', 'SP-X 80 challenges')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def embed_command(ctx: lightbulb.Context) -> None:
    embed = hikari.Embed(title="__SP-X 80__", description="   ", color=0x89CFF0)
    embed.add_field("__Base Camos__", "1 (lvl 2): Get 50 kills\n\n2 (lvl 7): Get 20 kills while mounted \n\n3 (lvl 13): Get 25 one-shot kills\n\n4 (lvl 18): Get 50 kills with a suppressor")
    embed.set_thumbnail("https://charlieintel.com/wp-content/uploads/2022/11/modern-warfare-2-sp-x-80.jpg")
    embed.set_footer("")
    await ctx.respond(embed)  # or respond(embed=embed)

def load(bot):
    bot.add_plugin(plugin)