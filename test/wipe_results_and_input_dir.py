import pathlib 
from pathlib import Path

from helpers import project_path

results_dir_path = Path.joinpath(project_path, "test/results")
input_dir_path = Path.joinpath(project_path, "test/input")

def rm_tree(pth):
    pth = Path(pth)
    for child in pth.glob('*'):
        if child.is_file():
            child.unlink()
        else:
            rm_tree(child)
    pth.rmdir()

if __name__ == "__main__":
    rm_tree(str(results_dir_path))
    rm_tree(str(input_dir_path))
