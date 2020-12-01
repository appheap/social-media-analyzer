import typing
from datetime import datetime
from json import dumps

import pyrogram


class Meta(type, metaclass=type("", (type,), {"__str__": lambda _: "~hi"})):
    def __str__(self):
        return f"<class 'pyrogram.types.{self.__name__}'>"


class Object(metaclass=Meta):
    def __init__(self, client: "pyrogram.Client" = None):
        self._client = client

    def bind(self, client: "pyrogram.Client"):
        """Bind a Client instance to this Pyrogram Object

        Parameters:
            client (:obj:`~pyrogram.types.Client`):
                The Client instance to bind this object with. Useful to re-enable bound methods after serializing and
                deserializing Pyrogram objects with ``repr`` and ``eval``.
        """
        self._client = client

    @staticmethod
    def default(obj: "Object"):
        if isinstance(obj, bytes):
            return repr(obj)

        # https://t.me/pyrogramchat/167281
        # Instead of re.Match, which breaks for python <=3.6
        if isinstance(obj, typing.Match):
            return repr(obj)

        return {
            "_": obj.__class__.__name__,
            **{
                attr: (
                    str(datetime.fromtimestamp(getattr(obj, attr)))
                    if attr.endswith("date") else
                    getattr(obj, attr)
                )
                for attr in filter(lambda x: not x.startswith("_"), obj.__dict__)
                if getattr(obj, attr) is not None
            }
        }

    def __str__(self) -> str:
        return dumps(self, indent=4, default=Object.default, ensure_ascii=False)

    def __repr__(self) -> str:
        return "pyrogram.types.{}({})".format(
            self.__class__.__name__,
            ", ".join(
                f"{attr}={repr(getattr(self, attr))}"
                for attr in filter(lambda x: not x.startswith("_"), self.__dict__)
                if getattr(self, attr) is not None
            )
        )

    def __eq__(self, other: "Object") -> bool:
        for attr in self.__dict__:
            try:
                if getattr(self, attr) != getattr(other, attr):
                    return False
            except AttributeError:
                return False

        return True

    def __getitem__(self, item):
        return getattr(self, item)

    def __setitem__(self, key, value):
        setattr(self, key, value)
