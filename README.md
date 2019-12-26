# conan-filament
The Google's Filament Rendering Engine as a conan package.

### Installation

```
git clone https://github.com/luizgabriel/conan-filament.git
cd conan-filament
conan create . google/stable
```
You will need to configure the clang compiler as a conan profile. If you're on windows I recomend you to use the `clang-cl` installed as Visual Studio toolchain ([LLVM](marketplace.visualstudio.com/items?itemName=LLVMExtensions.llvm-toolchain)).

In your conanfile.txt, add:
```
[requires]
filament/1.4.3@google/stable

[imports]
# imports filament tools
bin, * -> ./bin
```

If you'll need
