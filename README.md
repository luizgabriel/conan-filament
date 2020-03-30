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

- CMake 3.10 (or more recent)
- clang 7.0 (or more recent)
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
If you're using Windows, you'll need some extra steps to make it work. By default, Conan will look for a MinGW installation looking for GCC, and that's not what we want. You'll need to configure a special conan profile to be able with compile correctly this package. So, find the profiles folder in `C:\\Users\%USERNAME%\.conan\profiles` and create a file called `clang` (without extension) and put this:
```
[settings]
os=Windows
os_build=Windows
arch=x86_64
arch_build=x86_64

compiler=Visual Studio
compiler.version=16
compiler.toolset=LLVM
compiler.runtime=MTd

build_type=Debug
```

Requirements:
- Visual Studio 2019 and 2017 (Yes, both)
- The [LLVM Toolchain](https://marketplace.visualstudio.com/items?itemName=LLVMExtensions.llvm-toolchain)

In other to this `LLVM` toolchain to work, you'll need to change the `.conan\settings.yml` file with:
```yml
Visual Studio: &visual_studio
    runtime: [MD, MT, MTd, MDd] # <--- Add "MT" and "MTd"
    version: ["8", "9", "10", "11", "12", "14", "15", "16"]
    toolset: [None, v90, v100, v110, v110_xp, v120, v120_xp,
              v140, v140_xp, v140_clang_c2, LLVM-vs2012, LLVM-vs2012_xp,
              LLVM-vs2013, LLVM-vs2013_xp, LLVM-vs2014, LLVM-vs2014_xp,
              LLVM-vs2017, LLVM-vs2017_xp, v141, v141_xp, v141_clang_c2, v142, 
              ClangCl, LLVM] # <--- add this
    cppstd: [None, 14, 17, 20]
```

Now, just:
```sh
conan create . google/stable -pr=clang
```
This command will export the package and build with the clang profile. Now you'll just need to integrate it in you project. 
Here's an [example project](https://github.com/luizgabriel/Spatial.Engine) were I fully use this package.
