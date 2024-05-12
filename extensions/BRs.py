import lightbulb
import hikari

plugin = lightbulb.Plugin('brs')

@plugin.command
@lightbulb.command('br', 'parent command for AR gun challenges')
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def my_group1(ctx):
    pass


@my_group1.child
@lightbulb.command('lachmann762', 'Lachmann-762 challenges')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def embed_command(ctx: lightbulb.Context) -> None:
    embed = hikari.Embed(title="__Lachmann-762__", description="   ", color=0x89CFF0)
    embed.add_field("__Base Camos__", "1 (lvl 2): Get 50 kills\n\n2 (lvl 7): Get 50 kills while aiming down sights\n\n3 (lvl 13): Get 20 kills while mounted\n\n4 (lvl 18): Get 10 double kills")
    embed.set_thumbnail("https://www.pcgamesn.com/wp-content/sites/pcgamesn/2022/10/call-of-duty-modern-warfare-2-best-lachmann-762-loadout-550x309.jpg")
    embed.set_footer("")
    await ctx.respond(embed)  # or respond(embed=embed)

@my_group1.child
@lightbulb.command('so14', 'SO-14 challenges')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def embed_command(ctx: lightbulb.Context) -> None:
    embed = hikari.Embed(title="__SO-14__", description="   ", color=0x89CFF0)
    embed.add_field("__Base Camos__", "1 (lvl 2): Get 50 kills\n\n2 (lvl 8): Get 50 kills while aiming down sights\n\n3 (lvl 15): Get 10 double kills\n\n4 (lvl 21): Get 30 kills while prone")
    embed.set_thumbnail("https://hungrygeeks.com.ph/wp-content/uploads/2022/11/Modern-Warfare-2-SO-14.jpg")
    embed.set_footer("")
    await ctx.respond(embed)  # or respond(embed=embed)

@my_group1.child
@lightbulb.command('taqv', 'TAQ-V challenges')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def embed_command(ctx: lightbulb.Context) -> None:
    embed = hikari.Embed(title="__TAQ-V__", description="   ", color=0x89CFF0)
    embed.add_field("__Base Camos__", "1 (lvl 2): Get 50 kills\n\n2 (lvl 8): Get 15 point-blank kills\n\n3 (lvl 14): Get 15 kills from behind\n\n4 (lvl 20): Get 20 kills while mounted")
    embed.set_thumbnail("https://www.pcgamesn.com/wp-content/sites/pcgamesn/2022/11/best-taq-v-loadout-550x309.jpg")
    embed.set_footer("")
    await ctx.respond(embed)  # or respond(embed=embed)

@my_group1.child
@lightbulb.command('ftacrecon', 'FTAC Recon challenges')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def embed_command(ctx: lightbulb.Context) -> None:
    embed = hikari.Embed(title="__FTAC Recon__", description="   ", color=0x89CFF0)
    embed.add_field("__Base Camos__", "1 (lvl 2): Get 50 kills\n\n2 (lvl 9): Get 10 double kills\n\n3 (lvl 15): 50 kills using a suppressor\n\n4 (lvl 22): Get 30 kills while crouched")
    embed.set_thumbnail("https://www.theloadout.com/wp-content/sites/theloadout/2022/09/call-of-duty-modern-warfare-2-ftac-recon-battle-rifle-loadout-1-550x309.jpg")
    embed.set_footer("")
    await ctx.respond(embed)  # or respond(embed=embed)

def load(bot):
    bot.add_plugin(plugin)