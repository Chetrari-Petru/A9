

entry_schematic = {"description": None, "func": None}

class Menu:
    _entries = []
    def __init__(self):
        self._entries = []
        self.add_entry(desc ="Exits the program", func = exit)


    def __dict__(self):
        return self._entries

    def add_entry(self, desc, func):
        self._entries.append({"description": desc, "func": func})

    def run_option(self, option, **kwargs):
        try:
            option = int(option)
        except ValueError:
            raise KeyError("Option must be an integer")
        if option >= len(self._entries):
            raise KeyError("Option invalid")
        self._entries[option]["func"](**kwargs)

    def __repr__(self):
        text = "\n\n"
        for i in range(0, len(self._entries)):
            text = text + str(i)+"    "+self._entries[i]["description"]+"\n"
        return text+"\n"
