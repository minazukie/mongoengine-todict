# -*- coding: utf-8 -*-
import unittest
from bson import ObjectId
from mongoengine import (
    Document,
    EmbeddedDocument,
    BooleanField,
    EmailField,
    EmbeddedDocumentField,
    EmbeddedDocumentListField,
    FloatField,
    IntField,
    StringField,
)
from mongoengine_todict import DocumentMixin


class SubDocument(EmbeddedDocument, DocumentMixin):
    hello = StringField()
    world = StringField()


class MyDocument(Document, DocumentMixin):
    bool_field = BooleanField()
    email_field = EmailField()
    embedded_document_field = EmbeddedDocumentField(SubDocument)
    embedded_document_list_field = EmbeddedDocumentListField(SubDocument)
    float_field = FloatField()
    int_field = IntField()
    string_field = StringField()


class TestDocumentMixin(unittest.TestCase):
    def setUp(self) -> None:
        self.doc = MyDocument(
            **{
                "id": ObjectId(),
                "bool_field": True,
                "email_field": "abc@def.com",
                "embedded_document_field": SubDocument(hello="a", world="b"),
                "embedded_document_list_field": [SubDocument(hello="c", world="d"), SubDocument(hello="e", world="f")],
                "float_field": 12.34,
                "int_field": 567,
                "string_field": "ok",
            }
        )

    def test_to_dict(self):
        result = self.doc.to_dict()

        self.assertEqual(str, type(result.get("id")))
        self.assertEqual("e", result["embedded_document_list_field"][1]["hello"])
