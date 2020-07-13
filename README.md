# mongoengine-todict

Convert MongoEngine object to Python dict easily.

## Usage

Basic usage

```python
from bson import ObjectId
from mongoengine import *
from mongoengine_todict import DocumentMixin


class MyDocument(Document, DocumentMixin):
    name = StringField()
    age = IntField()


doc = MyDocument(id=ObjectId("5f0c47dae1daaaea244c3fc8"), name="Tom", age=18)
doc.to_dict()  # => {'name': 'Tom', 'age': 18, 'id': '5f0c47dae1daaaea244c3fc8'}
```

Register your custom field

```python
from bson import ObjectId
from mongoengine import *
from mongoengine_todict import DocumentMixin, register_field


class CustomField(StringField):
    pass


def handle_custom_field(data):
    # do something...
    return "my handler"


register_field(CustomField, handle_custom_field)


class MyDocument(Document, DocumentMixin):
    custom = CustomField()


doc = MyDocument(id=ObjectId("5f0c47dae1daaaea244c3fc8"), custom="{}")
doc.to_dict()  # => {'custom': 'my handler', 'id': '5f0c47dae1daaaea244c3fc8'}
```
