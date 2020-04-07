# conan-filament
The Google's Filament Rendering Engine as a conan package.

## Installation

In your conanfile.txt, add:
```
[requires]
filament/1.5.2@google/stable

[imports]
# imports filament tools
bin, * -> ./bin
```

## Requirements
To build Filament, you must first install the following tools:

- CMake 3.14 (or more recent)
- clang 9.0 (or more recent)
- ninja 1.8 (or more recent)

### Necessary Steps (Linux Only)
Make sure you've installed the following dependencies:

- `clang-7` or higher
- `libglu1-mesa-dev`
- `libc++-7-dev` (libcxx-devel and libcxx-static on Fedora) or higher
- `libc++abi-7-dev` (libcxxabi-static on Fedora) or higher
- `ninja-build`
- `libxi-dev`

### Necessary Steps (Windows Only)

Requirements:
- Visual Studio 2019
- LLVM

Recommended profile settings:
```
[settings]
compiler=Visual Studio
compiler.version=16
compiler.runtime=MTd
```

Here's an [example project](https://github.com/luizgabriel/Spatial.Engine) were I fully use this package.
