import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)
tree = bot.tree


language_regions = {
    "English": "Europe",
    "French": "Europe",
    "Russian": "Europe",
    "Spanish": "Europe",
    "Chinese": "Asia",
    "Japanese": "Asia",
    "Mongolian": "Asia",
    "Arabic": "Middle East",
    "Hebrew": "Middle East",
    "Swahili": "Africa",
    "Zulu": "Africa",
    "Esperanto": "Constructed/Other",
    "Cherokee": "Americas",
    "Hawaiian": "Oceania",
    # Add more here...
}

# Language list (ISO 639-1 + common names + emoji flags where possible)
languages = [
    ("English", "🇬🇧"),
    ("Chinese", "🇨🇳"),
    ("Mongolian", "🇲🇳"),
    ("Russian", "🇷🇺"),
    ("French", "🇫🇷"),
    ("German", "🇩🇪"),
    ("Spanish", "🇪🇸"),
    ("Portuguese", "🇵🇹"),
    ("Italian", "🇮🇹"),
    ("Arabic", "🇸🇦"),
    ("Japanese", "🇯🇵"),
    ("Korean", "🇰🇷"),
    ("Turkish", "🇹🇷"),
    ("Hindi", "🇮🇳"),
    ("Bengali", "🇧🇩"),
    ("Urdu", "🇵🇰"),
    ("Punjabi", "🇮🇳"),
    ("Persian", "🇮🇷"),
    ("Hebrew", "🇮🇱"),
    ("Thai", "🇹🇭"),
    ("Vietnamese", "🇻🇳"),
    ("Indonesian", "🇮🇩"),
    ("Malay", "🇲🇾"),
    ("Tagalog", "🇵🇭"),
    ("Cantonese", "🇭🇰"),
    ("Ukrainian", "🇺🇦"),
    ("Polish", "🇵🇱"),
    ("Romanian", "🇷🇴"),
    ("Hungarian", "🇭🇺"),
    ("Czech", "🇨🇿"),
    ("Slovak", "🇸🇰"),
    ("Swedish", "🇸🇪"),
    ("Finnish", "🇫🇮"),
    ("Norwegian", "🇳🇴"),
    ("Danish", "🇩🇰"),
    ("Dutch", "🇳🇱"),
    ("Greek", "🇬🇷"),
    ("Lithuanian", "🇱🇹"),
    ("Latvian", "🇱🇻"),
    ("Estonian", "🇪🇪"),
    ("Georgian", "🇬🇪"),
    ("Armenian", "🇦🇲"),
    ("Azerbaijani", "🇦🇿"),
    ("Kazakh", "🇰🇿"),
    ("Uzbek", "🇺🇿"),
    ("Tibetan", "🇨🇳"),
    ("Nepali", "🇳🇵"),
    ("Pashto", "🇦🇫"),
    ("Burmese", "🇲🇲"),
    ("Khmer", "🇰🇭"),
    ("Lao", "🇱🇦"),
    ("Sinhala", "🇱🇰"),
    ("Tamil", "🇮🇳"),
    ("Serbian", "🇷🇸"),
    ("Croatian", "🇭🇷"),
    ("Bosnian", "🇧🇦"),
    ("Albanian", "🇦🇱"),
    ("Macedonian", "🇲🇰"),
    ("Slovenian", "🇸🇮"),
    ("Bulgarian", "🇧🇬"),
    ("Basque", "🏴"),
    ("Galician", "🇪🇸"),
    ("Welsh", "🏴"),
    ("Irish", "🇮🇪"),
    ("Scottish Gaelic", "🏴"),
    ("Hawaiian", "🇺🇸"),
    ("Maori", "🇳🇿"),
    ("Samoan", "🇼🇸"),
    ("Tongan", "🇹🇴"),
    ("Zulu", "🇿🇦"),
    ("Swahili", "🇰🇪"),
    ("Hausa", "🇳🇬"),
    ("Amharic", "🇪🇹"),
    ("Yoruba", "🇳🇬"),
    ("Igbo", "🇳🇬"),
    ("Berber", "🏳️"),
    ("Somali", "🇸🇴"),
    ("Esperanto", "🟩"),
    ("Latin", "🏛️"),
    ("Sanskrit", "🕉️"),
    ("Tatar", "🇷🇺"),
    ("Chechen", "🇷🇺"),
    ("Ainu", "🇯🇵"),
    ("Nahuatl", "🇲🇽"),
    ("Quechua", "🇵🇪"),
    ("Guarani", "🇵🇾"),
    ("Māori", "🇳🇿"),
    ("Inuktitut", "🇨🇦"),
    ("Cherokee", "🏹"),
    ("Ojibwe", "🍁"),
    ("Maya", "🇲🇽"),
    ("Greenlandic", "🇬🇱"),
]

