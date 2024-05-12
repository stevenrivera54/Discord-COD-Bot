import lightbulb
import hikari

plugin = lightbulb.Plugin('smgs')

@plugin.command
@lightbulb.command('smg', 'parent command for AR gun challenges')
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def my_group8(ctx):
    pass

@my_group8.child
@lightbulb.command('vel46', 'VEL 46 challenges')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def embed_command(ctx: lightbulb.Context) -> None:
    embed = hikari.Embed(title="__VEL 46__", description="   ", color=0x89CFF0)
    embed.add_field("__Base Camos__", "1 (lvl 2): Get 50 kills\n\n2 (lvl 11): Get 50 kills while aiming down sights\n\n3 (lvl 19): Get 15 hip fire kills\n\n4 (lvl 28): Get 10 double kills")
    embed.set_thumbnail("https://www.theloadout.com/wp-content/sites/theloadout/2022/10/call-of-duty-modern-warfare-2-vel-46-loadout-550x309.jpg")
    embed.set_footer("")
    await ctx.respond(embed)  # or respond(embed=embed)

@my_group8.child
@lightbulb.command('mx9', 'MX9 challenges')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def embed_command(ctx: lightbulb.Context) -> None:
    embed = hikari.Embed(title="__MX9__", description="   ", color=0x89CFF0)
    embed.add_field("__Base Camos__", "1 (lvl 2): Get 50 kills\n\n2 (lvl 7): Get 10 double kills\n\n3 (lvl 11): Get 20 kills while mounted\n\n4 (lvl 16): Get 30 kills while crouched")
    embed.set_thumbnail("https://www.pcgamesn.com/wp-content/sites/pcgamesn/2022/11/modern-warfare-2-best-mx9-loadout-550x309.jpg")
    embed.set_footer("")
    await ctx.respond(embed)  # or respond(embed=embed)

@my_group8.child
@lightbulb.command('lachmannsub', 'Lachmann Sub challenges')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def embed_command(ctx: lightbulb.Context) -> None:
    embed = hikari.Embed(title="__Lachmann Sub__", description="   ", color=0x89CFF0)
    embed.add_field("__Base Camos__", "1 (lvl 2): Get 50 kills\n\n2 (lvl 7): Get 10 double kills\n\n3 (lvl 13): Get 50 Kills using a suppressor\n\n4 (lvl 18): Get 10 hip fire kills")
    embed.set_thumbnail("https://thenerdstash.com/wp-content/uploads/2022/10/Lachmann-Sub-MP5-in-Modern-Warfare-2.jpg.webp")
    embed.set_footer("")
    await ctx.respond(embed)  # or respond(embed=embed)

@my_group8.child
@lightbulb.command('vaznev9k', 'Vaznev-9K challenges')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def embed_command(ctx: lightbulb.Context) -> None:
    embed = hikari.Embed(title="__Vaznev-9K__", description="   ", color=0x89CFF0)
    embed.add_field("__Base Camos__", "1 (lvl 2): Get 50 kills\n\n2 (lvl 6): Get 50 kills while aiming down sights\n\n3 (lvl 9): Get 10 double kills\n\n4 (lvl 13): Get 15 hip fire kills")
    embed.set_thumbnail("https://www.pcgamesn.com/wp-content/sites/pcgamesn/2022/11/modern-warfare-2-vaznev-9k-loadout-best-550x309.jpg")
    embed.set_footer("")
    await ctx.respond(embed)  # or respond(embed=embed)

@my_group8.child
@lightbulb.command('fsshurricane', 'FSS Hurricane challenges')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def embed_command(ctx: lightbulb.Context) -> None:
    embed = hikari.Embed(title="__FSS Hurricane__", description="   ", color=0x89CFF0)
    embed.add_field("__Base Camos__", "1 (lvl 2): Get 50 kills\n\n2 (lvl 6): Get 50 kills with a suppressor\n\n3 (lvl 10): Get 50 kills while aiming down sights\n\n4 (lvl 14): Get 30 kills while prone")
    embed.set_thumbnail("https://www.theloadout.com/wp-content/sites/theloadout/2022/09/call-of-duty-modern-warfare-2-fss-hurricane-loadout-550x309.jpg")
    embed.set_footer("")
    await ctx.respond(embed)  # or respond(embed=embed)

@my_group8.child
@lightbulb.command('minibak', 'Minibak challenges')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def embed_command(ctx: lightbulb.Context) -> None:
    embed = hikari.Embed(title="__Minibak__", description="   ", color=0x89CFF0)
    embed.add_field("__Base Camos__", "1 (lvl 2): Get 50 kills\n\n2 (lvl 6): Get 10 double kills\n\n3 (lvl 10): Get 50 kills while aiming down sights\n\n4 (lvl 14): Get 15 point-blank kills")
    embed.set_thumbnail("https://charlieintel.com/wp-content/uploads/2022/11/Best-Minibak-loadout-in-Modern-Warfare-2.jpg")
    embed.set_footer("")
    await ctx.respond(embed)  # or respond(embed=embed)

@my_group8.child
@lightbulb.command('pdsw528', 'PDSW 528 challenges')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def embed_command(ctx: lightbulb.Context) -> None:
    embed = hikari.Embed(title="__PDSW 528__", description="   ", color=0x89CFF0)
    embed.add_field("__Base Camos__", "1 (lvl 2): Get 50 kills\n\n2 (lvl 11): Get 50 kills while aiming down sights\n\n3 (lvl 20): Get 15 hip fire kills\n\n4 (lvl 29): Get 10 point-blank kills")
    embed.set_thumbnail("https://www.theloadout.com/wp-content/sites/theloadout/2022/10/modern-warfare-2-pdsw-528-loadout-550x309.jpg")
    embed.set_footer("")
    await ctx.respond(embed)  # or respond(embed=embed)

@my_group8.child
@lightbulb.command('fennec45', 'Fennec 45 challenges')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def embed_command(ctx: lightbulb.Context) -> None:
    embed = hikari.Embed(title="__Fennec 45__", description="   ", color=0x89CFF0)
    embed.add_field("__Base Camos__", "1 (lvl 2): Get 50 kills\n\n2 (lvl 10): Get 30 kills while crouched\n\n3 (lvl 18): Get 15 kills from behind\n\n4 (lvl 26): Get 10 double kills")
    embed.set_thumbnail("https://www.pcgamesn.com/wp-content/sites/pcgamesn/2022/11/warzone-2-fennec-45-loadout-550x309.jpg")
    embed.set_footer("")
    await ctx.respond(embed)  # or respond(embed=embed)

def load(bot):
    bot.add_plugin(plugin)