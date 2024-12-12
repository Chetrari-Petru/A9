from src.Core.Core import CoreInterface as Core
from src.ui.UiObject import Ui_MainWindow

def main():
    core = Core()
    ui   = Ui_MainWindow(core)

    while True:
        ui.step()

if __name__ == '__main__':
    main()