region_colors = {
    "Europe": discord.Color.blue(),
    "Asia": discord.Color.red(),
    "Africa": discord.Color.green(),
    "Middle East": discord.Color.orange(),
    "Americas": discord.Color.purple(),
    "Oceania": discord.Color.gold(),
    "Constructed/Other": discord.Color.teal()
}

language_regions = {
    # Europe
    "English": "Europe",
    "French": "Europe",
    "German": "Europe",
    "Spanish": "Europe",
    "Portuguese": "Europe",
    "Italian": "Europe",
    "Russian": "Europe",
    "Ukrainian": "Europe",
    "Polish": "Europe",
    "Romanian": "Europe",
    "Hungarian": "Europe",
    "Czech": "Europe",
    "Slovak": "Europe",
    "Swedish": "Europe",
    "Finnish": "Europe",
    "Norwegian": "Europe",
    "Danish": "Europe",
    "Dutch": "Europe",
    "Greek": "Europe",
    "Lithuanian": "Europe",
    "Latvian": "Europe",
    "Estonian": "Europe",
    "Serbian": "Europe",
    "Croatian": "Europe",
    "Bosnian": "Europe",
    "Albanian": "Europe",
    "Macedonian": "Europe",
    "Slovenian": "Europe",
    "Bulgarian": "Europe",
    "Basque": "Europe",
    "Galician": "Europe",
    "Welsh": "Europe",
    "Irish": "Europe",
    "Scottish Gaelic": "Europe",
    "Tatar": "Europe",
    "Chechen": "Europe",

    # Asia
    "Chinese": "Asia",
    "Mongolian": "Asia",
    "Japanese": "Asia",
    "Korean": "Asia",
    "Hindi": "Asia",
    "Bengali": "Asia",
    "Urdu": "Asia",
    "Punjabi": "Asia",
    "Thai": "Asia",
    "Vietnamese": "Asia",
    "Indonesian": "Asia",
    "Malay": "Asia",
    "Tagalog": "Asia",
    "Cantonese": "Asia",
    "Kazakh": "Asia",
    "Uzbek": "Asia",
    "Tibetan": "Asia",
    "Nepali": "Asia",
    "Pashto": "Asia",
    "Burmese": "Asia",
    "Khmer": "Asia",
    "Lao": "Asia",
    "Sinhala": "Asia",
    "Tamil": "Asia",
    "Ainu": "Asia",
    "Armenian": "Asia",
    "Azerbaijani": "Asia",
    "Georgian": "Asia",

    # Middle East
    "Arabic": "Middle East",
    "Hebrew": "Middle East",
    "Persian": "Middle East",

    # Africa
    "Swahili": "Africa",
    "Zulu": "Africa",
    "Hausa": "Africa",
    "Amharic": "Africa",
    "Yoruba": "Africa",
    "Igbo": "Africa",
    "Berber": "Africa",
    "Somali": "Africa",

    # Oceania
    "Hawaiian": "Oceania",
    "Maori": "Oceania",
    "Māori": "Oceania",  # Duplicate name with macron
    "Samoan": "Oceania",
    "Tongan": "Oceania",

    # Americas
    "Nahuatl": "Americas",
    "Quechua": "Americas",
    "Guarani": "Americas",
    "Cherokee": "Americas",
    "Ojibwe": "Americas",
    "Maya": "Americas",
    "Inuktitut": "Americas",
    "Greenlandic": "Americas",

    # Constructed / Other
    "Esperanto": "Constructed/Other",
    "Latin": "Constructed/Other",
    "Sanskrit": "Constructed/Other"
}

@bot.command()
async def addlang(ctx, language: str, emoji: str):
    if any(language == lang for lang, _ in languages):
        await ctx.send(f"⚠️ **{language}** is already supported. You don’t need to add it manually.")
        return

    guild = ctx.guild
    speaker_role = f"{emoji} {language} Speaker"
    learner_role = f"{emoji} {language} Learner"

    existing_roles = [role.name for role in guild.roles]
    if speaker_role in existing_roles or learner_role in existing_roles:
        await ctx.send(f"⚠️ Roles for **{language}** already exist.")
        return

    # Fallback region detection
    region = language_regions.get(language)
    if not region:
        lowered = language.lower()
        if any(x in lowered for x in ["chinese", "japanese", "thai", "korean", "tibetan", "sanskrit"]):
            region = "Asia"
        elif any(x in lowered for x in ["french", "german", "polish", "slovak", "gaelic", "russian"]):
            region = "Europe"
        elif any(x in lowered for x in ["swahili", "zulu", "yoruba"]):
            region = "Africa"
        elif any(x in lowered for x in ["arabic", "hebrew", "persian"]):
            region = "Middle East"
        elif any(x in lowered for x in ["nahuatl", "maya", "cherokee"]):
            region = "Americas"
        elif any(x in lowered for x in ["maori", "hawaiian", "tongan"]):
            region = "Oceania"
        else:
            region = "Constructed/Other"

    role_color = region_colors.get(region, discord.Color.teal())

    await guild.create_role(name=speaker_role, color=role_color)
    await guild.create_role(name=learner_role, color=role_color)

    await ctx.send(f"✅ Created roles for **{language}** under region **{region}**.")

