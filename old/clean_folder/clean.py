from pathlib import Path
import sys
import shutil

import re


KIRILIK = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
LATINIC = ("a", "b", "v", "g", "d", "e", "e", "j", "z",
           "i", "y", "k", "l", "m", "n", "o", "p", "r", "s",
           "t", "u", "f", "h", "c", "ch", "sh", "sch", "",
           "u", "", "e", "yu", "ya", "e", "i", "i", "g")

TRANSLAT = {}

for kir, lat in zip(KIRILIK, LATINIC):
   TRANSLAT[ord(kir)] = lat
   TRANSLAT[ord(kir.upper())] = lat.upper()


def normalize(name: str) -> str:
    new_name = name.translate(TRANSLAT)
    new_name = re.sub(r'\W', '_', new_name)
    return new_name




IMAGES_LIST = []
DOCUMENTS_LIST = []
AUDIO_LIST = []
VIDEO_LIST = []
ARCHIVES_LIST = []
OTHER_LIST = []

KNOWN_EXTENSIONS = set()
UNKNOWN_EXTENSIONS = set()

FOLDER_LIST = []

INNER_FOLDERS_LIST = ('images', 'documents', 'audio', 'video', 'archives')

EXTENSIONS_DICT = {'images': ('jpeg', 'png', 'jpg', 'svg'),
                   'documents': ('doc', 'docx', 'txt', 'pdf', 'xlsx', 'pptx'),
                   'audio': ('mp3', 'ogg', 'wav', 'amr'),
                   'video': ('avi', 'mp4', 'mov', 'mkv'),
                   'archives': ('zip', 'gz', 'tar')}


def empty_folder_remover(folder: Path):
    for item in FOLDER_LIST[::-1]:
        try:
            item.rmdir()
        except OSError:
            print(f'Folder isn\'t empty {item}')


def make_dir_func(path):
    INNER_FOLDERS_LIST = ('images', 'documents', 'audio', 'video', 'archives')
    new_folder = 'Sorted_folder'
    for item in INNER_FOLDERS_LIST:
        Path(path, new_folder, item).mkdir(exist_ok=True, parents=True)



def file_scaner(folder_path: Path) -> None:

    for x in folder_path.iterdir():
        if x.is_file():

            if x.suffix[1:] in EXTENSIONS_DICT['images']:
                IMAGES_LIST.append(f'{normalize(x.stem)}{x.suffix}')
                KNOWN_EXTENSIONS.add(f'{x.suffix}')
                shutil.move(Path(x.absolute()),
                            Path(FOLDER_PATH, 'Sorted_folder', 'images', f'{normalize(x.stem)}{x.suffix}'))

            elif x.suffix[1:] in EXTENSIONS_DICT['documents']:
                DOCUMENTS_LIST.append(f'{normalize(x.stem)}{x.suffix}')
                KNOWN_EXTENSIONS.add(f'{x.suffix}')
                shutil.move(Path(x.absolute()),
                            Path(FOLDER_PATH, 'Sorted_folder', 'documents', f'{normalize(x.stem)}{x.suffix}'))

            elif x.suffix[1:] in EXTENSIONS_DICT['audio']:
                AUDIO_LIST.append(f'{normalize(x.stem)}{x.suffix}')
                KNOWN_EXTENSIONS.add(f'{x.suffix}')
                shutil.move(Path(x.absolute()),
                            Path(FOLDER_PATH, 'Sorted_folder', 'audio', f'{normalize(x.stem)}{x.suffix}'))

            elif x.suffix[1:] in EXTENSIONS_DICT['video']:
                VIDEO_LIST.append(f'{normalize(x.stem)}{x.suffix}')
                KNOWN_EXTENSIONS.add(f'{x.suffix}')
                shutil.move(Path(x.absolute()),
                            Path(FOLDER_PATH, 'Sorted_folder', 'video', f'{normalize(x.stem)}{x.suffix}'))

            elif x.suffix[1:] in EXTENSIONS_DICT['archives']:
                ARCHIVES_LIST.append(f'{normalize(x.stem)}{x.suffix}')
                KNOWN_EXTENSIONS.add(f'{x.suffix}')
                try:
                    shutil.unpack_archive(Path(x.absolute()),
                                          Path(FOLDER_PATH, 'Sorted_folder', 'archives',
                                               f'{normalize(x.stem)}{x.suffix}'))
                    shutil.move(Path(x.absolute()),
                                Path(FOLDER_PATH, 'Sorted_folder', 'archives', f'{normalize(x.stem)}{x.suffix}'))
                except shutil.ReadError:
                    print(f'Something become WRONG with {x}!')
                    shutil.move(Path(x.absolute()),
                                Path(FOLDER_PATH, 'Sorted_folder', 'archives', f'{normalize(x.stem)}{x.suffix}'))
            else:
                OTHER_LIST.append(f'{normalize(x.stem)}{x.suffix}')
                UNKNOWN_EXTENSIONS.add(f'{x.suffix}')
                shutil.move(Path(x.absolute()),
                            Path(FOLDER_PATH, 'Sorted_folder', f'{normalize(x.stem)}{x.suffix}'))
        elif x.is_dir():
            if x.name not in INNER_FOLDERS_LIST:
                FOLDER_LIST.append(x)
                file_scaner(x)


def main():
    if len(sys.argv) == 2:
        folder_path = Path(sys.argv[1])
        print(f'Start in folder {folder_path}')
        global FOLDER_PATH
        FOLDER_PATH = folder_path
        make_dir_func(Path(folder_path))
        file_scaner(Path(folder_path))
        empty_folder_remover(Path(folder_path))
        print(f'Images: {IMAGES_LIST}')
        print(f'Documents: {DOCUMENTS_LIST}')
        print(f'Audio: {AUDIO_LIST}')
        print(f'Videos: {VIDEO_LIST}')
        print(f'Archives: {ARCHIVES_LIST}')
        print(f'Unknown types: {OTHER_LIST}')

        print(f'Types of files in folder: {KNOWN_EXTENSIONS}')
        print(f'Unknown files of types: {UNKNOWN_EXTENSIONS}')
    else:
        print("You didn't write normal path to your folder. Try again.")




if __name__ == '__main__':
    main()

