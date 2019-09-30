cmake_minimum_required(VERSION 3.5)

project(module)

# Find default python libraries and interpreter
set(Python_ADDITIONAL_VERSIONS 3.5)
find_package(PythonInterp 3.5 REQUIRED)
find_package(PythonLibs 3.5 REQUIRED)
find_package(Boost COMPONENTS python-py35 REQUIRED)

include_directories(${Boost_INCLUDE_DIR} ${PYTHON_INCLUDE_DIRS})
link_directories(${Boost_LIBRARY_DIR})

# Build and link the module
add_library(module SHARED module.cpp)
target_link_libraries(module ${Boost_LIBRARIES} ${PYTHON_LIBRARIES})

# Tweaks the name of the library to match what Python expects
set_target_properties(module PROPERTIES SUFFIX .so)
set_target_properties(module PROPERTIES PREFIX "")
