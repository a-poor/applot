#!/usr/bin/env python
import os
import pathlib
import argparse

def rmr(path):
    if not path.is_dir():
        path.unlink()
    else:
        for p in path.glob("*"):
            if p.is_dir():
                rmr(p)
            else:
                p.unlink()
        path.rmdir()

WORK_DIR = pathlib.Path(__file__).parent.absolute()

CLEAN_FILES = [
    "dist/*",
    "build/*",
    "*.egg-info",
    "__pycache__",
    ".ipynb_checkpoints",
    ".pytest_cache"
]

BUILD_CMD = "python setup.py sdist bdist_wheel"
UPLOAD_CMD = "python -m twine upload --repository pypi dist/*"

def build():
    os.system(BUILD_CMD)

def upload():
    os.system(UPLOAD_CMD)

def clean():
    for pattern in CLEAN_FILES:
        for path in WORK_DIR.rglob(pattern):
            rmr(path)

def run_all():
    build()
    upload()
    clean()

FUNCTIONS = {
    'build':  build,
    'upload': upload,
    'clean':  clean,
    'all':    run_all
}


parser = argparse.ArgumentParser()
parser.add_argument(
    "cmd",
    default="all",
    nargs="*",
    choices=FUNCTIONS.keys(),
    help=f"""Function to call:
    build  -> build module "{BUILD_CMD}"
    upload -> upload to PyPi "{UPLOAD_CMD}"
    clean  -> remove any of the following: {CLEAN_FILES}
    all    -> build() then upload() then clean()
    """
)

args = parser.parse_args()
if 'all' in args.cmd:
    run_all()
else:
    for cmd in args.cmd:
        fn = FUNCTIONS.get(cmd,None)
        if fn is None:
            raise Exception("ERROR: Couldn't find function: " + cmd)
        fn()

print("done.")
