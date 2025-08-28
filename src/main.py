import os
import shutil
from gencontent import *
def copy_static(src, dst):
    if not os.path.exists(src):
        raise FileNotFoundError(src)
    if os.path.exists(dst):
        shutil.rmtree(dst)
    os.mkdir(dst)
    _copy_dir(src, dst)

def _copy_dir(src, dst):    
    for name in os.listdir(src):
        src_path = os.path.join(src, name)
        dst_path = os.path.join(dst, name)
        if os.path.isfile(src_path):
            shutil.copy(src_path, dst_path)
        else: 
            os.mkdir(dst_path)
            _copy_dir(src_path, dst_path)


def main():
    if os.path.exists("public"):
        shutil.rmtree('public')
    shutil.copytree("static", "public", dirs_exist_ok=True)
    generate_pages_recursive("content", "template.html", "public")


if __name__ == "__main__":
    main()
