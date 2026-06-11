Markdown
# TERMUX DISCORD SUNUCU KOPYALAMA REHBERİ

Bu rehberdeki komutları Termux ekranına sırasıyla kopyalayıp yapıştırarak kurulumu tamamlayabilirsiniz.

---

## 🛠️ 1. ADIM: TERMUX KURULUM KOMUTLARI (CMD EKRANINA SIRAYLA YAZIN)

Termux'u açın ve aşağıdaki komutları tek tek yapıştırıp Enter'a basın:

```bash
pkg update && pkg upgrade -y
(Ekranda soru çıkarsa y yazıp enterlayın)

Bash
pkg install python nano -y
Bash
pip install discord.py==1.7.3
📝 2. ADIM: SCRIPT DOSYASINI OLUŞTURMA
Şimdi bot kodunu yazacağımız dosyayı açıyoruz:

Bash
nano bot.py
Bu komutu yazınca karşınıza boş bir siyah ekran gelecek. Aşağıdaki Python kodunun tamamını kopyalayın ve Termux ekranına yapıştırın:
