#!/usr/bin/env python3
"""
Metadata Silici - Terminal ASCII Arayüz
Gerekli: pip install rich Pillow mutagen pikepdf python-docx
"""

import os
import sys
import shutil
import time
from datetime import datetime

try:
    from rich.console import Console
    from rich.panel import Panel
    from rich.table import Table
    from rich.text import Text
    from rich.prompt import Prompt, Confirm
    from rich.progress import Progress, SpinnerColumn, TextColumn
    from rich import box
except ImportError:
    print("Hata: 'rich' yüklü değil.  →  pip install rich")
    sys.exit(1)

try:
    from PIL import Image
    PIL_OK = True
except ImportError:
    PIL_OK = False

try:
    from mutagen import File as MutagenFile
    MUTAGEN_OK = True
except ImportError:
    MUTAGEN_OK = False

try:
    import pikepdf
    PIKEPDF_OK = True
except ImportError:
    PIKEPDF_OK = False

try:
    from docx import Document
    DOCX_OK = True
except ImportError:
    DOCX_OK = False

# ──────────────────────────────────────────────────────────────────────────────

console = Console()

RESIM_UZ = {".jpg", ".jpeg", ".png", ".tiff", ".tif", ".bmp", ".webp", ".gif"}
SES_UZ   = {".mp3", ".flac", ".ogg", ".m4a", ".wav", ".aac", ".wma", ".opus"}
PDF_UZ   = {".pdf"}
DOCX_UZ  = {".docx"}
TUM_UZ   = RESIM_UZ | SES_UZ | PDF_UZ | DOCX_UZ

BANNER = """\
  ███╗   ███╗███████╗████████╗ █████╗ ██████╗  █████╗ ████████╗ █████╗ 
  ████╗ ████║██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗
  ██╔████╔██║█████╗     ██║   ███████║██║  ██║███████║   ██║   ███████║
  ██║╚██╔╝██║██╔══╝     ██║   ██╔══██║██║  ██║██╔══██║   ██║   ██╔══██║
  ██║ ╚═╝ ██║███████╗   ██║   ██║  ██║██████╔╝██║  ██║   ██║   ██║  ██║
  ╚═╝     ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝
           ███████╗██╗██╗     ██╗ ██████╗██╗
           ██╔════╝██║██║     ██║██╔════╝██║
           ███████╗██║██║     ██║██║     ██║
           ╚════██║██║██║     ██║██║     ██║
           ███████║██║███████╗██║╚██████╗██║
           ╚══════╝╚═╝╚══════╝╚═╝ ╚═════╝╚═╝  v1.0\
"""

# ── Yardımcı ──────────────────────────────────────────────────────────────────

def temizle():
    os.system("cls" if os.name == "nt" else "clear")

def baslik_goster():
    temizle()
    console.print(Text(BANNER, style="bold cyan"))
    console.print(
        Panel(
            "[dim]Dosyalarınızdan EXIF · ID3 · PDF · DOCX meta verilerini güvenle silin[/dim]",
            border_style="cyan",
            box=box.DOUBLE_EDGE,
        )
    )

def kutup_durumu():
    tablo = Table(box=box.SIMPLE_HEAVY, show_header=True, header_style="bold magenta", padding=(0, 2))
    tablo.add_column("Kütüphane",    style="cyan",  min_width=14)
    tablo.add_column("Durum",        justify="center", min_width=12)
    tablo.add_column("Desteklenen Formatlar", style="dim")

    satirlar = [
        ("Pillow",      PIL_OK,     "JPG PNG TIFF BMP WEBP GIF"),
        ("mutagen",     MUTAGEN_OK, "MP3 FLAC OGG M4A WAV AAC WMA"),
        ("pikepdf",     PIKEPDF_OK, "PDF"),
        ("python-docx", DOCX_OK,    "DOCX"),
    ]
    for ad, ok, fmt in satirlar:
        tablo.add_row(
            ad,
            "[bold green]✔  Yüklü[/bold green]" if ok else "[bold red]✘  Eksik[/bold red]",
            fmt,
        )
    console.print(Panel(tablo, title="[bold]● Kütüphane Durumu", border_style="bright_black"))

# ── Metadata okuma ─────────────────────────────────────────────────────────────

