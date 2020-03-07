from conans import ConanFile, CMake, tools
from conans.errors import ConanInvalidConfiguration


class FilamentConan(ConanFile):
    name = "filament"
    version = "1.4.5"
    license = "Apache License 2.0"
    homepage = "https://github.com/google/filament"
    url = "https://github.com/luizgabriel/conan-filament"
    description = "Filament is a real-time physically based rendering engine for Android, iOS, Windows, Linux, macOS and WASM/WebGL"
    topics = ("graphics", "3d", "filament", "google")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = {"shared": False}
    generators = "cmake"

    def source(self):
        git = tools.Git(folder="filament")
        git.clone("https://github.com/google/filament.git", "v" + self.version)

        tools.replace_in_file("filament/CMakeLists.txt", "project(TNT)",
                              '''project(TNT)
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()''')

    def _configure_cmake(self):
        cmake = CMake(self)
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
	    # Required to link with filament
            "filament",
            "backend",
            "bluegl",
            "filabridge",
            "filaflat",
            "utils",
            "geometry",
            "smol-v",
            "ibl",
		
	    # Extra lib tools
	    "filamat",
            "filameshio",
            "gltfio",
            "gltfio_core",
            "image",
            "matdbg",
            "meshoptimizer",
            "rays",
            "shaders",
        ]

