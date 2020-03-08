from conans import ConanFile, CMake, tools
from conans.errors import ConanInvalidConfiguration


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
        "enable_java": [True, False],

        "with_filamat": [True, False],
        "with_filameshio": [True, False],
        "with_gltfio": [True, False],
        "with_gltfio_core": [True, False],
        "with_image": [True, False],
        "with_matdbg": [True, False],
        "with_meshoptimizer": [True, False],
        "with_rays": [True, False],
        "with_shaders": [True, False],

        "with_sdl": [True, False],
        "with_imgui": [True, False]
    }
    default_options = {
        "shared": False,
        "enable_java": False,

        "with_filamat": False,
        "with_filameshio": False,
        "with_gltfio": False,
        "with_gltfio_core": False,
        "with_image": False,
        "with_matdbg": False,
        "with_meshoptimizer": False,
        "with_rays": False,
        "with_shaders": False,

        "with_sdl": False,
        "with_imgui": False
    }
    generators = "cmake"

    def source(self):
        git = tools.Git(folder="filament")
        git.clone("https://github.com/google/filament.git", "v" + self.version)

        tools.replace_in_file("filament/CMakeLists.txt", "project(TNT)",
                              '''project(TNT)
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()''')

    def _configure_cmake(self):
        toolset = self.settings.compiler.toolset if self.settings.compiler == "Visual Studio" else None
        is_windows = self.settings.os == "Windows"
        is_valid_toolset = toolset in ["LLVM", "ClangCl"]

        if is_windows and not is_valid_toolset:
            raise ConanInvalidConfiguration("Only LLVM/ClangCl toolset supported.")

        cmake = CMake(self)
        cmake.definitions["ENABLE_JAVA"] = "ON" if self.options["enable_java"] else "OFF"
        cmake.definitions["BUILD_TESTING"] = "OFF"
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
            # Required to link with filament
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

        # Extra lib tools
        extra_libs = ["filamat", "filameshio", "gltfio", "gltfio_core", "image", "matdbg", "meshoptimizer",
                      "rays", "shaders"]
        for extra_lib in extra_libs:
            if self.options["with_" + extra_lib]:
                self.cpp_info.libs.append(extra_lib)

        # External integrated libs
        if self.options["with_sdl"]:
            self.cpp_info.libs.append("sdl2")
            self.cpp_info.libs.append("sdl2main")
