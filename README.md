# PC Monitorovací Panel – ročníkový projekt

## Autor

David Kaněra

---

## Cíl projektu

Cílem mého projektu je vytvořit externí informační panel připojený k počítači, který v reálném čase zobrazuje aktuální čas a teploty vybraných komponent počítače (CPU a GPU). Projekt slouží jako přehledný monitorovací nástroj a rozšiřuje možnosti běžného sledování stavu počítače.
Panel umožňuje přehledně sledovat stav počítače v reálném čase bez nutnosti zobrazovat data na hlavním monitoru.

---

## Použitý hardware

* 5" TFT LCD displej Waveshare (800×480, HDMI)
* Počítač s operačním systémem Windows 11
* HDMI kabel
* Napájení displeje přes USB

---

## Použitý software

* Windows 11
* Python 3
* Tkinter (grafické uživatelské rozhraní)
* OpenHardwareMonitor / LibreHardwareMonitor
* Knihovny Pythonu: **subprocess**, **datetime**

---

## Popis řešení

Aplikace je napsaná v jazyce **Python** a využívá knihovnu **Tkinter** pro vytvoření grafického rozhraní. Program běží v režimu celé obrazovky a je optimalizován pro rozlišení 800×480 pixelů, které odpovídá TFT displeji.

Teploty procesoru (CPU) a grafické karty (GPU) jsou získávány z monitorovacího nástroje běžícího na pozadí systému Windows. Tyto hodnoty jsou následně zpracovány a zobrazovány v aplikaci.

---

## Funkce aplikace

* Zobrazení aktuálního času
* Zobrazení aktuálního data
* Zobrazení teploty CPU
* Zobrazení teploty GPU
* Kruhové grafické ukazatele teplot
* Barevná signalizace teplot:

  * zelená – bezpečná teplota
  * oranžová – zvýšená teplota
  * červená – kritická teplota
* Automatická aktualizace hodnot každou sekundu
* Fullscreen režim vhodný pro externí displej
* 
---

## Screenshoty / Ukázka funkčního projektu

Níže můžete vidět, jak projekt vypadá při spuštění na počítači a na externím displeji.  

> **Poznámka:** Obrázky nahrajte do složky `images/` v repozitáři a změňte názvy souborů podle skutečných screenshotů.


![Hlavní obrazovka](images/screenshot1.png)
![Zobrazení teplot](images/screenshot2.png)
![Fullscreen režim](images/screenshot3.png)

---

## Problémy

Během vývoje projektu nastal problém se získáváním teplot hardwaru v operačním systému Windows 11. Standardní způsob ne vždy poskytuje spolehlivá data, proto jsem se rozhodl použít externí monitorovací software, který umožňuje čtení hodnot senzorů z procesoru a grafické karty.

Dále bylo nutné přizpůsobit grafické rozhraní malému rozlišení displeje tak, aby byly informace dobře čitelné.

---

## Vylepšení oproti základním řešením

* Vlastní grafické zpracování (kruhové indikátory)
* Barevná signalizace podle aktuální teploty
* Optimalizace rozložení prvků pro externí displej
* Oddělení logiky aplikace a grafického rozhraní

---

## Závěr

Výsledkem projektu je funkční monitorovací panel. Projekt propojuje programování, práci s hardwarem a praktické využití v reálném prostředí. Aplikace je přehledná, rozšiřitelná a vhodná pro další vývoj.

## Zdroje a citace

📙 Software / Nástroj

LibreHardwareMonitor (software):
LIBREHARDWAREMONITOR. LibreHardwareMonitor: monitorování hardwaru [software]. [cit. 2026‑01‑10]. Dostupné z: https://github.com/LibreHardwareMonitor/LibreHardwareMonitor
.

📙 Software / Nástroj

OpenHardwareMonitor (software):
OPENHARDWAREMONITOR. OpenHardwareMonitor: hardwarový monitor [software]. [cit. 2026‑01‑10]. Dostupné z: https://openhardwaremonitor.org/
.

📙 Dokumentace

Python dokumentace (online):
PYTHON SOFTWARE FOUNDATION. Python 3 Documentation [online]. [cit. 2026‑01‑10]. Dostupné z: https://docs.python.org/3/
.

Tkinter dokumentace (online):
PYTHON SOFTWARE FOUNDATION. Tkinter — Python interface to Tcl/Tk [online]. [cit. 2026‑01‑10]. Dostupné z: https://docs.python.org/3/library/tkinter.html
.

📙 Hardware reference (výrobce displeje)

Waveshare displej (produkt):
WAVESHARE. 5″ TFT LCD displej (800×480, HDMI) [online]. [cit. 2026‑01‑10]. Dostupné z: https://botland.cz/displeje-raspberry-pi/4467-odporovy-dotykovy-lcd-tft-5-800x480px-hdmi-gpio-pro-raspberry-pi-432-b-zero-waveshare-10563-5904422371364.html
.
