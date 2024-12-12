from datetime import date
import re
from .Menu import Menu
from src.Core.Errors.RepositoryErrors import *
from src.Core.Errors.UndoErrors import *
from ..Core.Errors.CoreErrors import InvalidRepositoryError


class Ui_MainWindow:
    _menu = None
    _curr_date = date(2024,1,1)
    def __init__(self, core):
        self._menu = Menu()
        self._menu.add_entry("Adds a movie or a new client", self.__add)
        self._menu.add_entry("List movies, rentals or clients", self.__ls)
        self._menu.add_entry("Removes a movie or a client", self.__rm)
        self._menu.add_entry("Modifies a movie or a client", self.__modify)
        self._menu.add_entry("Rents a movie", self.__rent)
        self._menu.add_entry("Returns a movie", self.__turn_in)
        self._menu.add_entry("Searches for a keyword in a specific repo ", self.__search_all)
        self._menu.add_entry("Searches a field ", self.__search)
        self._menu.add_entry("Change Date", self.__chdate)
        self._menu.add_entry("Undo last action", self.__undo)
        self._menu.add_entry("Redo last action", self.__redo)

        self.core = core

    def step(self):
        print(self._menu)
        print("date: "+str(self._curr_date))
        option = input("T-T  ")

        try:
            self._menu.run_option(option)
        except SystemExit:#KeyError:
            print("INVALID OPTION CHOSEN.")
            print("                      skill issue")

    def __add(self):
        print("Please choose what to add")
        mode = input("Modes: movie, client\n")
        mode.strip()

        args = {"kwargs" : {},
                "mode": mode}
        if mode == "movie":
            args["kwargs"]["title"] = input("Title: ")
            args["kwargs"]["description"] = input("Description: ")
            args["kwargs"]["genre"] = input("Genre: ")
        elif mode == "client":
            args["kwargs"]["name"] = input("Name: ")

        try:
            self.core.add(args["mode"], **args["kwargs"])
        except InvalidRepositoryError as e:
            print(e)

    def __ls(self):
        print("Modes: movies, rentals, clients")
        mode = input("Please choose a mode T-T: ")
        mode.strip()

        if mode != "movies" and mode != "clients" and mode != "rentals":
            print("INVALID OPTION CHOSEN.")
            print("                      skill issue")
            return

        print(self.core.get_storage(mode[:-1]))

    def __rm(self):
        print("Modes: movie, client")
        mode = input("Please choose a mode T-T: ")
        mode.strip()
        if mode != "movie" and mode != "client":
            print("INVALID OPTION CHOSEN.")
            print("                      skill issue")
            return

        _id = input("Please input the id of the element to remove\nT-T ")
        try:
            _id = int(_id)
        except ValueError:
            print("ID MUST BE INTEGER")
            print("                     skill issue")
            return

        try:
            self.core.remove(mode, id = _id)
        except Exception as e:
            print(e)
            print("                     skill issue")
            return


    def __rent(self):
        client_id = input("Please input the id of the client\nT-T ")
        try:
            client_id = int(client_id)
        except ValueError:
            print("ID MUST BE INTEGER")
            print("                     skill issue")
            return

        movie_id = input("Please input the id of the movie\nT-T ")
        try:
            movie_id = int(movie_id)
        except ValueError:
            print("ID MUST BE INTEGER")
            print("                     skill issue")
            return
        self.core.rent(client_id, movie_id, self._curr_date)

    def __chdate(self):
        _date = input("please input date: yyyy-mm-dd\nT-T ")
        _date.strip()
        match = re.match(r"\d{4}-\d{2}-\d{2}", _date)
        if not match:
            print("INVALID DATE")
            print("                     skill issue")
            return

        try:
            _date = date.fromisoformat(_date)
        except ValueError as ve:
            print(ve)
            print("                     skill issue")
            return
        self._curr_date = _date

    def __turn_in(self):
        client_id = input("Please input the id of the client\nT-T ")
        try:
            client_id = int(client_id)
        except ValueError:
            print("ID MUST BE INTEGER")
            print("                     skill issue")
            return

        movie_id = input("Please input the id of the movie\nT-T ")
        try:
            movie_id = int(movie_id)
        except ValueError:
            print("ID MUST BE INTEGER")
            print("                     skill issue")
            return

        try:
            self.core.return_movie(client_id, movie_id, self._curr_date)
        except ObjectNotFoundError as e:
            print(e)
            print("                     skill issue")
            return

    def __search(self):
        mode = input("Please choose a mode: movies, clients, rentals\n")
        mode.strip()
        if mode != "movies" and mode != "clients" and mode != "rentals":
            print("INVALID OPTION CHOSEN.")
            print("                     skill issue")
            return

        bp = self.core.get_blueprint(mode[:-1])
        bp_text = "Fields: "
        for field in bp:
            bp_text += str(field) + ", "
        print(bp_text)
        field = input("Please choose a field: ")
        field.strip()
        if not field in bp:
            print("INVALID FIELD")
            print("                     skill issue")
            return

        keywords = input("Search: ")
        search = self.core.search_field(mode[:-1], field, keywords)
        for i in search:
            print(i)

    def __search_all(self):
        mode = input("Please choose a mode: movies, clients, rentals\n")
        mode.strip()
        if mode != "movies" and mode != "clients" and mode != "rentals":
            print("INVALID OPTION CHOSEN.")
            print("                     skill issue")
            return
        keywords = input("Search: ")
        search = self.core.search_all(mode[:-1], keywords)
        for i in search:
            print(i)

    def __modify(self):
        mode = input("Please choose a mode: movie, client\n")
        mode.strip()
        if mode != "movie" and mode != "client":
            print("INVALID OPTION CHOSEN.")
            print("                     skill issue")
            return

        obj_id = input("Please input the id of the object to modify\n")
        try:
            obj_id = int(obj_id)
        except ValueError:
            print("ID MUST BE INTEGER")
            print("                     skill issue")
            return

        bp = self.core.get_blueprint(mode)
        del bp["id"]
        try:
            del bp["client_id"]
            del bp["movie_id"]
        except KeyError:
            pass

        bp_text = "Fields: "
        for field in bp:
            bp_text += str(field) + ", "

        print(bp_text)
        field = input("Please choose a field: ")
        field.strip()
        if not field in bp:
            print("INVALID FIELD")
            print("                     skill issue")
            return
        new_value = input("Please enter the new value: ")


        self.core.change_field(mode, obj_id, field, new_value)

    def __undo(self):
        try:
            self.core.undo()
        except UndoNotPossibleError as e:
            print(e)

    def __redo(self):
        try:
            self.core.redo()
        except RedoNotPossibleError as e:
            print(e)
