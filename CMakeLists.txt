cmake_minimum_required(VERSION 3.12)
project(leetcode)

include_directories(*/*)

file(GLOB subdirs RELATIVE ${CMAKE_CURRENT_SOURCE_DIR} "problems/*") 
foreach(subdir ${subdirs}) 
    message(${subdir})
    add_subdirectory("${subdir}")
endforeach()

