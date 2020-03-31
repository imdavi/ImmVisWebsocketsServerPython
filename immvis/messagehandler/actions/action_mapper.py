from kim import PolymorphicMapper, field
from .action import Action
from .load import LoadDataFrameFromFile
from .hello import HelloAction


class ActionMapper(PolymorphicMapper):
    __type__ = Action

    object_type = field.String(choices=['load_dataset', 'hello'])

    __mapper_args__ = {
        'polymorphic_on': object_type,
        'allow_polymorphic_marshal': True,
    }


class LoadDataFrameFromFileMapper(ActionMapper):
    __type__ = LoadDataFrameFromFile

    file_path = field.String()

    __mapper_args__ = {
        'polymorphic_name': 'load_dataset'
    }


class EchoMapper(ActionMapper):
    __type__ = HelloAction

    __mapper_args__ = {
        'polymorphic_name': 'hello'
    }
