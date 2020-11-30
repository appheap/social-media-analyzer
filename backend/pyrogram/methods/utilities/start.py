import logging

from pyrogram import raw
from pyrogram.scaffold import Scaffold

log = logging.getLogger(__name__)


class Start(Scaffold):
    async def start(self):
        """Start the client.

        This method connects the client to Telegram and, in case of new sessions, automatically manages the full
        authorization process using an interactive prompt.

        Returns:
            :obj:`~pyrogram.Client`: The started client itself.

        Raises:
            ConnectionError: In case you try to start an already started client.

        Example:
            .. code-block:: python
                :emphasize-lines: 4

                from pyrogram import Client

                app = Client("my_account")
                app.start()

                ...  # Call API methods

                app.stop()
        """
        is_authorized = await self.connect()

        try:
            if not is_authorized:
                await self.authorize()

            if not await self.storage.is_bot() and self.takeout:
                self.takeout_id = (await self.send(raw.functions.account.InitTakeoutSession())).id
                log.warning(f"Takeout session {self.takeout_id} initiated")

            await self.send(raw.functions.updates.GetState())
        except (Exception, KeyboardInterrupt):
            await self.disconnect()
            raise
        else:
            await self.initialize()
            return self
