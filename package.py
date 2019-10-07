name = "yaml_cpp"

version = "0.5.3"

authors = [
    "Jesse Beder"
]

description = \
    """
    yaml-cpp is a YAML parser and emitter in C++ matching the YAML 1.2 spec.
    """

requires = [
    "boost-1.61+",
    "cmake-3+",
    "gcc-6+",
    "python-2.7<3"
]

variants = [
    ["platform-linux"]
]

build_system = "cmake"

with scope("config") as config:
    config.build_thread_count = "logical_cores"

uuid = "yaml_cpp-{version}".format(version=str(version))

def commands():
    env.LD_LIBRARY_PATH.prepend("{root}/lib")
    env.PKG_CONFIG_PATH.prepend("{root}/lib/pkgconfig")

    # Helper environment variables.
    env.YAMLCPP_INCLUDE_PATH.set("{root}/include")
    env.YAMLCPP_LIBRARY_PATH.set("{root}/lib")
