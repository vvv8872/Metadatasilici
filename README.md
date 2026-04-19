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

```bash
pip install rich Pillow mutagen pikepdf python-docx
```

Tüm kütüphaneleri kurmak zorunda değilsiniz. Sadece kullanacağınız formata ait olanı kurmanız yeterlidir. `rich` kütüphanesi zorunludur, diğerleri isteğe bağlıdır.

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

**`git` veya `python` tanınmıyor hatası**
Programı yükledikten sonra terminali kapatıp yeniden açın.

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
