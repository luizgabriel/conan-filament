# Filament Conan Package
The Google's [Filament](https://github.com/google/filament) Rendering Engine as a conan package.

## Installation

Make sure to follow the [build prerequisites]([https://github.com/google/filament](https://github.com/google/filament/blob/main/BUILDING.md#prerequisites)).

```shell script
git clone https://github.com/luizgabriel/conan-filament && cd conan-filament
conan export . --user google --channel stable
```

In your conanfile.txt, add:
```
[requires]
filament/1.35.0@google/stable

[imports]
# imports filament tools
bin, * -> ./bin
```

Here's an [example project](https://github.com/luizgabriel/Spatial.Engine) were I fully use this package.