@bot.event
async def on_member_join(member):
    unverified_role = discord.utils.get(member.guild.roles, name="Unverified")
    if unverified_role:
        await member.add_roles(unverified_role)
        try:
            await member.send("👋 Welcome! Please run `/set_languages` in presentations channel to unlock full access to the server.")
        except discord.Forbidden:
            pass

@bot.event
async def on_ready():
    if not hasattr(bot, 'synced'):
        bot.synced = True  # Mark that we've run this setup

        print(f"✅ Logged in as {bot.user}")
        for guild in bot.guilds:
            existing_roles = [role.name for role in guild.roles]

            for name, emoji in languages:
                speaker = f"{emoji} {name} Speaker"
                learner = f"{emoji} {name} Learner"

                if speaker not in existing_roles:
                    await guild.create_role(name=speaker)
                    print(f"Created role: {speaker}")
                if learner not in existing_roles:
                    await guild.create_role(name=learner)
                    print(f"Created role: {learner}")

class LanguageModal(discord.ui.Modal, title="🗣️ Set Your Languages"):

    native_languages = discord.ui.TextInput(
    label="Native languages (comma-separated)",
    placeholder="e.g., Mongolian, Chinese",
    style=discord.TextStyle.short,
    required=True,
    )

    learning_languages = discord.ui.TextInput(
        label="Learning/mastered languages",
        placeholder="e.g., English, Russian",
        style=discord.TextStyle.short,
        required=True,
    )

    async def on_submit(self, interaction: discord.Interaction):
        spoken = [lang.strip().title() for lang in self.native_languages.value.split(",")]
        learning = [lang.strip().title() for lang in self.learning_languages.value.split(",")]

        await assign_roles(interaction.guild, interaction.user, spoken, learning)
        # Remove 'Unverified' role once they've set their languages
        unverified_role = discord.utils.get(interaction.guild.roles, name="Unverified")
        if unverified_role in interaction.user.roles:
            await interaction.user.remove_roles(unverified_role)
        # Post public embed in #introductions or #presentations
        intro_channel = discord.utils.get(interaction.guild.text_channels, name="💞｜presentations")
        if intro_channel:
            embed = discord.Embed(
                title=f"👋 Welcome {interaction.user.display_name}!",
                description=f"🗣️ **Speaks:** {', '.join(spoken)}\n📚 **Learning:** {', '.join(learning)}",
                color=discord.Color.blurple()
            )
            if interaction.user.avatar:
                embed.set_thumbnail(url=interaction.user.avatar.url)
            await intro_channel.send(embed=embed)

        await interaction.response.send_message(
            "✅ All set! We've shared your languages in #presentations.",
            ephemeral=True
        )

@tree.command(name="set_languages", description="Choose the languages you speak and learn")
async def set_languages(interaction: discord.Interaction):
    if interaction.guild is None:
        await interaction.response.send_message(
            "❌ This command can only be used inside a server, not in DMs.",
            ephemeral=True
        )
        return

    await interaction.response.send_modal(LanguageModal())

async def assign_roles(guild, user, spoken, learning):
    for lang in spoken:
        await create_and_assign_role(guild, user, lang, "Speaker")

    for lang in learning:
        await create_and_assign_role(guild, user, lang, "Learner")

async def create_and_assign_role(guild, user, lang, role_type):  # role_type = "Speaker" or "Learner"
    # Get emoji from language list
    emoji = next((e for n, e in languages if n.lower() == lang.lower()), None)
    if not emoji:
        emoji = "🌐"  # fallback emoji

    role_name = f"{emoji} {lang} {role_type}"

    # Search for the correct role or legacy (emoji-less) role
    role = discord.utils.get(guild.roles, name=role_name)
    if not role:
        # Fallback: check for plain "lang role_type"
        fallback_name = f"{lang} {role_type}"
        fallback_role = discord.utils.get(guild.roles, name=fallback_name)
        if fallback_role:
            # Rename and recolor existing fallback role
            await fallback_role.edit(name=role_name)
            role = fallback_role
        else:
            # Create a fresh new role with correct color
            region = language_regions.get(lang, "Constructed/Other")
            color = region_colors.get(region, discord.Color.teal())
            role = await guild.create_role(name=role_name, color=color)

    # If role exists but has wrong color → fix it
    region = language_regions.get(lang, "Constructed/Other")
    desired_color = region_colors.get(region, discord.Color.teal())
    if role.color != desired_color:
        await role.edit(color=desired_color)

    await user.add_roles(role)


# bot.run("MTM3NTA3NjA0ODgzNTg0MjE2OA.Gf3xhB.yO9n72LtAMdxamkfxZUBBic-SyHh-DW7Jvj-p4")
bot.run(os.getenv("DISCORD_BOT_TOKEN"))