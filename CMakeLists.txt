CMAKE_MINIMUM_REQUIRED(VERSION 3.0)

include(RezBuild)
include(RezRepository)
include(ExternalProject)

# yaml-cpp
rez_set_archive(
    YAMLCPP_URL yaml_cpp/yaml-cpp-yaml-cpp-${REZ_BUILD_PROJECT_VERSION}.tar.gz
    https://github.com/jbeder/yaml-cpp/archive/yaml-cpp-${REZ_BUILD_PROJECT_VERSION}.tar.gz
)

# The environment variable REZ_TMP_PATH is meant to point to a location such as "/tmp/rez".
set(EXTRACT_DIR $ENV{REZ_TMP_PATH}/yaml_cpp/${REZ_BUILD_PROJECT_VERSION})
set(BUILD_DIR ${EXTRACT_DIR}/build)

# We configure/build/install yaml-cpp through the ExternalProject_Add macro,
# using three different shell scripts for each of these steps.
# If necessary, it is possible to skip one of these steps by replacing the command
# by "", an empty string.
ExternalProject_Add(
    REZ_YAMLCPP
    URL ${YAMLCPP_URL}
    PREFIX yaml_cpp
    SOURCE_DIR ${EXTRACT_DIR}
    PATCH_COMMAND ""
    UPDATE_COMMAND ""
    CONFIGURE_COMMAND bash ${CMAKE_SOURCE_DIR}/configure.sh ${EXTRACT_DIR} ${BUILD_DIR}
    BUILD_COMMAND bash ${CMAKE_SOURCE_DIR}/build.sh ${BUILD_DIR}
    INSTALL_COMMAND bash ${CMAKE_SOURCE_DIR}/install.sh ${BUILD_DIR}
)

# We use a bogus CMake "install" step in order to be able to properly finish
# and get out of the CMake script.
install(
    CODE
    "execute_process(
        COMMAND echo \"\n[CMAKE] yaml-cpp-${REZ_BUILD_PROJECT_VERSION} PACKAGE SETUP FINISHED!\n\"
    )"
)
