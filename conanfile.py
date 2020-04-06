from conans import ConanFile, CMake, tools
import os

FILAMENT_FLAGS = {
    "FILAMENT_ENABLE_JAVA": False,
    "FILAMENT_SKIP_SAMPLES": True,
    "FILAMENT_ENABLE_LTO": False,
    "FILAMENT_BUILD_FILAMAT": False,
    "FILAMENT_SUPPORTS_METAL": False,
    "FILAMENT_SUPPORTS_VULKAN": False,
    "FILAMENT_GENERATE_JS_DOCS": False,
    "FILAMENT_INSTALL_BACKEND_TEST": False,
    "FILAMENT_USE_EXTERNAL_GLES3": False,
}


def flag_to_option(flag):
    return flag.replace("FILAMENT_", "").lower()

class FilamentConan(ConanFile):
    name = "filament"
    version = "1.5.2"
    license = "Apache License 2.0"
    homepage = "https://github.com/google/filament"
    url = "https://github.com/luizgabriel/conan-filament"
    description = "Filament is a real-time physically based rendering engine for Android, iOS, Windows, Linux, " \
                  "macOS and WASM/WebGL "
    topics = ("graphics", "3d", "filament", "google")
    settings = ("os", "compiler", "build_type", "arch")
    generators = "cmake"
    build_requires = "cmake_installer/3.15.5@conan/stable"
    options = {flag_to_option(opt): [True, False] for opt in FILAMENT_FLAGS.keys()}
    default_options = {flag_to_option(opt): value for opt, value in FILAMENT_FLAGS.items()}

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

    def _cmake_define(self, cmake, definition):
        option = definition.replace("FILAMENT_", "").lower()
        cmake.definitions[definition] = "ON" if self.options[option] else "OFF"

    def _configure_cmake(self):
        cmake = CMake(self, toolset=self.opt_toolset)
        cmake.definitions["CONAN_DISABLE_CHECK_COMPILER"] = "ON"

        for flag in FILAMENT_FLAGS.keys():
            cmake.definitions[flag] = "ON" if self.options[flag_to_option(flag)] else "OFF"

        cc = self.env.get("CC", None)
        if cc and os.path.exists(cc):
            cmake.definitions["CMAKE_C_COMPILER"] = cc

        cxx = self.env.get("CXX", None)
        if cxx and os.path.exists(cxx):
            cmake.definitions["CMAKE_CXX_COMPILER"] = cxx

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
