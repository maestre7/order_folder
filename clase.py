
# Native
import os
from pathlib import Path

class Fichero:

    def __init__(self, name, path) -> None:
        data = self.separate_name_type(name)
        self.name = name
        self.file_name = data[:-1]
        self.extension = data[-1]
        self.path = Path(path)


    def separate_name_type(self, name: str):
        """We separate the name of the file from its type"""

        return name.split(os.extsep)
    
        

    
