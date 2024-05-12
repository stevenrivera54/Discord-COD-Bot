import lightbulb
import hikari

plugin = lightbulb.Plugin('launchers')

@plugin.command
@lightbulb.command('launcher', 'parent command for AR gun challenges')
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def my_group2(ctx):
    pass

@my_group2.child
@lightbulb.command('pila', 'PILA challenges')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def embed_command(ctx: lightbulb.Context) -> None:
    embed = hikari.Embed(title="__PILA__", description="   ", color=0x89CFF0)
    embed.add_field("__Base Camos__", "1 (lvl 11): Get 40 kills")
    embed.set_thumbnail("https://www.gamesatlas.com/images/cod-modern-warfare-2/weapons/pila.jpg")
    embed.set_footer("")
    await ctx.respond(embed)  # or respond(embed=embed)

@my_group2.child
@lightbulb.command('strelap', 'STRELA-P challenges')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def embed_command(ctx: lightbulb.Context) -> None:
    embed = hikari.Embed(title="__STRELA-P__", description="   ", color=0x89CFF0)
    embed.add_field("__Base Camos__", "1 (lvl 11): Get 40 kills")
    embed.set_thumbnail("https://www.gamesatlas.com/images/cod-modern-warfare-2/weapons/strela-p.jpg")
    embed.set_footer("")
    await ctx.respond(embed)  # or respond(embed=embed)

@my_group2.child
@lightbulb.command('jokr', 'JOKR challenges')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def embed_command(ctx: lightbulb.Context) -> None:
    embed = hikari.Embed(title="__JOKR__", description="   ", color=0x89CFF0)
    embed.add_field("__Base Camos__", "1 (lvl 11): Get 40 kills")
    embed.set_thumbnail("https://www.gamesatlas.com/images/cod-modern-warfare-2/weapons/jokr.jpg")
    embed.set_footer("")
    await ctx.respond(embed)  # or respond(embed=embed)

@my_group2.child
@lightbulb.command('rpg7', 'RPG-7 challenges')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def embed_command(ctx: lightbulb.Context) -> None:
    embed = hikari.Embed(title="__RPG-7__", description="   ", color=0x89CFF0)
    embed.add_field("__Base Camos__", "1 (lvl 11): Get 40 kills")
    embed.set_thumbnail("https://www.gamesatlas.com/images/cod-modern-warfare-2/weapons/rpg-7.jpg")
    embed.set_footer("")
    await ctx.respond(embed)  # or respond(embed=embed)

def load(bot):
    bot.add_plugin(plugin)