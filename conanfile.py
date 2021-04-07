from conans import ConanFile

import sometool

# Conan instructions.
class SometoolConan(ConanFile):
    name = "sometool"
    version = "0.1"
    exports = "sometool.py"