def metadata_oku(yol: str) -> dict:
    bilgi = {}
    s = os.stat(yol)
    bilgi["📄 Dosya Adı"]    = os.path.basename(yol)
    bilgi["📦 Boyut"]        = f"{s.st_size / 1024:.1f} KB"
    bilgi["🕒 Oluşturma"]    = datetime.fromtimestamp(s.st_ctime).strftime("%d.%m.%Y %H:%M")
    bilgi["✏  Değiştirilme"] = datetime.fromtimestamp(s.st_mtime).strftime("%d.%m.%Y %H:%M")

    uz = os.path.splitext(yol)[1].lower()

    if uz in RESIM_UZ and PIL_OK:
        try:
            with Image.open(yol) as img:
                bilgi["🖼  Boyutlar"] = f"{img.width} x {img.height} px"
                bilgi["🎨 Renk Modu"] = img.mode
                exif = None
                if hasattr(img, "_getexif") and callable(img._getexif):
                    exif = img._getexif()
                if exif:
                    from PIL.ExifTags import TAGS
                    bilgi["📷 EXIF Alanları"] = f"{len(exif)} alan"
                    for tag_id, val in list(exif.items())[:6]:
                        bilgi[f"   {TAGS.get(tag_id, tag_id)}"] = str(val)[:52]
                else:
                    bilgi["📷 EXIF"] = "— yok —"
        except Exception as e:
            bilgi["Hata"] = str(e)

    elif uz in SES_UZ and MUTAGEN_OK:
        try:
            f = MutagenFile(yol)
            if f and f.tags:
                bilgi["🎵 Tag Sayısı"] = str(len(f.tags))
                for k, v in list(f.tags.items())[:8]:
                    bilgi[f"   {k}"] = str(v)[:52]
            else:
                bilgi["🎵 Ses Tag"] = "— yok —"
        except Exception as e:
            bilgi["Hata"] = str(e)

    elif uz in PDF_UZ and PIKEPDF_OK:
        try:
            with pikepdf.open(yol) as pdf:
                if pdf.docinfo:
                    for k, v in pdf.docinfo.items():
                        bilgi[f"📄 {k}"] = str(v)[:52]
                else:
                    bilgi["📄 PDF Meta"] = "— yok —"
        except Exception as e:
            bilgi["Hata"] = str(e)

    elif uz in DOCX_UZ and DOCX_OK:
        try:
            doc = Document(yol)
            p = doc.core_properties
            alanlar = {
                "👤 Yazar": p.author, "📝 Başlık": p.title,
                "📌 Konu": p.subject, "🔑 Etiketler": p.keywords,
                "💬 Açıklama": p.description,
                "✏  Son Düzenleyen": p.last_modified_by,
            }
            bos = True
            for k, v in alanlar.items():
                if v:
                    bilgi[k] = str(v)[:52]
                    bos = False
            if bos:
                bilgi["📝 DOCX Meta"] = "— yok —"
        except Exception as e:
            bilgi["Hata"] = str(e)

    return bilgi

def metadata_tablosu_goster(bilgi: dict):
    tablo = Table(box=box.SIMPLE_HEAVY, show_header=True,
                  header_style="bold yellow", padding=(0, 2))
    tablo.add_column("Alan",  style="yellow", min_width=24)
    tablo.add_column("Değer", style="white",  min_width=36)
    for k, v in bilgi.items():
        tablo.add_row(k, v)
    console.print(Panel(tablo, title="[bold]● Mevcut Metadata", border_style="yellow"))

# ── Metadata silme ─────────────────────────────────────────────────────────────

def yedek_al(yol: str) -> str:
    ad, uz = os.path.splitext(yol)
    yedek = f"{ad}_yedek{uz}"
    shutil.copy2(yol, yedek)
    return yedek

def resim_sil(yol):
    if not PIL_OK:
        return False, "Pillow yüklü değil  →  pip install Pillow"
    with Image.open(yol) as img:
        fmt = img.format
        data = list(img.getdata())
        temiz = Image.new(img.mode, img.size)
        temiz.putdata(data)
    yedek = yedek_al(yol)
    temiz.save(yol, format=fmt)
    return True, yedek

def ses_sil(yol):
    if not MUTAGEN_OK:
        return False, "mutagen yüklü değil  →  pip install mutagen"
    f = MutagenFile(yol)
    if f is None:
        return False, "Format tanınamadı"
    yedek = yedek_al(yol)
    f.delete(); f.save()
    return True, yedek

def pdf_sil(yol):
    if not PIKEPDF_OK:
        return False, "pikepdf yüklü değil  →  pip install pikepdf"
    yedek = yedek_al(yol)
    with pikepdf.open(yol, allow_overwriting_input=True) as pdf:
        with pdf.open_metadata() as m:
            m.clear()
        pdf.docinfo.clear()
        pdf.save(yol)
    return True, yedek

def docx_sil(yol):
    if not DOCX_OK:
        return False, "python-docx yüklü değil  →  pip install python-docx"
    yedek = yedek_al(yol)
    doc = Document(yol)
    p = doc.core_properties
    for attr in ("author","last_modified_by","title","subject",
                 "description","keywords","comments","category",
                 "content_status","identifier","language","version"):
        try:
            setattr(p, attr, "")
        except Exception:
            pass
    try:
        p.revision = 1
    except Exception:
        pass
    doc.save(yol)
    return True, yedek

