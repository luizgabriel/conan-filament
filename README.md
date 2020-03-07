# conan-filament
The Google's Filament Rendering Engine as a conan package.

### Installation

```
git clone https://github.com/luizgabriel/conan-filament.git
cd conan-filament
conan create . google/stable
```

In your conanfile.txt, add:
```
[requires]
filament/1.4.5@google/stable

[imports]
# imports filament tools
bin, * -> ./bin
```
