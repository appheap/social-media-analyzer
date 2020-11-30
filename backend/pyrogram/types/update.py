import pyrogram


class Update:
    def stop_propagation(self):
        raise pyrogram.StopPropagation

    def continue_propagation(self):
        raise pyrogram.ContinuePropagation
