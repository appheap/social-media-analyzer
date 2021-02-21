#  Pyrogram - Telegram MTProto API Client Library for Python
#  Copyright (C) 2017-2021 Dan <https://github.com/delivrance>
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

from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Union, Any

# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #


class InitConnection(TLObject):  # type: ignore
    """Telegram API method.

    Details:
        - Layer: ``123``
        - ID: ``0xc1cd5ea9``

    Parameters:
        api_id: ``int`` ``32-bit``
        device_model: ``str``
        system_version: ``str``
        app_version: ``str``
        system_lang_code: ``str``
        lang_pack: ``str``
        lang_code: ``str``
        query: Any method from :obj:`~pyrogram.raw.functions`
        proxy (optional): :obj:`InputClientProxy <pyrogram.raw.base.InputClientProxy>`
        params (optional): :obj:`JSONValue <pyrogram.raw.base.JSONValue>`

    Returns:
        Any object from :obj:`~pyrogram.raw.types`
    """

    __slots__: List[str] = ["api_id", "device_model", "system_version", "app_version", "system_lang_code", "lang_pack",
                            "lang_code", "query", "proxy", "params"]

    ID = 0xc1cd5ea9
    QUALNAME = "functions.InitConnection"

    def __init__(self, *, api_id: int, device_model: str, system_version: str, app_version: str, system_lang_code: str,
                 lang_pack: str, lang_code: str, query: TLObject, proxy: "raw.base.InputClientProxy" = None,
                 params: "raw.base.JSONValue" = None) -> None:
        self.api_id = api_id  # int
        self.device_model = device_model  # string
        self.system_version = system_version  # string
        self.app_version = app_version  # string
        self.system_lang_code = system_lang_code  # string
        self.lang_pack = lang_pack  # string
        self.lang_code = lang_code  # string
        self.query = query  # !X
        self.proxy = proxy  # flags.0?InputClientProxy
        self.params = params  # flags.1?JSONValue

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "InitConnection":
        flags = Int.read(data)

        api_id = Int.read(data)

        device_model = String.read(data)

        system_version = String.read(data)

        app_version = String.read(data)

        system_lang_code = String.read(data)

        lang_pack = String.read(data)

        lang_code = String.read(data)

        proxy = TLObject.read(data) if flags & (1 << 0) else None

        params = TLObject.read(data) if flags & (1 << 1) else None

        query = TLObject.read(data)

        return InitConnection(api_id=api_id, device_model=device_model, system_version=system_version,
                              app_version=app_version, system_lang_code=system_lang_code, lang_pack=lang_pack,
                              lang_code=lang_code, query=query, proxy=proxy, params=params)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.proxy is not None else 0
        flags |= (1 << 1) if self.params is not None else 0
        data.write(Int(flags))

        data.write(Int(self.api_id))

        data.write(String(self.device_model))

        data.write(String(self.system_version))

        data.write(String(self.app_version))

        data.write(String(self.system_lang_code))

        data.write(String(self.lang_pack))

        data.write(String(self.lang_code))

        if self.proxy is not None:
            data.write(self.proxy.write())

        if self.params is not None:
            data.write(self.params.write())

        data.write(self.query.write())

        return data.getvalue()
