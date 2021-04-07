import sys
from importlib.machinery import SourceFileLoader, FileFinder, SOURCE_SUFFIXES
from importlib.util import module_from_spec

files_to_compile = []

def add_file(file):
    files_to_compile.append(file)

def configure(root_folder):
    finder = FileFinder(root_folder, (SourceFileLoader, SOURCE_SUFFIXES))
    spec = finder.find_spec("config")
    config_module = module_from_spec(spec)
    spec.loader.exec_module(config_module)

    config_module.setup(sys.modules[__name__])

def build():
    for file in files_to_compile:
        print("building %s" % file)