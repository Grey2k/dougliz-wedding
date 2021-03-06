# -*- coding: utf-8 -*-
"""
Person object storage repository.
"""
import typing as tp
from uuid import UUID

from app.crud.person import PersonRepository
from app.db.crud.base import SQLRepositoryMixin
from app.db.models.name import Name
from app.db.models.person import Person
from app.exceptions import ObjectNotFoundError


class PersonSQLRepository(SQLRepositoryMixin, PersonRepository[Person]):
    """
    Person object database storage repository.
    """
    __obj_cls__ = Person

    def get_by_name_id(
        self,
        name_id: UUID,
        *,
        raise_ex: bool = False
    ) -> tp.Optional[Person]:
        rv = self._session.query(Person).join(Name) \
            .filter(Name.uid == name_id) \
            .first()
        if not rv and raise_ex:
            raise ObjectNotFoundError(Person, 'name_id')
        return rv
