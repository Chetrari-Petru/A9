from src.Core.domain.Action import Action
from src.Core.Errors.UndoErrors import *

class UndoServices:
    repository = None
    core = None
    opposites = []
    stack_index = -1

    def __init__(self, core):
        self.repository = []
        self.core = core
        self.opposites  = [[core.add, core.remove],
                           [core.return_movie, self.__reverse_return_movie],
                           [core.change_field, core.change_field],
                           [core.rent, core.remove]]
        self.stack_index = 0

    def __reverse_return_movie(self, client_id, movie_id, date):
        rentals = self.core.get_storage("rental")
        rental_ids = []
        for rental in rentals:
            rental_dict = rentals[rental].__dict__()
            rental_valid = rental_dict["client_id"] == client_id
            rental_valid = rental_valid and rental_dict["movie_id"] == movie_id
            rental_valid = rental_valid and rental_dict["returned_date"] == date
            if rental_valid:
                rental_ids.append(rental_dict["id"])
        for id in rental_ids:
            self.core.change_field("rental", id, "due_date", None)

    def register_action(self, action, **kwargs):
        print(self.stack_index, self.repository.__len__())
        try:
            self.repository = self.repository[:self.stack_index]
        except IndexError:
            pass


        self.stack_index += 1
        args = self.__args(action, kwargs)
        act_dict = self.__get_opposites(action)
        new_action = Action(action = act_dict["action"],
                            reverse_action=  act_dict["reverse"],
                            action_parameters = args["action"],
                            reverse_action_parameters = args["reverse"])
        self.repository.append(new_action)


    def undo(self):
        if self.stack_index - 1 < 0:
            raise UndoNotPossibleError("Cannot undo anymore")
        self.stack_index -= 1
        print(self.stack_index, self.repository.__len__())


        action = self.repository[self.stack_index]
        action.undo()

    def redo(self):
        if self.stack_index + 1 > len(self.repository):
            raise RedoNotPossibleError("Cannot redo anymore")


        action = self.repository[self.stack_index]
        self.stack_index += 1
        print(self.stack_index, self.repository.__len__())
        action.redo()

    def __clean_dict(self, dict):
        _dict = dict.copy()
        try:
            del _dict["id"]
        except KeyError:
            pass
        return _dict

    def __get_opposites(self, action):
        for opposite in self.opposites:
            for i in range(2):
                if opposite[i] != action:
                    continue
                _d = {"action": action}
                _d["reverse"] = opposite[1-i]
                return _d


    def __args(self, action, kwargs):
        t = {}
        print(kwargs)
        try:
            t[self.core.add] = {"action": self.__clean_dict(kwargs),  "reverse": {"repo": kwargs["repo"],"id":kwargs["id"]}}
        except KeyError:
            pass
        try:
            stg = self.core.get_storage(kwargs["repo"])
            item_dict = stg[kwargs["id"]].__dict__()
            item_dict["repo"] = kwargs["repo"]
            t[self.core.remove] = {"action": kwargs,  "reverse": self.__clean_dict(item_dict)}
        except KeyError:
            pass
        try:
            t[self.core.change_field] = {"action": kwargs, "reverse": {"object_id":kwargs["object_id"],
                                                                "repo":kwargs["repo"],
                                                                "field":kwargs["field"],
                                                                "new_value":self.core.get_storage(kwargs["repo"])[kwargs["object_id"]].__dict__()[kwargs["field"]]}}
        except KeyError:
            pass
        try:
            t[self.core.return_movie] = {"action": kwargs, "reverse": kwargs}
        except KeyError:
            pass
        try:
            t[self.__reverse_return_movie] = {"action": kwargs, "reverse": kwargs}
        except KeyError:
            pass
        try:
            t[self.core.rent] = {"action": self.__clean_dict(kwargs), "reverse": {"repo": "rental","id":kwargs["id"]}}
        except KeyError as e:
            pass
        return t[action]

