# -*- coding: utf-8 -*-
from mongoengine import (
    BooleanField,
    EmailField,
    EmbeddedDocumentField,
    EmbeddedDocumentListField,
    FloatField,
    IntField,
    ReferenceField,
    StringField,
)

from mongoengine_todict.errors import FieldAlReadyExistsError

_handlers = {
    StringField: lambda data: str(data),
    FloatField: lambda data: float(data),
    IntField: lambda data: int(data),
    EmailField: lambda data: str(data),
    BooleanField: lambda data: bool(data),
    EmbeddedDocumentField: lambda data: data.to_dict(),
    EmbeddedDocumentListField: lambda data: [d.to_dict() for d in data],
    ReferenceField: lambda data: str(data.id),
    # TODO: and more...
}


def _converted_data(obj, data):
    return _handlers.get(type(obj), lambda data: data)(data)


def register_field(cls, handler):
    if cls in _handlers:
        raise FieldAlReadyExistsError()
    _handlers[cls] = handler


class DocumentMixin:
    def to_dict(self):
        return_data = []

        for field_name in self._fields:
            data = self._data[field_name]
            if field_name in ("id",):
                return_data.append((field_name, str(data)))
            else:
                return_data.append((field_name, _converted_data(self._fields[field_name], data)))
        return dict(return_data)
