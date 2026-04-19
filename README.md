# Metadata Silici

Fotoğraf, ses, PDF ve Word dosyalarındaki gizli bilgileri temizleyen terminal uygulaması.

---

## Metadata Nedir ve Neden Önemlidir?

Bir dosyayı paylaşırken içinde farkında olmadığınız bilgiler bulunabilir:

| Dosya Türü | Saklanan Gizli Bilgiler |
|------------|------------------------|
| Fotoğraf | GPS konumu, kamera modeli, çekim tarihi |
| Müzik | Kullanıcı adı, yorum, yazılım adı |
| PDF | Yazar adı, şirket, düzenleme geçmişi |
| Word | Yazar, son düzenleyen, gizli yorumlar |

Bu uygulama o bilgileri dosyadan temizler.

---

## Kurulum

Python 3.10 veya üzeri gereklidir.

### 1. Depoyu indirin

```bash
git clone https://github.com/vvv8872/Metadatasilici.git
cd Metadatasilici
```

### 2. Kütüphaneleri yükleyin

```bash
pip install -r requirements.txt
```

Tüm kütüphaneleri kurmak zorunda değilsiniz. Sadece kullanacağınız formata ait olanı kurmanız yeterlidir. `rich` kütüphanesi zorunludur, diğerleri isteğe bağlıdır.

**Tek tek kurmak isterseniz:**

```bash
pip install rich          # Zorunlu — arayüz için
pip install Pillow        # Resim desteği için
pip install mutagen       # Ses desteği için
pip install pikepdf       # PDF desteği için
pip install python-docx   # DOCX desteği için
```

---

## Kullanım

```bash
python metadata_silici.py
```

Uygulama açıldığında üç seçenek sunar:

- **1 — Görüntüle:** Dosyanın metadata bilgilerini listeler, silmez.
- **2 — Sil:** Metadata'yı siler, işlem öncesinde onay ister.
- **3 — Hızlı:** Önce gösterir, ardından onayınızla siler.

Dosya yolunu tam olarak girin. Örnek:

```
C:\Kullanicilar\Ali\Masaustu\fotograf.jpg
```

---

## Desteklenen Dosya Formatları

| Format | Uzantılar | Gerekli Kütüphane |
|--------|-----------|-------------------|
| Resim | .jpg .jpeg .png .tiff .bmp .webp .gif | Pillow |
| Ses | .mp3 .flac .ogg .m4a .wav .aac .wma | mutagen |
| PDF | .pdf | pikepdf |
| Word | .docx | python-docx |

---

## Güvenlik

- Silme işlemi öncesinde orijinal dosyanın yedeği otomatik alınır.
- Yedek dosya aynı klasöre `_yedek` ekiyle kaydedilir. Örnek: `fotograf_yedek.jpg`
- Uygulama internet bağlantısı kullanmaz, tüm işlemler bilgisayarınızda gerçekleşir.

---

## Sorun Giderme

**Belirli bir format çalışmıyor**
Uygulama açılışında kütüphane durumu tablosunu kontrol edin. Eksik olanı kurun:
```bash
pip install Pillow
pip install mutagen
pip install pikepdf
pip install python-docx
```

**Dosya bulunamadı hatası**
Dosya adında boşluk varsa yolu tırnak içine alın:
```
"C:\Kullanicilar\Ali\tatil foto.jpg"
```

**pikepdf kurulum hatası (Linux)**
```bash
sudo apt install libqpdf-dev
pip install pikepdf
```

---

## Gereksinimler

| Kütüphane | Sürüm |
|-----------|-------|
| rich | 13.0 ve üzeri |
| Pillow | 10.0 ve üzeri |
| mutagen | 1.47 ve üzeri |
| pikepdf | 8.0 ve üzeri |
| python-docx | 1.1 ve üzeri |

---

## Lisans

MIT — Serbestçe kullanabilir, değiştirebilir ve paylaşabilirsiniz.
