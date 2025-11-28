from conan import ConanFile
from conan.tools.cmake import CMake, cmake_layout
from conan.tools.files import copy

class DarkMetalConanFile(ConanFile):
    name = "darkmetal-engine"
    version = "1.0.0"
    url = "https://github.com/Subject9x/darkmetal-engine"
    license = "GPL-2.0-only"
    build_requires = "cmake/4.3.2"
    requires = "sdl/2.32.10"
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeToolchain", "CMakeDeps"

    def layout(self):
        cmake_layout(self)

    def build(self):
        cmake = CMake(self)
        cmake.configure(cli_args=["-DCMAKE_POLICY_VERSION_MINIMUM=3.5"])
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.configure(cli_args=["-DCMAKE_POLICY_VERSION_MINIMUM=3.5"])
        cmake.install()
