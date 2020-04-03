import os

from conans import ConanFile, CMake, tools
from conans.errors import ConanInvalidConfiguration, ConanException


class FilamentConan(ConanFile):
    name = "filament"
    version = "1.4.5"
    license = "Apache License 2.0"
    homepage = "https://github.com/google/filament"
    url = "https://github.com/luizgabriel/conan-filament"
    description = "Filament is a real-time physically based rendering engine for Android, iOS, Windows, Linux, " \
                  "macOS and WASM/WebGL "
    topics = ("graphics", "3d", "filament", "google")
    settings = ("os", "compiler", "build_type", "arch")
    options = {
        "shared": [True, False],
        "enable_java": [True, False]
    }
    default_options = {
        "shared": False,
        "enable_java": False
    }
    generators = "cmake"
    #build_requires = "cmake_installer/3.15.5@conan/stable"

    def source(self):
        git = tools.Git(folder="filament")
        git.clone("https://github.com/google/filament.git", "v" + self.version)

        tools.replace_in_file("filament/CMakeLists.txt", "project(TNT)",
                              '''project(TNT)
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()''')
        
    @property
    def opt_toolset(self):
        return self.settings.get_safe("compiler.toolset")

    def _configure_cmake(self):
        cmake = CMake(self, toolset=self.opt_toolset)
        cmake.definitions["ENABLE_JAVA"] = "ON" if self.options["enable_java"] else "OFF"
        cmake.definitions["BUILD_TESTING"] = "OFF"
        cmake.definitions["CONAN_DISABLE_CHECK_COMPILER"] = "ON"
            
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

        self.cpp_info.libdirs = [lib_dir]
        self.cpp_info.libs = [
            "backend", "filamat", "gltfio", "meshoptimizer",
            "bluegl", "gltfio_core", "rays",
            "camutils", "filament", "ibl", "shaders",
            "filabridge", "filameshio", "image", "smol-v",
            "filaflat", "geometry", "matdbg", "utils",
        ]
