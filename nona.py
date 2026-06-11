import discord
from discord.ext import commands

TOKEN = "BURAYA_HESAP_TOKENİNİZİ_YAZIN"
KOPYALANACAK_ID =     # Kopyalanacak Sunucu ID
YAPISTIRILACAK_ID =   # Yapıştırılacak Sunucu ID

bot = commands.Bot(command_prefix="!", self_bot=True)

@bot.event
async def on_ready():
    print(f"[{bot.user}] Olarak Giriş Yapıldı!")
    
    kaynak = bot.get_guild(KOPYALANACAK_ID)
    hedef = bot.get_guild(YAPISTIRILACAK_ID)
    
    if not kaynak or not hedef:
        print("Hata: Sunucu ID'leri yanlış veya hesap bu sunucularda yok!")
        return

    print(f"'{kaynak.name}' sunucusu '{hedef.name}' sunucusuna aktarılıyor...")

    for kanal in hedef.channels:
        try: await kanal.delete()
        except: pass

    # Rolleri Kopyala
    for rol in reversed(kaynak.roles):
        if rol.is_default(): continue
        try:
            await hedef.create_role(name=rol.name, permissions=rol.permissions, color=rol.color)
            print(f"Rol Kopyalandı: {rol.name}")
        except: pass

    # Kategorileri ve Kanalları Kopyala
    for kategori in kaynak.categories:
        yeni_kategori = await hedef.create_category(name=kategori.name)
        for kanal in kategori.channels:
            if isinstance(kanal, discord.TextChannel):
                await hedef.create_text_channel(name=kanal.name, category=yeni_kategori)
            elif isinstance(kanal, discord.VoiceChannel):
                await hedef.create_voice_channel(name=kanal.name, category=yeni_kategori)
        print(f"Kategori ve Kanalları Kopyalandı: {kategori.name}")

    print("\n[+] Kopyalama işlemi başarıyla tamamlandı!")
    print("Enes tarafından yapılmıştır.")
    await bot.close()

bot.run(TOKEN, bot=False)
