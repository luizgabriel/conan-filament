# Filament Conan Package
The Google's [Filament](https://github.com/google/filament) Rendering Engine as a conan package.

## Installation

```shell script
git clone https://github.com/google/filament conan-filament && cd conan-filament
conan export . google/stable
```

In your conanfile.txt, add:
```
[requires]
filament/1.7.0@google/stable

[imports]
# imports filament tools
bin, * -> ./bin
```

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

Recommended profile settings:
```
[settings]
compiler=Visual Studio
compiler.version=16
compiler.runtime=MTd
```

Here's an [example project](https://github.com/luizgabriel/Spatial.Engine) were I fully use this package.
