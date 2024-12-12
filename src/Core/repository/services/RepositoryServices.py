from src.Core.Errors.RepositoryErrors import *
import re

class RepositoryServices:
    def __init__(self, repository):
        self._repo = repository

    def validate_id(self, id):
        storage = self._repo.get_storage()
        if not id in storage:
            raise ObjectNotFoundError("Object with id {0} was not found.".format(id))

    def get_blueprint(self):
        cls = self._repo.get_type_of_content()
        obj = object.__new__(cls)
        blueprint = obj.__dict__()
        return blueprint

    def search_field(self, field, keyword):
        pattern = r'\w*'+keyword.lower()+r"\w*"

        stg = self._repo.get_storage()

        elements = []
        for element in stg.values():
            if re.match(pattern, element.__dict__()[field], re.IGNORECASE):
                elements.append(element.__dict__())

        return elements
    def search_all(self, keyword):
        pattern = r'\w*'+keyword.lower()+r"\w*"
        stg = self._repo.get_storage()
        elements = []
        for element in stg.values():
            item = element.__dict__()
            for key in item:
                if re.match(pattern, str(item[key]), re.IGNORECASE):
                    if not element in elements:
                        elements.append(element)

        return elements