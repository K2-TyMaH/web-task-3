import argparse
from pathlib import Path
from shutil import copyfile
from threading import Thread
import logging

"""
py main.py --source -s picture
py main.py --output -o dist
"""

EXTENSIONS_DICT = {'images': ('jpeg', 'png', 'jpg', 'svg'),
                   'documents': ('doc', 'docx', 'txt', 'pdf', 'xlsx', 'pptx'),
                   'audio': ('mp3', 'ogg', 'wav', 'amr'),
                   'video': ('avi', 'mp4', 'mov', 'mkv'),
                   'archives': ('zip', 'gz', 'tar', 'rar')}

known_extensions = []
for k, v in EXTENSIONS_DICT.items():
    for item in v:
        known_extensions.append(item)

parser = argparse.ArgumentParser(description="App for sorting folder")
parser.add_argument("-s", "--source", required=True)
parser.add_argument("-o", "--output", default="Sorted")
args = vars(parser.parse_args())
source = args.get("source")
output = args.get("output")

folders = []

def copirator(path: Path):
    for el in path.iterdir():
        if el.is_file():
            et = el.suffix[1:]
            
            if et not in known_extensions:
                new_path = output_folder / "Others"                
                try:
                    new_path.mkdir(exist_ok=True, parents=True)
                    copyfile(el, new_path / el.name)
                except OSError as e:
                    logging.error(e)

            for k, v in EXTENSIONS_DICT.items():    
                if et in v:
                    new_path = output_folder / k                
                    try:
                        new_path.mkdir(exist_ok=True, parents=True)
                        copyfile(el, new_path / el.name)
                    except OSError as e:
                        logging.error(e)
           

def grabs_folder(path: Path):
    for el in path.iterdir():
        if el.is_dir():
            folders.append(el)
            grabs_folder(el)

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format="%(threadName)s %(message)s")
    base_folder = Path(source)
    output_folder = Path(output)

    folders.append(base_folder)
    grabs_folder(base_folder)

    threads = []
    for folder in folders:
        th = Thread(target=copirator, args=(folder,))
        th.start()
        threads.append(th)

    [th.join() for th in threads]


