from conans import ConanFile

class SometoolTestConan(ConanFile):
    python_requires = "sometool/[>0.0]"

    settings = "os", "compiler", "build_type", "arch"

    def build(self):
        sometool = self.python_requires["sometool"].module.sometool
        sometool.configure(self.recipe_folder)
        sometool.build()

    def test(self):
        return