def metadata_sil(yol: str):
    uz = os.path.splitext(yol)[1].lower()
    try:
        if uz in RESIM_UZ:   return resim_sil(yol)
        elif uz in SES_UZ:   return ses_sil(yol)
        elif uz in PDF_UZ:   return pdf_sil(yol)
        elif uz in DOCX_UZ:  return docx_sil(yol)
        else:
            return False, f"'{uz}' uzantısı desteklenmiyor."
    except Exception as e:
        return False, str(e)

# ── Dosya seçimi ───────────────────────────────────────────────────────────────

def dosya_sec():
    console.print(
        Panel(
            "[dim]Tam dosya yolunu girin (örn: /home/user/foto.jpg)\n"
            "'q' yazarak menüye dönebilirsiniz.[/dim]",
            title="[bold cyan]● Dosya Seç",
            border_style="cyan",
        )
    )
    while True:
        yol = Prompt.ask("[bold cyan]  Yol[/bold cyan]").strip().strip('"').strip("'")
        if yol.lower() in ("q", "exit", "çık"):
            return None
        if not yol:
            console.print("[red]  ✘ Boş yol. Tekrar deneyin.[/red]")
            continue
        if not os.path.isfile(yol):
            console.print(f"[red]  ✘ Dosya bulunamadı:[/red] {yol}")
            continue
        uz = os.path.splitext(yol)[1].lower()
        if uz not in TUM_UZ:
            desteklenen = "  ".join(sorted(TUM_UZ))
            console.print(
                f"[yellow]  ⚠ '{uz}' desteklenmiyor.[/yellow]\n"
                f"[dim]  Desteklenen: {desteklenen}[/dim]"
            )
            continue
        return yol

# ── Ana menü ───────────────────────────────────────────────────────────────────

def ana_menu():
    baslik_goster()
    kutup_durumu()

    while True:
        console.rule("[bold cyan]  MENÜ  ", style="cyan")

        tablo = Table(box=box.SIMPLE, show_header=False, padding=(0, 3))
        tablo.add_column(style="bold yellow", min_width=5)
        tablo.add_column(style="white")
        tablo.add_row("[1]", "Dosya Seç ve Metadata Görüntüle")
        tablo.add_row("[2]", "Metadata Sil")
        tablo.add_row("[3]", "Görüntüle + Sil  (Hızlı)")
        tablo.add_row("[q]", "Çıkış")
        console.print(tablo)

        secim = Prompt.ask(
            "[cyan]  Seçim[/cyan]",
            choices=["1", "2", "3", "q"],
            default="q",
        )

        if secim == "q":
            console.print("\n[bold cyan]  Görüşürüz! 👋[/bold cyan]\n")
            break

        yol = dosya_sec()
        if yol is None:
            baslik_goster()
            kutup_durumu()
            continue

        # Görüntüle
        if secim in ("1", "3"):
            with Progress(SpinnerColumn(), TextColumn("{task.description}"), transient=True) as p:
                p.add_task("Metadata okunuyor…", total=None)
                time.sleep(0.4)
                bilgi = metadata_oku(yol)
            metadata_tablosu_goster(bilgi)

        # Sil
        if secim in ("2", "3"):
            onay = Confirm.ask(
                f"\n[bold red]  ⚠  '{os.path.basename(yol)}' dosyasının metadata'sı silinecek. Devam?[/bold red]",
                default=False,
            )
            if not onay:
                console.print("[yellow]  İptal edildi.[/yellow]")
            else:
                with Progress(SpinnerColumn(), TextColumn("{task.description}"), transient=True) as p:
                    p.add_task("Metadata siliniyor…", total=None)
                    time.sleep(0.6)
                    basari, mesaj = metadata_sil(yol)

                if basari:
                    console.print(
                        Panel(
                            f"[bold green]✔  Metadata başarıyla silindi![/bold green]\n\n"
                            f"[dim]Orijinal yedeklendi →[/dim]\n[cyan]{mesaj}[/cyan]",
                            title="[bold green]● BAŞARILI",
                            border_style="green",
                        )
                    )
                else:
                    console.print(
                        Panel(
                            f"[bold red]✘  İşlem başarısız:[/bold red]\n{mesaj}",
                            title="[bold red]● HATA",
                            border_style="red",
                        )
                    )

        Prompt.ask("\n[dim]  Devam için Enter[/dim]", default="")
        baslik_goster()
        kutup_durumu()


if __name__ == "__main__":
    try:
        ana_menu()
    except KeyboardInterrupt:
        console.print("\n\n[bold cyan]  Çıkış yapıldı.[/bold cyan]\n")