from conans import ConanFile

class Package_2Conan(ConanFile):
    name = "package_2"
    version = "0.1"

    requires = "package_1/0.1"
    python_requires = "sometool/[>0.0]"

    settings = "os", "compiler", "build_type", "arch"

    exports = "config.py"

    def build(self):
        sometool = self.python_requires["sometool"].module.sometool
        sometool.configure(self.recipe_folder)
        sometool.build()

    def test(self):
        return
