import lightbulb
import hikari

plugin = lightbulb.Plugin('pistols')

@plugin.command
@lightbulb.command('pistol', 'parent command for AR gun challenges')
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def my_group6(ctx):
    pass

@my_group6.child
@lightbulb.command('p890', 'P890 challenges')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def embed_command(ctx: lightbulb.Context) -> None:
    embed = hikari.Embed(title="__P890__", description="   ", color=0x89CFF0)
    embed.add_field("__Base Camos__", "1 (lvl 2): Get 40 kills\n\n2 (lvl 10): Get 40 kills with a suppressor \n\n3 (lvl 18): Get 5 double kills\n\n4 (lvl 26): Get 10 point-blank kills")
    embed.set_thumbnail("https://www.pcgamesn.com/wp-content/sites/pcgamesn/2022/11/Screenshot-2022-11-02-114122-550x309.jpg")
    embed.set_footer("")
    await ctx.respond(embed)  # or respond(embed=embed)

@my_group6.child
@lightbulb.command('50gs', '.50 GS challenges')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def embed_command(ctx: lightbulb.Context) -> None:
    embed = hikari.Embed(title="__.50 GS__", description="   ", color=0x89CFF0)
    embed.add_field("__Base Camos__", "1 (lvl 2): Get 40 kills\n\n2 (lvl 10): Get 5 double kills\n\n3 (lvl 18): Get 15 kills while mounted\n\n4 (lvl 26): Get 40 kills while akimbo")
    embed.set_thumbnail("https://hungrygeeks.com.ph/wp-content/uploads/2022/11/50GS-Cover.jpg")
    embed.set_footer("")
    await ctx.respond(embed)  # or respond(embed=embed)

"""
@my_group6.child
@lightbulb.command('p890', 'P890 challenges')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def subcommand(ctx):
    await ctx.respond('1 (lvl 2): Get 40 kills\n\n2 (lvl 10): Get 40 kills with a suppressor \n\n3 (lvl 18): Get 5 double kills\n\n4 (lvl 26): Get 10 point-blank kills')

@my_group6.child
@lightbulb.command('50gs', '.50 GS challenges')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def subcommand(ctx):
    await ctx.respond('1 (lvl 2): Get 40 kills\n\n2 (lvl 10): Get 5 double kills\n\n3 (lvl 18): Get 15 kills while mounted\n\n4 (lvl 26): Get 40 kills while akimbo')
"""

@my_group6.child
@lightbulb.command('x12', 'X12 challenges')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def embed_command(ctx: lightbulb.Context) -> None:
    embed = hikari.Embed(title="__X12__", description="   ", color=0x89CFF0)
    embed.add_field("__Base Camos__", "1 (lvl 2): Get 30 kills\n\n2 (lvl 8): Get 25 kills while aiming down sights\n\n3 (lvl 13): Get 10 hip fire kills\n\n4 (lvl 19): Get 40 kills while akimbo")
    embed.set_thumbnail("https://static.wikia.nocookie.net/callofduty/images/c/c9/X12_Gunsmith_MWII.png/revision/latest?cb=20220926032741")
    embed.set_footer("")
    await ctx.respond(embed)  # or respond(embed=embed)

@my_group6.child
@lightbulb.command('basilisk', 'Basilisk challenges')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def embed_command(ctx: lightbulb.Context) -> None:
    embed = hikari.Embed(title="__Basilisk__", description="   ", color=0x89CFF0)
    embed.add_field("__Base Camos__", "1 (lvl 2): Get 40 kills\n\n2 (lvl 11): Get 30 kills while aiming down sights \n\n3 (lvl 19): Get 10 point-blank kills\n\n4 (lvl 28): Get 30 kills while akimbo")
    embed.set_thumbnail("https://static.wikia.nocookie.net/callofduty/images/1/14/Basilisk_Gunsmith_MWII.png/revision/latest?cb=20221022081730")
    embed.set_footer("")
    await ctx.respond(embed)  # or respond(embed=embed)

@my_group6.child
@lightbulb.command('x13auto', 'X13 Auto challenges')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def embed_command(ctx: lightbulb.Context) -> None:
    embed = hikari.Embed(title="__X13 Auto__", description="   ", color=0x89CFF0)
    embed.add_field("__Base Camos__", "1 (lvl 2): Get 40 kills\n\n2 (lvl 8): Get 10 hipfire kills \n\n3 (lvl 15): Get 10 double kills\n\n4 (lvl 21): Get 40 kills while akimbo")
    embed.set_thumbnail("https://hungrygeeks.com.ph/wp-content/uploads/2022/11/XRK13-Cover.jpg")
    embed.set_footer("")
    await ctx.respond(embed)  # or respond(embed=embed)

def load(bot):
    bot.add_plugin(plugin)