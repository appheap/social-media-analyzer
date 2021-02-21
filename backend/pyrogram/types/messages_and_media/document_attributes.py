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

import pyrogram

from pyrogram import raw
from ..object import Object
from pyrogram import types


class DocumentAttribute(Object):
    """Various possible attributes of a document (used to define if it's a sticker, a GIF, a video, a mask sticker, an image, an audio, and so on)



    Parameters:

    """

    def __init__(
            self,
            *,
            client: "pyrogram.Client" = None,
    ):
        super().__init__(client)

    @staticmethod
    def _parse(client, doc_attr: "raw.base.DocumentAttribute") -> "DocumentAttribute":
        if isinstance(doc_attr, raw.types.DocumentAttributeImageSize):
            return DocumentAttributeImageSize._parse(client, doc_attr)

        elif isinstance(doc_attr, raw.types.DocumentAttributeAnimated):
            return DocumentAttributeAnimated._parse(client, doc_attr)

        elif isinstance(doc_attr, raw.types.DocumentAttributeSticker):
            return DocumentAttributeSticker._parse(client, doc_attr)

        elif isinstance(doc_attr, raw.types.DocumentAttributeVideo):
            return DocumentAttributeVideo._parse(client, doc_attr)

        elif isinstance(doc_attr, raw.types.DocumentAttributeAudio):
            return DocumentAttributeAudio._parse(client, doc_attr)

        elif isinstance(doc_attr, raw.types.DocumentAttributeFilename):
            return DocumentAttributeFilename._parse(client, doc_attr)

        elif isinstance(doc_attr, raw.types.DocumentAttributeHasStickers):
            return DocumentAttributeHasStickers._parse(client, doc_attr)
        else:
            return None


class DocumentAttributeImageSize(DocumentAttribute):
    """Defines the width and height of an image uploaded as document


    Parameters:

    """

    def __init__(
            self,
            *,
            client: "pyrogram.Client" = None,

            width: int = None,
            height: int = None,
    ):
        super().__init__(client=client)

        self.width = width,
        self.height = height

    @staticmethod
    def _parse(client, doc_attr: "raw.base.DocumentAttribute") -> "DocumentAttributeImageSize":
        return DocumentAttributeImageSize(
            client=client,

            width=doc_attr.w,
            height=doc_attr.h
        )


class DocumentAttributeAnimated(DocumentAttribute):
    """Defines an animated GIF


    Parameters:

    """

    def __init__(
            self,
            *,
            client: "pyrogram.Client" = None,

    ):
        super().__init__(client=client)

    @staticmethod
    def _parse(client, doc_attr: "raw.base.DocumentAttribute") -> "DocumentAttributeAnimated":
        return DocumentAttributeAnimated(
            client=client,
        )


class DocumentAttributeSticker(DocumentAttribute):
    """Defines a sticker


    Parameters:

    """

    def __init__(
            self,
            *,
            client: "pyrogram.Client" = None,

            alt: str,
            stickerset: "types.StickerSet",
            is_mask_sticker: bool = None,
            mask_coords: "types.MaskCoords" = None,
    ):
        super().__init__(client=client)

        self.alt = alt,
        self.stickerset = stickerset
        self.is_mask_sticker = is_mask_sticker
        self.mask_coords = mask_coords

    @staticmethod
    def _parse(client, doc_attr: "raw.base.DocumentAttribute") -> "DocumentAttributeSticker":
        return DocumentAttributeSticker(
            client=client,

            alt=doc_attr.alt,
            stickerset=types.StickerSet._parse_from_input_stickerset(client, doc_attr.stickerset),
            is_mask_sticker=getattr(doc_attr, 'mask', None),
            mask_coords=types.MaskCoords._parse(client, getattr(doc_attr, 'mask_coords', None)),
        )


class DocumentAttributeVideo(DocumentAttribute):
    """Defines a video


    Parameters:

    """

    def __init__(
            self,
            *,
            client: "pyrogram.Client" = None,

            width: int = None,
            height: int = None,
            duration: int = None,
            round_message: bool = None,
            supports_streaming: bool = None,
    ):
        super().__init__(client=client)

        self.width = width,
        self.height = height
        self.duration = duration
        self.round_message = round_message
        self.supports_streaming = supports_streaming

    @staticmethod
    def _parse(client, doc_attr: "raw.base.DocumentAttribute") -> "DocumentAttributeVideo":
        return DocumentAttributeVideo(
            client=client,

            width=doc_attr.w,
            height=doc_attr.h,
            duration=doc_attr.duration,
            supports_streaming=getattr(doc_attr, 'supports_streaming', None),
            round_message=getattr(doc_attr, 'round_message', None),
        )


class DocumentAttributeAudio(DocumentAttribute):
    """Represents an audio file


    Parameters:

    """

    def __init__(
            self,
            *,
            client: "pyrogram.Client" = None,

            duration: int,
            voice: bool = None,
            title: str = None,
            performer: str = None,
            waveform: bytes = None,
    ):
        super().__init__(client=client)

        self.duration = duration
        self.voice = voice
        self.title = title
        self.performer = performer
        self.waveform = waveform

    @staticmethod
    def _parse(client, doc_attr: "raw.base.DocumentAttribute") -> "DocumentAttributeAudio":
        return DocumentAttributeAudio(
            client=client,

            duration=doc_attr.duration,
            voice=getattr(doc_attr, 'voice', None),
            title=getattr(doc_attr, 'title', None),
            performer=getattr(doc_attr, 'performer', None),
            waveform=getattr(doc_attr, 'waveform', None),
        )


class DocumentAttributeFilename(DocumentAttribute):
    """Represents an audio file


    Parameters:

    """

    def __init__(
            self,
            *,
            client: "pyrogram.Client" = None,

            file_name: str,
    ):
        super().__init__(client=client)

        self.file_name = file_name

    @staticmethod
    def _parse(client, doc_attr: "raw.base.DocumentAttribute") -> "DocumentAttributeFilename":
        return DocumentAttributeFilename(
            client=client,

            file_name=doc_attr.file_name,
        )


class DocumentAttributeHasStickers(DocumentAttribute):
    """Whether the current document has stickers attached


    Parameters:

    """

    def __init__(
            self,
            *,
            client: "pyrogram.Client" = None,

            file_name: str,
    ):
        super().__init__(client=client)

        self.file_name = file_name

    @staticmethod
    def _parse(client, doc_attr: "raw.base.DocumentAttribute") -> "DocumentAttributeHasStickers":
        return DocumentAttributeHasStickers(
            client=client,

            file_name=doc_attr.file_name,
        )
