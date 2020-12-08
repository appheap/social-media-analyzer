#  Pyrogram - Telegram MTProto API Client Library for Python
#  Copyright (C) 2017-2020 Dan <https://github.com/delivrance>
#
#  This file is part of Pyrogram.
#
#  Pyrogram is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Pyrogram is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with Pyrogram.  If not, see <http://www.gnu.org/licenses/>.

import pyrogram

from pyrogram import raw
from ..object import Object
from pyrogram import types
from typing import List


class WebDocument(Object):
    """Remote document

    # todo: update docs

    Parameters:

    """

    def __init__(
            self,
            *,
            client: "pyrogram.Client" = None,

            url: str,
            size: int,
            mime_type: str,
            attributes: List["types.DocumentAttribute"],
            access_hash: int = None,
            type: str = None,

    ):
        super().__init__(client)
        self.url = url
        self.size = size
        self.mime_type = mime_type
        self.attributes = attributes
        self.access_hash = access_hash
        self.type = type

    @staticmethod
    def _parse(client, web_document: "raw.base.WebDocument") -> "WebDocument":
        if isinstance(web_document, raw.types.WebDocument):
            return WebDocument(
                client=client,

                url=web_document.url,
                size=web_document.size,
                mime_type=web_document.mime_type,
                attributes=types.List(
                    [types.DocumentAttribute._parse(client, attr) for attr in web_document.attributes]) or None,
                access_hash=getattr(web_document, 'access_hash', None),
                type='normal' if isinstance(web_document, raw.types.WebDocument) else 'no_proxy',
            )
