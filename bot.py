import hikari
import lightbulb

bot = lightbulb.BotApp(
    token='MTAzOTg2ODMwNjk4MDYyMjM0Ng.GIxGxd.ghOBxxEY2JwqwLWCoB_lP3mbo8Ma8c_cDVGUDU',
    default_enabled_guilds=(1039867077181313046, 964608981194637345, 681175403913805855)
)


bot.load_extensions_from('./extensions')

@bot.command
@lightbulb.command('ping', 'says pong!')
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx):
    await ctx.respond('Pong!')

@bot.command
@lightbulb.command('allguns', 'shows a list of all weapons and their slash command names')
@lightbulb.implements(lightbulb.SlashCommand)
async def embed_command(ctx: lightbulb.Context) -> None:
    embed = hikari.Embed(title="Weapons List", description="A list of all weapons and their respective slash command names.", color=0xFFA500)
    embed.add_field("__Assault Rifles__   (/ar)", " - Kastov 545\n  - Kastov 762\n  - Kastov-74U\n  - Lachmann-556\n  - M16\n  - M4\n  - STB 556\n  - TAQ-56\n ")
    embed.add_field("__Battle Rifles__   (/br)", " - FTAC Recon\n  - Lachmann-762\n  - SO-14\n  - TAQ-V\n ")
    embed.add_field("__SMGs__   (/smg)", "  - BAS-P\n  - Fennec 45\n  - FSS Hurricane\n  - Lachmann Sub\n  - MINIBAK\n  - MX9\n  - PDSW-528\n  - Vaznev-9K\n  - VEL 46\n ")
    embed.add_field("__Shotguns__   (/shotgun)", " - Bryson 800\n  - Bryson 890\n  - Expedite 12\n  - Lockwood 300\n ")
    embed.add_field("__LMGs__   (/lmg)", " - 556 Icarus\n  - HCR 56\n  - RAAL MG\n  - RAPP H\n  - RPK\n  - Sakin MG38\n ")
    embed.add_field("__Marksman Rifles__   (/mr)", " - EBR-14\n  - LM-S\n  - Lockwood MK2\n  - SA-B 50\n  - SP-R 208\n  - TAQ-M\n ")
    embed.add_field("__Snipers__   (/sr)", " - LA-B 330\n  - MCPR-300\n  - SP-X 80\n  - Signal 50\n ")
    embed.add_field("__Pistols__   (/pistol)", " - 50 GS\n  - Basilisk\n  - P890\n  - X12\n  - X13 Auto\n ")
    embed.add_field("__Launchers__   (/launcher)", " - JOKR\n  - PILA\n  - RPG-7\n  - Strela-P\n ")
    embed.add_field("__Melees__   (/melee)", " - Combat Knife\n  - Riot Shield\n ")
    embed.set_footer("Note: All gun names in commands are absent of spaces, special characters, and capital letters.")
    await ctx.respond(embed)  # or respond(embed=embed)



#@bot.command
#@lightbulb.option('gun', 'Gun wished to get challenges for',type=str)
#@lightbulb.command('chal', 'Get challenges for a gun')
#@lightbulb.implements(lightbulb.SlashCommand)
#async def chal(ctx):
#    if(ctx.options.gun=="x12"):
#        await ctx.respond('1: Get 30 kills\n\n2: Get 25 kills while aiming down sights\n\n3: Get 10 hip fire kills\n\n4: Get 40 kills while akimbo')

bot.run()