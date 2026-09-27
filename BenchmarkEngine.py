from pathlib import Path
import importlib
import time
from plugin.lib.CoreLib import clear, ErrorFlash, MenuTemplate


def catch_plugins():
    plugin_list = []

    cdir = Path(__file__).resolve().parent
    pdir = cdir / "plugin"
    for file_path in pdir.glob("*.py"):
        if file_path.name == "__init__.py":
            continue
        modpath = f"plugin.{file_path.stem}"
        print(f"Found {file_path.name}.")
        try:
            plugin = importlib.import_module(modpath)
            if hasattr(plugin, "main"):
                name = getattr(plugin, "NAME", file_path.stem)
                plugin_list.append([name, plugin])
            else:
                print(f"{file_path.name} doesn't have main().")
        except Exception as e:
            print(f"Failed to catch plugin: {file_path.name}")
            print(f"Reason: {e}")
    return plugin_list


plist = catch_plugins()
pname = [p[0] for p in plist]

main_menu = MenuTemplate(
    title="Human Benchmark Trainer", subtitle="Main Page", context=pname
)


def choose():
    try:
        choice = int(input())
    except ValueError:
        ErrorFlash()
        return True

    if choice > len(plist) + 1 or choice < 1:
        ErrorFlash()
        return True

    if choice == len(plist) + 1:
        return False

    try:
        clear()
        plist[choice - 1][1].main()
        return True
    except Exception as e:
        print(f"Oops! Somthing went wrong: {e}")
        ErrorFlash("Returning to the main menu...", 1.35)


def main():
    while True:
        clear()
        main_menu.menu()
        isB = choose()
        if isB == False:
            break
        else:
            continue
    return 0


main()
