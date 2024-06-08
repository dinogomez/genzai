
# <img src=https://github.com/dinogomez/genzai/assets/41871666/0536940c-fa2d-4fda-9744-25edbc5ead14 style="height:1em;"/> Genzai : Discord Rich Presence
---


A lightweight Discord custom Rich Presence manager that runs on Linux and Windows, with macOS support coming soon. Built with [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) and [pypresence](https://github.com/qwertyquerty/pypresence), heavily inspired by [maximax42](https://github.com/maximmax42)'s amazing [Discord-CustomRP](https://github.com/maximmax42/Discord-CustomRP). 

<p align="center">
<img src="https://github.com/dinogomez/genzai/assets/41871666/0d384431-5226-491f-baca-8a1c075b06ce">



## Installation

```bash
pyinstaller --noconfirm --onedir --windowed --icon "<Genzai Location>/Genzai/assets/genzai.ico" --add-data "<CustomTkinter Location>/customtkinter:customtkinter/" --add-data "<Genzai Location>/Genzai/assets:assets/" --hidden-import "PIL._tkinter_finder"  "<Genzai Location>/Genzai/genzai.py"
```
