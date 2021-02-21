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

from typing import List, Union

from pyrogram import raw
from pyrogram import utils
from pyrogram.file_id import FileType
from pyrogram.scaffold import Scaffold


class DeleteProfilePhotos(Scaffold):
    async def delete_profile_photos(
            self,
            photo_ids: Union[str, List[str]]
    ) -> bool:
        """Delete your own profile photos.

        Parameters:
            photo_ids (``str`` | List of ``str``):
                A single :obj:`~pyrogram.types.Photo` id as string or multiple ids as list of strings for deleting
                more than one photos at once.

        Returns:
            ``bool``: True on success.

        Example:
            .. code-block:: python

                # Get the photos to be deleted
                photos = app.get_profile_photos("me")

                # Delete one photo
                app.delete_profile_photos(photos[0].file_id)

                # Delete the rest of the photos
                app.delete_profile_photos([p.file_id for p in photos[1:]])
        """
        photo_ids = photo_ids if isinstance(photo_ids, list) else [photo_ids]
        input_photos = [utils.get_input_media_from_file_id(i, FileType.PHOTO).id for i in photo_ids]

        return bool(await self.send(
            raw.functions.photos.DeletePhotos(
                id=input_photos
            )
        ))
