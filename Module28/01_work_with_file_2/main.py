from typing import TextIO

class File:

    def __init__(self, filename:str, mode:str) -> None:
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self) -> TextIO:
        try:
            self.file = open(self.filename, self.mode, encoding='utf8')
        except (FileExistsError, FileNotFoundError):
            self.file = open(self.filename, 'w', encoding='utf8')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb) ->bool:
        self.file.close()
        if exc_type is OSError:
            pass
        return True


with File(filename="example.txt", mode="w") as file:
    file.write("Всем привет!")

