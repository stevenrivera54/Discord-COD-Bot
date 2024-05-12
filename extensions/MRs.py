import lightbulb
import hikari

plugin = lightbulb.Plugin('mrs')

@plugin.command
@lightbulb.command('mr', 'parent command for AR gun challenges')
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def my_group5(ctx):
    pass

@my_group5.child
@lightbulb.command('ebr14', 'EBR-14 challenges')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def embed_command(ctx: lightbulb.Context) -> None:
    embed = hikari.Embed(title="__EBR-14__", description="   ", color=0x89CFF0)
    embed.add_field("__Base Camos__", "1 (lvl 2): Get 50 kills\n\n2 (lvl 6): Get 30 kills while crouched\n\n3 (lvl 10): Get 20 kills while mounted\n\n4 (lvl 14): Get 10 double kills")
    embed.set_thumbnail("https://www.theloadout.com/wp-content/sites/theloadout/2022/10/call-of-duty-modern-warfare-2-ebr-14-loadout-550x309.jpg")
    embed.set_footer("")
    await ctx.respond(embed)  # or respond(embed=embed)

@my_group5.child
@lightbulb.command('spr208', 'SP-R 208 challenges')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def embed_command(ctx: lightbulb.Context) -> None:
    embed = hikari.Embed(title="__SP-R 208__", description="   ", color=0x89CFF0)
    embed.add_field("__Base Camos__", "1 (lvl 2): Get 50 kills\n\n2 (lvl 6): Get 50 kills while aiming down sights\n\n3 (lvl 11): Get 30 kills while prone\n\n4 (lvl 14): Get 20 kills while mounted")
    embed.set_thumbnail("https://staticg.sportskeeda.com/editor/2022/10/c9da0-16671586675266-1920.jpg")
    embed.set_footer("")
    await ctx.respond(embed)  # or respond(embed=embed)

@my_group5.child
@lightbulb.command('lockwoodmk2', 'Lockwood MK2 challenges')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def embed_command(ctx: lightbulb.Context) -> None:
    embed = hikari.Embed(title="__Lockwood MK2__", description="   ", color=0x89CFF0)
    embed.add_field("__Base Camos__", "1 (lvl 2): Get 50 kills\n\n2 (lvl 11): Get 15 kills from behind\n\n3 (lvl 19): Get 25 one-shot kills\n\n4 (lvl 28): Get 10 point-blank kills")
    embed.set_thumbnail("https://cdn-ggbgl.nitrocdn.com/BxNnyXQaRWZsvraElQmsbEFLGomRULSs/assets/static/optimized/rev-28048fd/wp-content/uploads/Modern-Warfare-2-Lockwood-MK2-Header.jpg")
    embed.set_footer("")
    await ctx.respond(embed)  # or respond(embed=embed)

@my_group5.child
@lightbulb.command('lms', 'LM-S challenges')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def embed_command(ctx: lightbulb.Context) -> None:
    embed = hikari.Embed(title="__LM-S__", description="   ", color=0x89CFF0)
    embed.add_field("__Base Camos__", "1 (lvl 2): Get 50 kills\n\n2 (lvl 5): Get 20 kills while mounted\n\n3 (lvl 9): Get 20 one-shot kills\n\n4 (lvl 12): Get 30 kills while crouched")
    embed.set_thumbnail("https://www.gamesatlas.com/images/cod-modern-warfare-2/weapons/lm-s-0.jpg")
    embed.set_footer("")
    await ctx.respond(embed)  # or respond(embed=embed)

@my_group5.child
@lightbulb.command('sab50', 'SA-B 50 challenges')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def embed_command(ctx: lightbulb.Context) -> None:
    embed = hikari.Embed(title="__SA-B 50__", description="   ", color=0x89CFF0)
    embed.add_field("__Base Camos__", "1 (lvl 2): Get 50 kills\n\n2 (lvl 8): Get 25 one-shot kills\n\n3 (lvl 14): Get 10 double kills\n\n4 (lvl 20): Get 10 kills while mounted")
    embed.set_thumbnail("https://charlieintel.com/wp-content/uploads/2022/11/modern-warfare-2-sa-b-50-loadout-e1667922975237.png")
    embed.set_footer("")
    await ctx.respond(embed)  # or respond(embed=embed)

@my_group5.child
@lightbulb.command('taqm', 'TAQ-M challenges')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def embed_command(ctx: lightbulb.Context) -> None:
    embed = hikari.Embed(title="__TAQ-M__", description="   ", color=0x89CFF0)
    embed.add_field("__Base Camos__", "1 (lvl 2): Get 50 kills\n\n2 (lvl 10): Get 25 kills while mounted \n\n3 (lvl 17): Get 5 hip fire kills\n\n4 (lvl 25): Get 10 double kills")
    embed.set_thumbnail("https://www.pcgamesn.com/wp-content/sites/pcgamesn/2022/11/taq-m-550x309.jpg")
    embed.set_footer("")
    await ctx.respond(embed)  # or respond(embed=embed)

def load(bot):
    bot.add_plugin(plugin)