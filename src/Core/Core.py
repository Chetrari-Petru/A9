from src.Core.Errors.RepositoryErrors import NothingImportedError
from src.Core.repository import *
from src.Core.services.SettingsLoader import SettingsLoader
from src.Core.Errors.CoreErrors import *
from datetime import timedelta
from src.Core.services.UndoServices import UndoServices

class CoreInterface:
    core = None
    _undo_service = None
    def __init__(self):
        self.core = Core()
        self._undo_service = UndoServices(self.core)


    def add(self, repo, **kwargs):
        item = self.core.add(repo, **kwargs)
        _id = item.get_id()
        self._undo_service.register_action(self.core.add, id = _id, repo = repo, **kwargs)

    def remove(self, repo, **kwargs):
        self._undo_service.register_action(self.core.remove, repo = repo, **kwargs)
        self.core.remove(repo, **kwargs)

    def rent(self, client_id, movie_id, rent_date):
        item = self.core.rent(client_id, movie_id, rent_date)
        _id = item.get_id()
        self._undo_service.register_action(self.core.rent, id = _id, client_id = client_id, movie_id = movie_id, rent_date = rent_date)

    def return_movie(self, client_id, movie_id, date):
        self._undo_service.register_action(self.core.return_movie, client_id = client_id, movie_id = movie_id, date = date)
        self.core.return_movie(client_id, movie_id, date)

    def change_field(self, repo, object_id, field, new_value):
        self._undo_service.register_action(self.core.change_field, repo = repo, object_id = object_id, field = field, new_value = new_value)
        self.core.change_field(repo, object_id, field, new_value)

    def undo(self):
        self._undo_service.undo()

    def redo(self):
        self._undo_service.redo()


    # direct references to core
    def get_blueprint(self, repo):
        return self.core.get_blueprint(repo)

    def search_field(self, repo, field, keywords):
        return self.core.search_field(repo, field, keywords)

    def search_all(self, repo, keywords):
        return self.core.search_all(repo, keywords)

    def get_storage(self, repo, **kwargs):
        return self.core.get_storage(repo, **kwargs)




class Core:
    _repository = None
    _settings = None
    _repos = None

    def __init__(self):
        settings =  SettingsLoader().load_settings()
        self.settings = settings
        self._repository = RepositoryController(
            settings['client_repo'],
            settings['movie_repo'],
            settings['rental_repo'])
        self._repos = {
            "client": self._repository.client_repo,
            "movie": self._repository.movie_repo,
            "rental": self._repository.rental_repo
        }
        self._repo_services = {
            "client": self._repository.client_services,
            "movie": self._repository.movie_services,
            "rental": self._repository.rental_services
        }

    def __validate_repo(self, repo):
        if not repo in self._repos:
            raise InvalidRepositoryError(repo + " is not a valid repository")

    def add(self, repo, **kwargs):
        self.__validate_repo(repo)
        try:
            item = self._repos[repo].add(**kwargs)
        except NothingImportedError:
            pass
        return item

    def remove(self, repo, **kwargs):
        self.__validate_repo(repo)
        self._repos[repo].remove(**kwargs)

    def get_storage(self, repo, **kwargs):
        self.__validate_repo(repo)
        return self._repos[repo].get_storage(**kwargs)

    def rent(self, client_id, movie_id, rent_date):
        self._repository.client_services.validate_id(client_id)
        self._repository.movie_services.validate_id(movie_id)
        if not self._repository.rental_services.check_can_rent(client_id, rent_date):
            raise CannotRentError("user with id {0} cannot rent".format(client_id))
        item = self.add(repo = "rental", client_id = client_id,
                                         movie_id = movie_id,
                                         rented_date = rent_date,
                                         due_date = rent_date+timedelta(14),
                                         returned_date = None)
        return item

    def return_movie(self, client_id, movie_id, date):
        self._repository.client_services.validate_id(client_id)
        self._repository.movie_services.validate_id(movie_id)

        rentals = self._repository.rental_repo.get_storage()
        rental_ids = []
        for rental in rentals:
            rental_dict = rentals[rental].__dict__()
            rental_valid = rental_dict["client_id"] == client_id
            rental_valid = rental_valid and rental_dict["movie_id"] == movie_id
            rental_valid = rental_valid and rental_dict["returned_date"] is None
            if rental_valid:
                rental_ids.append(rental)


        for rental in rental_ids:
            self._repository.rental_services.turn_in_rental(rental, date)

    def change_field(self, repo, object_id, field, new_value):
        self.__validate_repo(repo)
        stg = self._repos[repo].get_storage()
        stg[object_id].change_field(field, new_value)
        self._repos[repo].modify(stg[object_id])


    def get_blueprint(self, repo):
        self.__validate_repo(repo)
        return self._repo_services[repo].get_blueprint()

    def search_field(self, repo, field, keywords):
        return self._repo_services[repo].search_field(field, keywords)

    def search_all(self, repo, keywords):
        return self._repo_services[repo].search_all(keywords)


