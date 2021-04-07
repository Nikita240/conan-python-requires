from conans import ConanFile
from pathlib import Path

class SometoolTestConan(ConanFile):
    python_requires = "sometool/[>0.0]"

    settings = "os", "compiler", "build_type", "arch"

    def build(self):
        sometool = self.python_requires["sometool"].module.sometool
        print(sometool.what_module_am_i())

    def test(self):
        return


