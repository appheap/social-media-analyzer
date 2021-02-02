from .file import File


class InputFile:
    def __init__(
            self,
            file: 'File',
            saved: bool = True,
    ):
        self.file = file
        self.saved = saved

    def save(self):
        if not self.saved:
            self.file.save()
