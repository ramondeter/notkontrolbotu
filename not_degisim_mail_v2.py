import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import requests
import time
import json
import os

# Ayarlar
LOGIN_URL = "https://unisis.uludag.edu.tr/"
NOTLAR_URL = "https://unisis.uludag.edu.tr/api/OgrenciEkranlarApi/OgrenciAktifSinavSonuclari?bireyID=514984&birimID=254"
KULLANICI_ADI = "032020584"
SIFRE = "Ali123Al;"
EMAIL_GONDEREN = "ramonmailgenerator@gmail.com"
EMAIL_ALICI = "ramonmailgenerator@gmail.com"
EMAIL_SIFRE = "5D6A69C935A068EE12CA70E0FE0F20890B4A"  # Elastic Email şifreniz

# E-posta gönderme fonksiyonu
def mail_gonder(degisenler):
    konu = "Yeni Not Girişi"
    mesaj = (degisenler+"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n Bu kısmı dikkate almayınız. \n")
    msg = MIMEMultipart()
    msg["From"] = EMAIL_GONDEREN
    msg["To"] = EMAIL_ALICI
    msg["Subject"] = konu
    msg.attach(MIMEText(mesaj, "plain", "utf-8"))  # UTF-8 ile encode et

    # SMTP sunucu ayarları
    smtp_server = "smtp.elasticemail.com"
    smtp_port = 2525  # Elastic Email için port
    sender_email = EMAIL_GONDEREN
    receiver_email = EMAIL_ALICI

    # SSL/TLS bağlantısını başlat
    context = ssl.create_default_context()

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls(context=context)  # TLS bağlantısını başlat
            server.login(sender_email, EMAIL_SIFRE)  # SMTP şifresi ile giriş yap
            server.sendmail(sender_email, receiver_email, msg.as_string())  # E-posta gönder
        print("E-posta başarıyla gönderildi.")
    except Exception as e:
        print(f"E-posta gönderimi sırasında bir hata oluştu: {e}")
def test_mail():
    konu = "Sistem açıldı ve çalışıyor"
    mesaj = "Sistem açıldı ve düzgün bir şekilde çalışıyor.\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n Bu kısmı dikkate almayınız. \n"

    msg = MIMEMultipart()
    msg["From"] = EMAIL_GONDEREN
    msg["To"] = EMAIL_ALICI
    msg["Subject"] = konu

    msg.attach(MIMEText(mesaj, "plain", "utf-8"))  # UTF-8 ile encode et

    # SMTP sunucu ayarları
    smtp_server = "smtp.elasticemail.com"
    smtp_port = 2525  # Elastic Email için port
    sender_email = EMAIL_GONDEREN
    receiver_email = EMAIL_ALICI

    # SSL/TLS bağlantısını başlat
    context = ssl.create_default_context()

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls(context=context)  # TLS bağlantısını başlat
            server.login(sender_email, EMAIL_SIFRE)  # SMTP şifresi ile giriş yap
            server.sendmail(sender_email, receiver_email, msg.as_string())  # E-posta gönder
        print("Sistem açıldı ve düzgün bir şekilde çalışıyor.")
    except Exception as e:
        print(f"Test e-postası gönderilemedi: {e}")
def notlari_cek():
    with requests.Session() as session:
        import urllib3
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

        # Giriş yap
        login_data = {"name": KULLANICI_ADI, "password": SIFRE}
        session.post(LOGIN_URL, data=login_data, verify=False)

        # Notları çek
        response = session.get(NOTLAR_URL, verify=False)
        return response.json()  # JSON verisi olarak döndür
def veriyi_stringe_donustur(veri):
    # JSON verisini formatlayarak string oluşturma
    sinav_adi = veri.get("SinavAdi", "Bilinmiyor")
    tarih = veri.get("Tarih", "Bilinmiyor")
    sinav_tipi = veri.get("SinavTipi", "Bilinmiyor")
    sinav_notu = veri.get("SinavNotu", "Bilinmiyor")
    sinav_ortalama = veri.get("SinavOrtalama", "Bilinmiyor")

    return f"SinavAdi: {sinav_adi}\nTarih: {tarih}\nSinavTipi: {sinav_tipi}\nSinavNotu: {sinav_notu}\nSinavOrtalama: {sinav_ortalama}"
def veriyi_dosyaya_kaydet(veri):
    with open("sinav_verisi.json", "w", encoding="utf-8") as f:
        json.dump(veri, f, ensure_ascii=False, indent=4)
def dosyadan_veri_oku():
    # Dosya yoksa, oluştur ve ardından oku
    if not os.path.exists("sinav_verisi.json"):
        veri = {"data": []}
        with open("sinav_verisi.json", "w", encoding="utf-8") as f:
            json.dump(veri, f, ensure_ascii=False, indent=4)
    
    # Dosya varsa ya da oluşturulduysa, veriyi oku
    with open("sinav_verisi.json", "r", encoding="utf-8") as f:
        try:
            veri = json.load(f)
            # Eğer veri anlamlı değilse, içeriği "data": [] olarak değiştir
            if not isinstance(veri, dict) or "data" not in veri or not isinstance(veri["data"], list):
                veri = {"data": []}
        except json.JSONDecodeError:
            # Eğer JSON formatında geçerli bir veri yoksa, içeriği sıfırla
            veri = {"data": []}

    # Güncel veya sıfırlanmış veriyi dosyaya geri yaz
    with open("sinav_verisi.json", "w", encoding="utf-8") as f:
        json.dump(veri, f, ensure_ascii=False, indent=4)

    return veri

def main():
    test_mail()
    while True:
        # Dosyadaki eski verileri oku
        eski_veri = dosyadan_veri_oku()  
        # Veriyi çek
        print("Veri okunuyor.")
        veri = notlari_cek()
        # Yeni sınavları kontrol et
        yeni_sinavlar = []
        for sinav in veri["data"]:
            sinav_id = sinav.get("SinavID")
            if sinav_id not in [eski_sinav.get("SinavID") for eski_sinav in eski_veri["data"]]:
                # Yeni sınav bulunduysa, veriyi stringe dönüştür
                print("Değişiklik tespit edildi")
                sinav_bilgisi = veriyi_stringe_donustur(sinav)
                print("Mail Gönderliyor..\n\nİçerik:")
                print(sinav_bilgisi)
                mail_gonder(sinav_bilgisi)
                # Yeni sınavları sakla
                yeni_sinavlar.append(sinav)
                print("\nVeritabanına kaydediliyor.\n")
            else:
                print("Değişiklik Yok.\n")
        # Eğer yeni sınav varsa, dosyayı güncelle
        if yeni_sinavlar:
            eski_veri["data"].extend(yeni_sinavlar)
            veriyi_dosyaya_kaydet(eski_veri)  # Yeni veriyi dosyaya kaydet

        # 1 dakika bekle
        time.sleep(60)

if __name__ == "__main__":
    main()
