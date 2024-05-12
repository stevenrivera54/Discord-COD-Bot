import lightbulb
import hikari

plugin = lightbulb.Plugin('lmgs')

@plugin.command
@lightbulb.command('lmg', 'parent command for AR gun challenges')
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def my_group3(ctx):
    pass

@my_group3.child
@lightbulb.command('sakinmg38', 'SAKIN MG38 challenges')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def embed_command(ctx: lightbulb.Context) -> None:
    embed = hikari.Embed(title="__SAKIN MG38__", description="   ", color=0x89CFF0)
    embed.add_field("__Base Camos__", "1 (lvl 2): Get 50 kills\n\n2 (lvl 8): Get 30 kills while prone\n\n3 (lvl 13): Get 10 double kills\n\n4 (lvl 19): Get 50 kills with a suppressor")
    embed.set_thumbnail("https://static.wikia.nocookie.net/callofduty/images/c/c8/SAKIN_MG38_Gunsmith_MWII.png/revision/latest?cb=20220926032039")
    embed.set_footer("")
    await ctx.respond(embed)  # or respond(embed=embed)

@my_group3.child
@lightbulb.command('hcr56', 'HCR 56 challenges')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def embed_command(ctx: lightbulb.Context) -> None:
    embed = hikari.Embed(title="__HCR 56__", description="   ", color=0x89CFF0)
    embed.add_field("__Base Camos__", "1 (lvl 2): Get 50 kills\n\n2 (lvl 7): Get 50 kills while aiming down sights\n\n3 (lvl 13): Get 10 double kills\n\n4 (lvl 18): Get 20 kills while mounted")
    embed.set_thumbnail("https://charlieintel.com/wp-content/uploads/2022/11/best-hcr-56-loadout-modern-warfare-2-e1668010397538.jpg")
    embed.set_footer("")
    await ctx.respond(embed)  # or respond(embed=embed)

@my_group3.child
@lightbulb.command('556icarus', '556 Icarus challenges')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def embed_command(ctx: lightbulb.Context) -> None:
    embed = hikari.Embed(title="__556 Icarus__", description="   ", color=0x89CFF0)
    embed.add_field("__Base Camos__", "1 (lvl 2): Get 50 kills\n\n2 (lvl 6): Get 10 double kills\n\n3 (lvl 11): Get 20 kills while mounted\n\n4 (lvl 15): Get 30 kills while crouched")
    embed.set_thumbnail("https://www.pcgamesn.com/wp-content/sites/pcgamesn/2022/10/icarus-550x309.jpg")
    embed.set_footer("")
    await ctx.respond(embed)  # or respond(embed=embed)

@my_group3.child
@lightbulb.command('raalmg', 'RAAL MG challenges')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def embed_command(ctx: lightbulb.Context) -> None:
    embed = hikari.Embed(title="__RAAL MG__", description="   ", color=0x89CFF0)
    embed.add_field("__Base Camos__", "1 (lvl 2): Get 50 kills\n\n2 (lvl 10): Get 15 kills from behind\n\n3 (lvl 19): Get 20 kills while mounted\n\n4 (lvl 27): Get 10 hip fire kills")
    embed.set_thumbnail("https://charlieintel.com/wp-content/uploads/2022/11/modern-warfare-2-best-raal-mg-loadout-1-e1667576673820.jpg")
    embed.set_footer("")
    await ctx.respond(embed)  # or respond(embed=embed)

@my_group3.child
@lightbulb.command('rpk', 'RPK challenges')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def embed_command(ctx: lightbulb.Context) -> None:
    embed = hikari.Embed(title="__RPK__", description="   ", color=0x89CFF0)
    embed.add_field("__Base Camos__", "1 (lvl 2): Get 50 kills\n\n2 (lvl 7): Get 10 double kills\n\n3 (lvl 13): Get 50 kills with a suppressor\n\n4 (lvl 18): Get 20 kills while mounted")
    embed.set_thumbnail("https://charlieintel.com/wp-content/uploads/2022/11/modern-warfare-2-best-RPK-loadout-e1667854232663.jpg")
    embed.set_footer("")
    await ctx.respond(embed)  # or respond(embed=embed)@my_group3.child

@my_group3.child
@lightbulb.command('rapph', 'RAPP H challenges')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def embed_command(ctx: lightbulb.Context) -> None:
    embed = hikari.Embed(title="__RAPP H__", description="   ", color=0x89CFF0)
    embed.add_field("__Base Camos__", "1 (lvl 2): Get 50 kills\n\n2 (lvl 7): Get 10 point-blank kills\n\n3 (lvl 13): Get 20 kills while mounted\n\n4 (lvl 18): Get 50 kills while ADS")
    embed.set_thumbnail("https://www.pcgamesn.com/wp-content/sites/pcgamesn/2022/10/raal-550x309.jpg")
    embed.set_footer("")
    await ctx.respond(embed)  # or respond(embed=embed)

def load(bot):
    bot.add_plugin(plugin)