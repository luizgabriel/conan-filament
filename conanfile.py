from conans import ConanFile, CMake, tools
from conans.errors import ConanInvalidConfiguration


class FilamentConan(ConanFile):
    name = "filament"
    version = "1.4.3"
    license = "<Put the package license here>"
    author = "<Put your name here> <And your email here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of Filament here>"
    topics = ("<Put some tag here>", "<here>", "<and here>")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "with_filameshio": [True, False]}
    default_options = {"shared": False, "with_filameshio": True}
    generators = "cmake"

    def source(self):
        git = tools.Git(folder="filament")
        git.clone("https://github.com/google/filament.git", "v" + self.version)

        tools.replace_in_file("filament/CMakeLists.txt", "project(TNT)",
                              '''project(TNT)
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()''')

    def _configure_cmake(self):
        toolset = "LLVM" if self.settings.compiler == "Visual Studio" else None
        is_windows = self.settings.os == "Windows"
        valid_toolset = self.settings.compiler.toolset in ["LLVM", "ClangCl"]

        if is_windows and not valid_toolset:
            raise ConanInvalidConfiguration("Only LLVM/ClangCl toolset suported.")

        cmake = CMake(self, toolset=toolset)
        cmake.definitions["ENABLE_JAVA"] = "OFF"
        cmake.configure(source_dir="filament")

        return cmake

    def build(self):
        cmake = self._configure_cmake()
        cmake.build()

    def package(self):
        cmake = self._configure_cmake()
        cmake.install()

    def package_info(self):
        lib_dir = f"lib/{self.settings.arch}"

        self.cpp_info.libdirs = [ lib_dir ]
        self.cpp_info.libs = [
            "filament",
            "backend",
            "bluegl",
            "filabridge",
            "filaflat",
            "utils",
            "geometry",
            "smol-v",
            "ibl"
        ]

        if self.options.with_filameshio:
        	self.cpp_info.libs.append("filameshio");

