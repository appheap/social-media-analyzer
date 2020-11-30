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

# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

PageBlock = Union[
    raw.types.PageBlockAnchor, raw.types.PageBlockAudio, raw.types.PageBlockAuthorDate, raw.types.PageBlockBlockquote, raw.types.PageBlockChannel, raw.types.PageBlockCollage, raw.types.PageBlockCover, raw.types.PageBlockDetails, raw.types.PageBlockDivider, raw.types.PageBlockEmbed, raw.types.PageBlockEmbedPost, raw.types.PageBlockFooter, raw.types.PageBlockHeader, raw.types.PageBlockKicker, raw.types.PageBlockList, raw.types.PageBlockMap, raw.types.PageBlockOrderedList, raw.types.PageBlockParagraph, raw.types.PageBlockPhoto, raw.types.PageBlockPreformatted, raw.types.PageBlockPullquote, raw.types.PageBlockRelatedArticles, raw.types.PageBlockSlideshow, raw.types.PageBlockSubheader, raw.types.PageBlockSubtitle, raw.types.PageBlockTable, raw.types.PageBlockTitle, raw.types.PageBlockUnsupported, raw.types.PageBlockVideo]


# noinspection PyRedeclaration
class PageBlock:  # type: ignore
    """This base type has 29 constructors available.

    Constructors:
        .. hlist::
            :columns: 2

            - :obj:`PageBlockAnchor <pyrogram.raw.types.PageBlockAnchor>`
            - :obj:`PageBlockAudio <pyrogram.raw.types.PageBlockAudio>`
            - :obj:`PageBlockAuthorDate <pyrogram.raw.types.PageBlockAuthorDate>`
            - :obj:`PageBlockBlockquote <pyrogram.raw.types.PageBlockBlockquote>`
            - :obj:`PageBlockChannel <pyrogram.raw.types.PageBlockChannel>`
            - :obj:`PageBlockCollage <pyrogram.raw.types.PageBlockCollage>`
            - :obj:`PageBlockCover <pyrogram.raw.types.PageBlockCover>`
            - :obj:`PageBlockDetails <pyrogram.raw.types.PageBlockDetails>`
            - :obj:`PageBlockDivider <pyrogram.raw.types.PageBlockDivider>`
            - :obj:`PageBlockEmbed <pyrogram.raw.types.PageBlockEmbed>`
            - :obj:`PageBlockEmbedPost <pyrogram.raw.types.PageBlockEmbedPost>`
            - :obj:`PageBlockFooter <pyrogram.raw.types.PageBlockFooter>`
            - :obj:`PageBlockHeader <pyrogram.raw.types.PageBlockHeader>`
            - :obj:`PageBlockKicker <pyrogram.raw.types.PageBlockKicker>`
            - :obj:`PageBlockList <pyrogram.raw.types.PageBlockList>`
            - :obj:`PageBlockMap <pyrogram.raw.types.PageBlockMap>`
            - :obj:`PageBlockOrderedList <pyrogram.raw.types.PageBlockOrderedList>`
            - :obj:`PageBlockParagraph <pyrogram.raw.types.PageBlockParagraph>`
            - :obj:`PageBlockPhoto <pyrogram.raw.types.PageBlockPhoto>`
            - :obj:`PageBlockPreformatted <pyrogram.raw.types.PageBlockPreformatted>`
            - :obj:`PageBlockPullquote <pyrogram.raw.types.PageBlockPullquote>`
            - :obj:`PageBlockRelatedArticles <pyrogram.raw.types.PageBlockRelatedArticles>`
            - :obj:`PageBlockSlideshow <pyrogram.raw.types.PageBlockSlideshow>`
            - :obj:`PageBlockSubheader <pyrogram.raw.types.PageBlockSubheader>`
            - :obj:`PageBlockSubtitle <pyrogram.raw.types.PageBlockSubtitle>`
            - :obj:`PageBlockTable <pyrogram.raw.types.PageBlockTable>`
            - :obj:`PageBlockTitle <pyrogram.raw.types.PageBlockTitle>`
            - :obj:`PageBlockUnsupported <pyrogram.raw.types.PageBlockUnsupported>`
            - :obj:`PageBlockVideo <pyrogram.raw.types.PageBlockVideo>`
    """

    QUALNAME = "pyrogram.raw.base.PageBlock"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://docs.pyrogram.org/telegram/base/page-block")
