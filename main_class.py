
# Native
import os
import shutil
from pathlib import Path

# own
from clase import Fichero
from funciones import check_type_file


class Principal():

    def __init__(self) -> None:

        self.root_folder = None
        self.files = []
        self.sub_folder = []


    def initiation(self, path_folder):

        try:
            os.chdir(path_folder)
            self.root_folder = Path(os.getcwd())

        except OSError as err:
            raise OSError(f"{__name__}: {err}, {path_folder}")
        

    def check_folder(self):
        """We recover the content of the folder and separate its content
        depending on whether they are files or folders"""

        try:
            folder_work = os.listdir()

            for element in folder_work: # discriminamos ficheros o carpetas
                if '.' in element:
                    path = os.path.join(self.root_folder, element)
                    self.files.append(Fichero(element, path))
                else:
                    self.sub_folder.append(element)

        except Exception as err:
            raise Exception(f"{__name__}: {err}, {self.root_folder}")

    def check_files(self):
        """Depending on the type of file we associate it to a folder and move it to it"""

        try:
            for element in self.files:
                folder = check_type_file(f".{element.extension}")

                if folder:

                    if folder not in self.sub_folder:
                        os.mkdir(folder)
                        self.sub_folder.append(folder)

                    shutil.move(element.name, folder)

        except Exception as err:
            raise Exception(f"{__name__}: {err}, {self.files}")

                

