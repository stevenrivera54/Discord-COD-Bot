import lightbulb
import hikari

plugin = lightbulb.Plugin('ars')

@plugin.command
@lightbulb.command('ar', 'parent command for AR gun challenges')
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def my_group(ctx):
    pass

#---------------------------------------------------------------- ARS --------------------------------------------------------------------------

@my_group.child
@lightbulb.command('m4', 'M4 challenges')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def embed_command(ctx: lightbulb.Context) -> None:
    embed = hikari.Embed(title="__M4__", description="   ", color=0x89CFF0)
    embed.add_field("__Base Camos__", "1 (Lvl 2): Get 50 kills\n\n2 (Lvl 8): Get 50 kills while aiming down sights\n\n3 (Lvl 13): Get 10 double kills\n\n4 (Lvl 19): Get 15 kills from behind")
    embed.set_thumbnail("https://www.theloadout.com/wp-content/sites/theloadout/2022/09/call-of-duty-modern-warfare-2-m4-loadout-550x309.jpg")
    embed.set_footer("")
    await ctx.respond(embed)  # or respond(embed=embed)

@my_group.child
@lightbulb.command('taq56', 'Taq-56 challenges')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def embed_command(ctx: lightbulb.Context) -> None:
    embed = hikari.Embed(title="__Taq-56__", description="   ", color=0x89CFF0)
    embed.add_field("__Base Camos__", "1 (Lvl 2): Get 50 kills\n\n2 (Lvl 8): Get 10 double kills\n\n3 (Lvl 13): Get 50 kills while aiming down sights\n\n4 (Lvl 19): Get 15 hip fire kills")
    embed.set_thumbnail("https://www.theloadout.com/wp-content/sites/theloadout/2022/10/call-of-duty-modern-warfare-2-taq-56-loadout-550x309.jpg")
    embed.set_footer("")
    await ctx.respond(embed)  # or respond(embed=embed)

@my_group.child
@lightbulb.command('kastov762', 'Kastov 762 challenges')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def embed_command(ctx: lightbulb.Context) -> None:
    embed = hikari.Embed(title="__Kastov 762__", description="   ", color=0x89CFF0)
    embed.add_field("__Base Camos__", "1 (Lvl 2): Get 50 kills\n\n2 (Lvl 8): Get 20 while mounted\n\n3 (Lvl 14): Get 50 kills while aiming down sights\n\n4 (Lvl 20): Get 15 kills from behind")
    embed.set_thumbnail("https://www.theloadout.com/wp-content/sites/theloadout/2022/10/call-of-duty-modern-warfare-2kastov-762-loadout-1-550x309.jpg")
    embed.set_footer("")
    await ctx.respond(embed)  # or respond(embed=embed)

@my_group.child
@lightbulb.command('lachmann556', 'Lachmann 556 challenges')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def embed_command(ctx: lightbulb.Context) -> None:
    embed = hikari.Embed(title="__Lachmann 556__", description="   ", color=0x89CFF0)
    embed.add_field("__Base Camos__", "1 (Lvl 2): Get 50 kills\n\n2 (Lvl 8): Get 10 double kills\n\n3 (Lvl 14): Get 50 kills using a suppressor\n\n4 (Lvl 19): Get 10 hip fire kills")
    embed.set_thumbnail("https://charlieintel.com/wp-content/uploads/2022/11/best-modern-warfare-2-lachmann-556-loadout-attachments-perks.jpg")
    embed.set_footer("")
    await ctx.respond(embed)  # or respond(embed=embed)

@my_group.child
@lightbulb.command('stb556', 'STB 556 challenges')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def embed_command(ctx: lightbulb.Context) -> None:
    embed = hikari.Embed(title="__STB 556__", description="   ", color=0x89CFF0)
    embed.add_field("__Base Camos__", "1 (Lvl 2): Get 50 kills\n\n2 (Lvl 8): Get 20 kills while mounted\n\n3 (Lvl 14): Get 10 double kills\n\n4 (Lvl 20): Get 30 kills while crouched")
    embed.set_thumbnail("https://www.theloadout.com/wp-content/sites/theloadout/2022/10/call-of-duty-modern-warfare-2-stb-556-loadout-1-550x309.jpg")
    embed.set_footer("")
    await ctx.respond(embed)  # or respond(embed=embed)

@my_group.child
@lightbulb.command('m16', 'M16 challenges')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def embed_command(ctx: lightbulb.Context) -> None:
    embed = hikari.Embed(title="__M16__", description="   ", color=0x89CFF0)
    embed.add_field("__Base Camos__", "1 (Lvl 2): Get 50 kills\n\n2 (Lvl 6): Get 10 double kills\n\n3 (Lvl 11): Get 30 kills while crouched\n\n4 (Lvl 15): Get 20 kills while mounted")
    embed.set_thumbnail("https://www.pcgamesn.com/wp-content/sites/pcgamesn/2022/10/call-of-duty-modern-warfare-2-best-m16-loadout-550x309.jpg")
    embed.set_footer("")
    await ctx.respond(embed)  # or respond(embed=embed)

@my_group.child
@lightbulb.command('kastov74u', 'Kastov-74u challenges')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def embed_command(ctx: lightbulb.Context) -> None:
    embed = hikari.Embed(title="__Kastov-74u__", description="   ", color=0x89CFF0)
    embed.add_field("__Base Camos__", "1 (Lvl 2): Get 50 kills\n\n2 (Lvl 8): Get 15 point-blank kills\n\n3 (Lvl 14): Get 10 double kills\n\n4 (Lvl 20): Get 30 kills while crouched")
    embed.set_thumbnail("https://charlieintel.com/wp-content/uploads/2022/09/Best-KASTOV-74u-Modern-Warfare-2-loadout.jpg")
    embed.set_footer("")
    await ctx.respond(embed)  # or respond(embed=embed)@my_group.child

@my_group.child
@lightbulb.command('kastov545', 'Kastov 545 challenges')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def embed_command(ctx: lightbulb.Context) -> None:
    embed = hikari.Embed(title="__Kastov 545__", description="   ", color=0x89CFF0)
    embed.add_field("__Base Camos__", "1 (Lvl 2): Get 50 kills\n\n2 (Lvl 7): Get 10 hip fire kills\n\n3 (Lvl 13): Get 50 kills while aiming down sights\n\n4 (Lvl 18): Get 50 kills with a suppressor")
    embed.set_thumbnail("https://charlieintel.com/wp-content/uploads/2022/11/best-modern-warfare-2-kastov-545-loadout-attachments-perks.jpg")
    embed.set_footer("")
    await ctx.respond(embed)  # or respond(embed=embed)

def load(bot):
    bot.add_plugin(plugin)