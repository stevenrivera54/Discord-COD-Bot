import lightbulb
import hikari

plugin = lightbulb.Plugin('melee')

@plugin.command
@lightbulb.command('melee', 'parent command for AR gun challenges')
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def my_group4(ctx):
    pass

@my_group4.child
@lightbulb.command('riotshield', 'Riot Shield challenges')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def embed_command(ctx: lightbulb.Context) -> None:
    embed = hikari.Embed(title="__Riot Shield__", description="   ", color=0x89CFF0)
    embed.add_field("__Base Camos__", "1 (lvl 11): Get 40 kills")
    embed.set_thumbnail("https://www.gamesatlas.com/images/cod-modern-warfare-2/weapons/riot-shield.jpg")
    embed.set_footer("")
    await ctx.respond(embed)  # or respond(embed=embed)

@my_group4.child
@lightbulb.command('combatknife', 'Combat Knife challenges')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def embed_command(ctx: lightbulb.Context) -> None:
    embed = hikari.Embed(title="__Combat Knife__", description="   ", color=0x89CFF0)
    embed.add_field("__Base Camos__", "1 (lvl 11): Get 50 kills")
    embed.set_thumbnail("https://www.gamesatlas.com/images/cod-modern-warfare-2/weapons/combat-knife-2.jpg")
    embed.set_footer("")
    await ctx.respond(embed)  # or respond(embed=embed)

def load(bot):
    bot.add_plugin(plugin)