from pathlib import Path
import importlib
import time
from plugin.lib.CoreLib import clear, ErrorFlash, MenuTemplate, InputManage


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
    title="Human Benchmark Trainer", subtitle="Homepage", context=pname
)
main_choose = InputManage(max_val=len(pname) + 1)


def choose():
    choice = main_choose.get_int()
    if choice is None:
        return False

    if choice == len(plist) + 1:
        return True

    clear()
    plist[choice - 1][1].main()
    return False


def main():
    while True:
        main_menu.menu()
        isB = choose()
        if isB == True:
            break
    return 0

if __name__ == "__main__":
    main()
