# 🔒 Metadata Silici

```
  ███╗   ███╗███████╗████████╗ █████╗ ██████╗  █████╗ ████████╗ █████╗ 
  ████╗ ████║██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗
  ██╔████╔██║█████╗     ██║   ███████║██║  ██║███████║   ██║   ███████║
  ██║╚██╔╝██║██╔══╝     ██║   ██╔══██║██║  ██║██╔══██║   ██║   ██╔══██║
  ██║ ╚═╝ ██║███████╗   ██║   ██║  ██║██████╔╝██║  ██║   ██║   ██║  ██║
  ╚═╝     ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝
```

> Terminal tabanlı ASCII arayüzüyle dosyalarınızdaki gizli metadata'yı temizleyin.

---

## 📋 İçindekiler

- [Nedir?](#-nedir)
- [Neden Kullanmalıyım?](#-neden-kullanmalıyım)
- [Özellikler](#-özellikler)
- [Desteklenen Formatlar](#-desteklenen-formatlar)
- [Kurulum](#-kurulum)
- [Kullanım](#-kullanım)
- [Ekran Görüntüsü](#-ekran-görüntüsü)
- [Nasıl Çalışır?](#-nasıl-çalışır)
- [Güvenlik](#-güvenlik)
- [Sorun Giderme](#-sorun-giderme)

---

## 🔍 Nedir?

**Metadata Silici**, fotoğraflarınızda, ses dosyalarınızda, PDF'lerinizde ve Word belgelerinizde saklanan gizli bilgileri (metadata) temizleyen bir komut satırı aracıdır. Tamamen Python ile yazılmıştır ve `rich` kütüphanesiyle güzel bir terminal arayüzüne sahiptir.

---

## 🎯 Neden Kullanmalıyım?

Dosya paylaşırken farkında olmadan **çok fazla kişisel bilgi** paylaşıyor olabilirsiniz:

| Dosya Türü | Saklanan Gizli Bilgiler |
|------------|------------------------|
| 📸 Fotoğraf (JPG/PNG) | GPS konumu, kamera modeli, çekim tarihi/saati, işletim sistemi |
| 🎵 Müzik (MP3/FLAC) | Albüm bilgisi, yorum, kullanıcı adı, yazılım adı |
| 📄 PDF | Yazar adı, şirket adı, oluşturma yazılımı, düzenleme geçmişi |
| 📝 Word (DOCX) | Yazar, son düzenleyen, gizli yorumlar, revizyon geçmişi |

---

## ✨ Özellikler

- 🖥️ **Sade terminal arayüzü** — `rich` tabanlı renkli ASCII tasarım
- 🔍 **Metadata önizleme** — silmeden önce nelerin temizleneceğini görün
- 💾 **Otomatik yedekleme** — orijinal dosya `_yedek` eki ile saklanır
- ⚡ **3 mod** — sadece görüntüle / sadece sil / hızlı (görüntüle+sil)
- 🧩 **Modüler yapı** — eksik kütüphane varsa yalnızca o format devre dışı kalır
- ✅ **Onay ekranı** — yanlışlıkla silmeyi önlemek için onay sorusu

---

## 📁 Desteklenen Formatlar

### 🖼️ Resim — EXIF Metadata (Pillow)
```
.jpg  .jpeg  .png  .tiff  .tif  .bmp  .webp  .gif
```
GPS koordinatları, kamera bilgisi, lens ayarları, tarih/saat ve tüm EXIF alanları temizlenir.

### 🎵 Ses — ID3 / Tag Metadata (mutagen)
```
.mp3  .flac  .ogg  .m4a  .wav  .aac  .wma  .opus
```
Albüm kapağı, şarkı sözleri, yorumlar ve tüm ID3 tag'leri temizlenir.

### 📄 PDF — Belge Metadata (pikepdf)
```
.pdf
```
Yazar, başlık, konu, anahtar kelimeler, oluşturma yazılımı ve XMP metadata temizlenir.

### 📝 Word — Çekirdek Özellikler (python-docx)
```
.docx
```
Yazar, son düzenleyen, başlık, konu, açıklama, etiketler ve revizyon sayısı temizlenir.

---

## 🚀 Kurulum

### 1. Depoyu klonlayın

```bash
git clone https://github.com/kullanici/metadata-silici.git
cd metadata-silici
```

### 2. Bağımlılıkları yükleyin

**Tüm özellikleri aktif etmek için (önerilen):**
```bash
pip install rich Pillow mutagen pikepdf python-docx
```

**Sadece belirli formatlar için:**
```bash
pip install rich          # Zorunlu — arayüz için
pip install Pillow        # Resim desteği için
pip install mutagen       # Ses desteği için
pip install pikepdf       # PDF desteği için
pip install python-docx   # DOCX desteği için
```

> **Not:** `rich` kütüphanesi zorunludur. Diğerleri isteğe bağlıdır; kurulmayan kütüphanenin formatı devre dışı kalır ama uygulama çalışmaya devam eder.

### 3. Python sürümü

Python **3.10 veya üzeri** gereklidir (`match` ifadesi ve `tuple[...]` tip ipuçları kullanılmaktadır).

```bash
python --version   # 3.10+ olmalı
```

---

## 💻 Kullanım

### Uygulamayı başlatın

```bash
python metadata_silici.py
```

### Menü seçenekleri

```
┌─────────────────────────────────────────┐
│  [1]  Dosya Seç ve Metadata Görüntüle  │
│  [2]  Metadata Sil                      │
│  [3]  Görüntüle + Sil  (Hızlı)         │
│  [q]  Çıkış                             │
└─────────────────────────────────────────┘
```

| Seçenek | Açıklama |
|---------|----------|
| `1` | Dosyayı seçip metadata'sını tablo olarak görüntüler, **silmez** |
| `2` | Metadata'yı doğrudan siler, önce onay alır |
| `3` | Önce görüntüler, ardından onay alarak siler |
| `q` | Uygulamadan çıkar |

### Dosya yolu girişi

```
  Yol > /home/kullanici/Masaustu/tatil_fotografi.jpg
```

- Tam yol (absolute path) girilmelidir
- Yolu tırnak içinde de yazabilirsiniz: `"/home/user/dosya adı var.jpg"`
- `q` yazarak menüye dönebilirsiniz

---

## 🖥️ Ekran Görüntüsü

```
╔══════════════════════════════════════════════════════════════════╗
║  ██████  ██ ██      ██  ██████ ██                               ║
║  ██      ██ ██      ██ ██      ██                               ║
║  ███████ ██ ██      ██ ██      ██                               ║
║  ██      ██ ██      ██ ██      ██                               ║
║  ███████ ██ ███████ ██  ██████ ██  v1.0                        ║
╚══════════════════════════════════════════════════════════════════╝

  Dosyalarınızdan EXIF · ID3 · PDF · DOCX meta verilerini temizleyin

  ● Kütüphane Durumu
  ┃ Kütüphane    ┃     Durum      ┃ Desteklenen Formatlar         ┃
  ┃ Pillow       ┃  ✔  Yüklü     ┃ JPG PNG TIFF BMP WEBP GIF     ┃
  ┃ mutagen      ┃  ✔  Yüklü     ┃ MP3 FLAC OGG M4A WAV AAC WMA  ┃
  ┃ pikepdf      ┃  ✘  Eksik     ┃ PDF                            ┃
  ┃ python-docx  ┃  ✔  Yüklü     ┃ DOCX                           ┃

  ──────────────────────── MENÜ ─────────────────────────
  [1]   Dosya Seç ve Metadata Görüntüle
  [2]   Metadata Sil
  [3]   Görüntüle + Sil  (Hızlı)
  [q]   Çıkış
  Seçim:
```

---

## ⚙️ Nasıl Çalışır?

### Resimler (Pillow)
Görseli piksel piksel okuyarak yeni bir görüntü oluşturur. Bu süreçte EXIF bloğu dahil hiçbir metadata yeni dosyaya aktarılmaz. Görüntü kalitesi korunur.

### Ses Dosyaları (mutagen)
`mutagen` kütüphanesinin `delete()` metodu ile dosyanın tüm tag bölümü kaldırılır. Ses verisi bütünüyle korunur.

### PDF (pikepdf)
`open_metadata()` ile XMP metadata bloğu temizlenir, `docinfo` sözlüğü sıfırlanır. PDF içeriği ve yapısı değişmez.

### DOCX (python-docx)
`core_properties` nesnesi üzerinden yazar, başlık, konu, etiketler ve benzeri alanlar boşaltılır. Belgenin metin ve biçimlendirmesi bozulmaz.

---

## 🛡️ Güvenlik

- **Orijinal dosya asla silinmez.** Her işlem öncesinde dosyanın yanına `_yedek` uzantılı bir kopya oluşturulur.
  ```
  tatil.jpg  →  tatil_yedek.jpg  (orijinal)
                tatil.jpg        (metadata temizlenmiş)
  ```
- Silme işlemi **yalnızca onaydan sonra** gerçekleşir.
- Uygulama internet bağlantısı gerektirmez; tüm işlemler **yerel olarak** yapılır.
- Üçüncü taraflara herhangi bir veri gönderilmez.

---

## 🔧 Sorun Giderme

### `rich` bulunamadı
```bash
pip install rich
```

### Belirli bir format çalışmıyor
Uygulama açılışında kütüphane durumu tablosunu kontrol edin. Eksik kütüphaneyi kurun:
```bash
pip install Pillow        # Resim için
pip install mutagen       # Ses için
pip install pikepdf       # PDF için
pip install python-docx   # DOCX için
```

### `python: command not found`
Sisteminize göre `python3` komutunu deneyin:
```bash
python3 metadata_silici.py
```

### Python sürümü eski
```bash
python --version   # 3.10 altında ise güncelleyin
```

### Dosya bulunamadı hatası
- Yolu tam olarak girin (örn: `/home/kullanici/Belgeler/dosya.jpg`)
- Dosya adında boşluk varsa tırnak kullanın: `"/home/user/tatil foto.jpg"`
- Windows'ta ters eğik çizgi yerine düz eğik çizgi kullanabilirsiniz

### pikepdf kurulum hatası (Linux)
```bash
sudo apt install libqpdf-dev   # Debian/Ubuntu
pip install pikepdf
```

---

## 📦 Bağımlılıklar

| Kütüphane | Sürüm | Kullanım | PyPI |
|-----------|-------|----------|------|
| `rich` | ≥ 13.0 | Terminal arayüzü (zorunlu) | [pypi.org/project/rich](https://pypi.org/project/rich/) |
| `Pillow` | ≥ 10.0 | Resim EXIF temizleme | [pypi.org/project/Pillow](https://pypi.org/project/Pillow/) |
| `mutagen` | ≥ 1.47 | Ses tag temizleme | [pypi.org/project/mutagen](https://pypi.org/project/mutagen/) |
| `pikepdf` | ≥ 8.0 | PDF metadata temizleme | [pypi.org/project/pikepdf](https://pypi.org/project/pikepdf/) |
| `python-docx` | ≥ 1.1 | DOCX metadata temizleme | [pypi.org/project/python-docx](https://pypi.org/project/python-docx/) |

---

## 📄 Lisans

MIT License — dilediğiniz gibi kullanabilir, değiştirebilir ve dağıtabilirsiniz.

---

<div align="center">
  <sub>Python 3.10+ · Terminal ASCII UI · Yerel & Güvenli</sub>
</div>
#   M e t a d a t a s i l i c i  
 