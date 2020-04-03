# conan-filament
The Google's Filament Rendering Engine as a conan package.

## Installation

```
git clone https://github.com/luizgabriel/conan-filament.git
cd conan-filament
conan export . google/stable
```

In your conanfile.txt, add:
```
[requires]
filament/1.4.5@google/stable

[imports]
# imports filament tools
bin, * -> ./bin
```

## Requirements
To build Filament, you must first install the following tools:

- CMake 3.15 (or more recent)
- clang 9.0 (or more recent)
- ninja 1.8 (or more recent)

### Necessary Steps (Linux Only)
Make sure you've installed the following dependencies:

- `clang-9` or higher
- `libglu1-mesa-dev`
- `libc++-9-dev` (libcxx-devel and libcxx-static on Fedora) or higher
- `libc++abi-9-dev` (libcxxabi-static on Fedora) or higher
- `ninja-build`
- `libxi-dev`

### Necessary Steps (Windows Only)
Visual Studio 2019 already comes with Clang compiler support as a toolset. So, just add these lines to your conan profile:
```
[settings]
filament:compiler=Visual Studio
filament:compiler.version=16
filament:compiler.toolset=ClangCl
filament:compiler.runtime=MTd
```

In other to this `ClangCl` toolchain to work, you'll need to change the `.conan\settings.yml` file with:
```yml
Visual Studio: &visual_studio
    runtime: [MD, MT, MTd, MDd]
    version: ["8", "9", "10", "11", "12", "14", "15", "16"]
    toolset: [None, v90, v100, v110, v110_xp, v120, v120_xp,
              v140, v140_xp, v140_clang_c2, LLVM-vs2012, LLVM-vs2012_xp,
              LLVM-vs2013, LLVM-vs2013_xp, LLVM-vs2014, LLVM-vs2014_xp,
              LLVM-vs2017, LLVM-vs2017_xp, v141, v141_xp, v141_clang_c2, v142, 
              ClangCl] # <--- add this
    cppstd: [None, 14, 17, 20]
```

Here's an [example project](https://github.com/luizgabriel/Spatial.Engine) were I fully use this package.
