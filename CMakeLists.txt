cmake_minimum_required(VERSION 3.20)
project(VeritasLabNative LANGUAGES CXX)
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_library(heat_kernel SHARED src/kernels/heat_kernel.cpp)
target_include_directories(heat_kernel PUBLIC include)
