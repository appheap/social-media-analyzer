from pyrogram.errors import RPCError
from pyrogram.scaffold import Scaffold
from typing import List
from pyrogram import types
import logging

log = logging.getLogger(__name__)


class GetAllDialogs(Scaffold):

    async def get_all_dialogs(self) -> List["types.ChannelAdminLogEvent"]:
        """
        Get all of the user's dialogs.

        Returns:
            List of :obj:`~pyrogram.types.Dialog`: On success, a list of dialogs is returned.

        Example:
            .. code-block:: python

                # Get all dialogs
                app.get_all_dialogs()
        """

        offset_date = 0
        dialogs = []
        while True:
            try:
                dialogs_slice = await self.get_dialogs(offset_date, )
            except RPCError as e:
                log.exception(e)
            except Exception as e:
                log.exception(e)
            else:
                if dialogs_slice:
                    dialogs.extend(dialogs_slice)
                    offset_date = dialogs_slice[-1].top_message.date
                else:
                    break
        return dialogs
