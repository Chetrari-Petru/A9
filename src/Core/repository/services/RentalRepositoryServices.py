from .RepositoryServices import RepositoryServices
import datetime

from ...Errors.RepositoryErrors import NothingImportedError


class RentalRepositoryServices(RepositoryServices):
    def __init__(self, repository):
        super().__init__(repository)

    def check_can_rent(self, client_id, date):
        stg = self._repo.get_storage()
        for rent in stg:
            rental = stg[rent].__dict__()
            if rental['client_id'] == client_id and datetime.date.fromisoformat(str(rental['due_date'])) < date:
                return False
        return True

    def turn_in_rental(self, rental_id, date):
        stg = self._repo.get_storage()

        rental = stg[rental_id]
        rental.returned_date = date

        self._repo.remove(rental_id)
        rdict = rental.__dict__()
        del rdict['id']
        try:
            self._repo.add(**rdict)
        except NothingImportedError:
            pass

    def delete_dependency(self, client_id = None, movie_id = None):
        stg = self._repo.get_storage()


