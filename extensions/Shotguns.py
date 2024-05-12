import lightbulb
import hikari

plugin = lightbulb.Plugin('shotguns')

@plugin.command
@lightbulb.command('shotgun', 'parent command for AR gun challenges')
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def my_group7(ctx):
    pass

@my_group7.child
@lightbulb.command('lockwood300', 'Lockwood 300 challenges')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def embed_command(ctx: lightbulb.Context) -> None:
    embed = hikari.Embed(title="__Lockwood 300__", description="   ", color=0x89CFF0)
    embed.add_field("__Base Camos__", "1 (lvl 2): Get 40 kills\n\n2 (lvl 10): Get 40 kills using a suppressor\n\n3 (lvl 19): Get 25 one-shot kills\n\n4 (lvl 27): Get 20 kills while mounted")
    embed.set_thumbnail("https://www.pcgamesn.com/wp-content/sites/pcgamesn/2022/11/mw2-lockwood-loadout-550x309.jpg")
    embed.set_footer("")
    await ctx.respond(embed)  # or respond(embed=embed)

@my_group7.child
@lightbulb.command('expedite12', 'Expedite 12 challenges')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def embed_command(ctx: lightbulb.Context) -> None:
    embed = hikari.Embed(title="__Expedite 12__", description="   ", color=0x89CFF0)
    embed.add_field("__Base Camos__", "1 (lvl 2): Get 40 kills\n\n2 (lvl 11): Get 15 hip fire kills\n\n3 (lvl 20): Get 30 kills while aiming down sights\n\n4 (lvl 29): Get 25 kills while prone")
    embed.set_thumbnail("https://www.pcgamesn.com/wp-content/sites/pcgamesn/2022/11/expedition-550x309.jpg")
    embed.set_footer("")
    await ctx.respond(embed)  # or respond(embed=embed)

@my_group7.child
@lightbulb.command('bryson800', 'Bryson 800 challenges')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def embed_command(ctx: lightbulb.Context) -> None:
    embed = hikari.Embed(title="__Bryson 800__", description="   ", color=0x89CFF0)
    embed.add_field("__Base Camos__", "1 (lvl 2): Get 40 kills\n\n2 (lvl 8): Get 15 hip fire kills\n\n3 (lvl 14): Get 10 double kills\n\n4 (lvl 20): Get 20 one-shot kills")
    embed.set_thumbnail("https://charlieintel.com/wp-content/uploads/2022/11/best-modern-warfare-2-bryson-800-loadout-attachments-perks.jpg")
    embed.set_footer("")
    await ctx.respond(embed)  # or respond(embed=embed)

@my_group7.child
@lightbulb.command('bryson890', 'Bryson 890 challenges')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def embed_command(ctx: lightbulb.Context) -> None:
    embed = hikari.Embed(title="__Bryson 890__", description="   ", color=0x89CFF0)
    embed.add_field("__Base Camos__", "1 (lvl 2): Get 40 kills\n\n2 (lvl 8): Get 15 point blank kills\n\n3 (lvl 14): Get 10 double kills\n\n4 (lvl 21): Get 25 kills while crouched")
    embed.set_thumbnail("https://hungrygeeks.com.ph/wp-content/uploads/2022/11/Modern-Warfare-2-Bryson-890-Cover.jpg")
    embed.set_footer("")
    await ctx.respond(embed)  # or respond(embed=embed)

def load(bot):
    bot.add_plugin(plugin)