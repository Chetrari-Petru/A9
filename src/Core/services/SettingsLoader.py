from .SettingsParser import SettingsParser
import os
class SettingsLoader:
    _settings_path = ""
    def __init__(self):
        self._settings_path = os.path.join(os.path.dirname(__file__), "..\\..\\..")
        print(self._settings_path)

    def load_settings(self):
        cwd = os.getcwd()
        os.chdir(self._settings_path)
        with open(os.getcwd()+"\\settings.properties", "r") as settings_file:
            settings = settings_file.read()
            parser = SettingsParser(settings)
            parsed_settings = parser.parse()
        os.chdir(cwd)
        return parsed_settings