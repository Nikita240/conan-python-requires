from conans import ConanFile

class Package_1Conan(ConanFile):
    name = "package_1"
    version = "0.1"

    python_requires = "sometool/[>0.0]"

    settings = "os", "compiler", "build_type", "arch"

    exports = "config.py"

    def build(self):
        sometool = self.python_requires["sometool"].module.sometool
        sometool.configure(self.recipe_folder)
        sometool.build()

    def test(self):
        return
