cmake_minimum_required(VERSION 3.5)

project(module)

# Find default python libraries and interpreter
set(Python_ADDITIONAL_VERSIONS 3.7)
find_package(PythonInterp 3.7 REQUIRED)
find_package(PythonLibs 3.7 REQUIRED)
find_package(Boost COMPONENTS python37 REQUIRED)

include_directories(${Boost_INCLUDE_DIR} ${PYTHON_INCLUDE_DIRS})
link_directories(${Boost_LIBRARY_DIR})

# Build and link the module
add_library(module SHARED module.cpp)
target_link_libraries(module pthread ${Boost_LIBRARIES} ${PYTHON_LIBRARIES})

# Tweaks the name of the library to match what Python expects
set_target_properties(module PROPERTIES SUFFIX .so)
set_target_properties(module PROPERTIES PREFIX "")

# Set C++14 support
set_target_properties(module PROPERTIES CXX_STANDARD 14)
