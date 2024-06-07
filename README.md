<p align="center">
<img src="https://github.com/dinogomez/genzai/assets/41871666/b1848453-2ff3-47a8-8f6a-9016bdee1404.png#gh-light-mode-only">
<img src="https://github.com/dinogomez/genzai/assets/41871666/24f7387c-0bb4-426d-b071-4c9b108aa673#gh-dark-mode-only">
</p>


---

A lightweight Discord custom Rich Presence manager made for Linux. Built with [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) and [pypresence](https://github.com/qwertyquerty/pypresence), heavily inspired by [maximmax42/Discord-CustomRP](https://github.com/maximmax42/Discord-CustomRP).

<p align="center">
<img src="https://github.com/dinogomez/genzai/assets/41871666/8c8cc8f9-74fa-4330-abaf-fe6b977954d0">
</p>

## Installation

```bash
pyinstaller --noconfirm --onedir --windowed --icon "<Genzai Location>/Genzai/assets/genzai.ico" --add-data "<CustomTkinter Location>/customtkinter:customtkinter/" --add-data "<Genzai Location>/Genzai/assets:assets/" --hidden-import "PIL._tkinter_finder"  "<Genzai Location>/Genzai/genzai.py"
```
