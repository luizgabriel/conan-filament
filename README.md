# conan-filament
The Google's Filament Rendering Engine as a conan package.

### Installation

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

### Necessary Steps (Windows Only)
If you're using Windows, you'll need some extra steps to make it work. By default, Conan will look for a MinGW installation looking for GCC, and that's not what we want. You'll need to configure a special conan profile to be able with compile correctly this engine. So, find the profiles folder in `C:\\Users\%USERNAME%\.conan\profiles` and create a file called `clang` (without extension) and put this:
```
[settings]
os=Windows
os_build=Windows
arch=x86_64
arch_build=x86_64

compiler=Visual Studio
compiler.version=16
compiler.toolset=ClangCl
compiler.runtime=MTd
compiler.cppstd=17

build_type=Release

[options]

[build_requires]

[env]
CC=C:/PROGRA~1/LLVM/bin/clang-cl.exe
CXX=C:/PROGRA~1/LLVM/bin/clang-cl.exe
```

You'll need do install [Visual Studio 2019 Community](https://visualstudio.microsoft.com/pt-br/downloads/)
  > Make sure to mark these options:
  >
  > ![LLVM Option](https://devblogs.microsoft.com/cppblog/wp-content/uploads/sites/9/2019/04/Clang-Compilers-for-Windows-Installer-Annotated.png)
  
Then download [LLVM](http://releases.llvm.org/download.html) and [CMake](https://cmake.org/download/)

Now, just:
```sh
conan create . google/stable -pr=clang
```
This command will export the package and build with the clang profile. Now you'll just need to integrate it in you project. Here's an [example project](https://github.com/luizgabriel/Spatial.Engine) were I fully use this package.
