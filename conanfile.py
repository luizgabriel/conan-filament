from conans import ConanFile, CMake, tools

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
    build_requires = "cmake_installer/3.14.5@conan/stable"
    options = {flag_to_option(opt): [True, False] for opt in FILAMENT_FLAGS.keys()}
    default_options = {flag_to_option(opt): value for opt, value in FILAMENT_FLAGS.items()}

    def source(self):
        git = tools.Git(folder="filament")
        git.clone("https://github.com/google/filament.git", "v" + self.version)

        tools.replace_in_file("filament/CMakeLists.txt", "project(TNT)",
                              '''project(TNT)
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()''')

    def _configure_cmake(self):
        cmake = CMake(self)

        for flag in FILAMENT_FLAGS.keys():
            cmake.definitions[flag] = "ON" if self.options[flag_to_option(flag)] else "OFF"

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
