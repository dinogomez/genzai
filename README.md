<p align=center>
  <a href="https://github.com/dinogomez/genzai/releases/latest"><img alt="GitHub release (latest by date)" src="https://img.shields.io/github/v/tag/dinogomez/genzai?color=343638&label=latest&logo=github"></a>
  <a href="https://github.com/dinogomez/genzai/releases/latest"><img alt="GitHub Releases" src="https://img.shields.io/github/downloads/dinogomez/genzai/latest/total?color=343638&label=downloads&logo=github"></a>
  <a href="https://github.com/dinogomez/genzai/releases/"><img alt="All GitHub Releases" src="https://img.shields.io/github/downloads/dinogomez/genzai/total?color=343638&label=total%20downloads&logo=github"></a>
</p>

# <img src=https://github.com/dinogomez/genzai/assets/41871666/0536940c-fa2d-4fda-9744-25edbc5ead14 style="height:1em;"/> Genzai : Discord Rich Presence

---

### ⭐ [NEW] Added option to load and save your settings to a config file.

A lightweight Discord custom Rich Presence manager that runs on Linux and Windows, with macOS support coming soon. Built with [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) and [pypresence](https://github.com/qwertyquerty/pypresence), heavily inspired by [maximax42](https://github.com/maximmax42)'s amazing [Discord-CustomRP](https://github.com/maximmax42/Discord-CustomRP).

<p align="center">
<img src="https://github.com/dinogomez/genzai/assets/41871666/0d384431-5226-491f-baca-8a1c075b06ce">

# Download

### Latest [DOWNLOAD HERE](https://github.com/dinogomez/genzai/releases/latest)

The latest official release of Genzai is available for both Linux and Windows. Check the [Genzai Latest Release](https://github.com/dinogomez/genzai/releases/latest).

- [Download for Linux](https://github.com/dinogomez/genzai/releases/download/1.0.1/genzai_linux_1.0.1.zip)
- [Download for Windows](https://github.com/dinogomez/genzai/releases/download/1.0.1/genzai_windows_1.0.1.zip)

## How to use Genzai?

### Linux and Windows

1. Extract the zip file.
2. Run `genzai.exe` inside the `genzai` folder.
3. Make a new Discord application, here in the [Discord Developer Portal](https://discord.com/developers/applications).
4. Click `New Application` on the top right.
5. Create your application name, this will be your `title` in your Discord Presence.
6. Copy the `Application ID` and paste it in the `App ID` field in Genzai.
7. Click `Connect`
8. Fill out the fields you want.
9. Click `Update`
10. Enjoy your new Discord Rich Presence!

## How to build Genzai from source

Clone the repository and cd into it.

```bash
$ git clone git@github.com:dinogomez/genzai.git
$ cd genzai
```

Install the python requirements via pip

```bash
pip install -r requirements.txt
```

I advice building the application with `auto-py-to-exe` or `pyinstaller` to avoid any issues with missing dependencies.

With `auto-py-to-exe`.

1. Select `One Directory`
2. Select `Window Based`
3. Select `Add Folder` and add the `genzai/assets` folder
4. Select `Add Folder` and add `customtkinter` package.

   > Use `pip show customtkinter` to find the location of the package.

5. Add the `PIL._tkinter_finder` hidden import
6. Select `Convert .py to .exe` and wait for the build to finish
7. Run the `genzai.exe` file in the `output` folder
   <br>
   <br>

With `pyinstaller`, refer to this [documentation](https://customtkinter.tomschimansky.com/documentation/packaging) when building customtkinter apps.

```bash
pyinstaller --noconfirm --onedir --windowed --icon "<Genzai Location>/Genzai/assets/genzai.ico" 
--add-data "<CustomTkinter Location>/customtkinter:customtkinter/" 
--add-data "<Genzai Location>/Genzai/assets:assets/" 
--hidden-import "PIL._tkinter_finder"  
"<Genzai Location>/Genzai/genzai.py"
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](https://github.com/dinogomez/genzai/blob/main/LICENSE)
