
# Native
from pathlib import Path

# Own
from main_class import Principal


def main():
    try:
        path_folder: Path("C:\Users\usuario\Downloads")

        app = Principal()
        app.initiation(path_folder)
        app.check_folder()
        app.check_files()
        return 0
    
    except Exception as err:
        print(err)
        return -1

if __name__ == '__main__':
    main()