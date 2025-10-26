# Wifiphisher-Template-Generator-Captive-Portal-Edition
Uno script Python stabile e collaudato per creare template personalizzati per [Wifiphisher](https://github.com/wifiphisher/wifiphisher), progettati per essere visualizzati correttamente su captive portal di dispositivi Android, iOS, macOS e Windows.

> ✅ Compatibile con l’ultima versione stabile di Wifiphisher  
> ✅ Logo inline (Base64)  
> ✅ Tastiera stabile e focus automatico  
> ✅ HTML pulito e responsivo  
> ✅ Template testati con successo in ambienti reali

---

## 📌 Caratteristiche principali

- Generazione **automatica** della struttura del template in:

/usr/lib/python3/dist-packages/wifiphisher/data/phishing-pages/<nome_template>/

Always show details

- Logo PNG convertito e inserito **inline** (evita problemi di caricamento)
- HTML ottimizzato per **migliore compatibilità mobile**
- Focus stabile sul campo password (la tastiera non scompare)
- `config.ini` conforme a Wifiphisher
  

---

## ⚙️ Requisiti

- Python 3.x
- `Pillow` (`sudo apt install python3-pil`)
- Permessi root per modificare `/usr/lib/python3/dist-packages/`

---

## 🚀 Utilizzo

1. Esegui lo script:

```bash
sudo python3 genera_template_wifiphisher_v2.py

    Inserisci:

        Nome ID del template (es: wind)

        Nome visualizzato (es: Wind - Accesso WiFi)

        Percorso immagine logo .png

    Avvia wifiphisher con il template:

Always show details

sudo wifiphisher -p wind

🛠 Struttura del progetto

Always show details

├── genera_template_wifiphisher_v2.py          # Generatore principale
├── captive_http_responder.py (opzionale)      # Server HTTP 200 (per test)
├── README.md
├── LICENSE
└── .gitignore

⚠️ Disclaimer

    Questo strumento è progettato esclusivamente per test di penetrazione, formazione e ricerca in ambienti autorizzati.
    Qualsiasi uso non autorizzato è illegale.
