cmake_minimum_required(VERSION 3.16.1)
project(letcode)
set(THISDIR ${CMAKE_SOURCE_DIR})
file(GLOB SOURCE ${THISDIR}/../source/*.cpp)
include_directories(${THISDIR}/../include)
foreach (file ${SOURCE}) 
    get_filename_component(BASENAME ${file} NAME_WLE )
    message(STATUS ${BASENAME})
    add_executable(${BASENAME} ${file})
    set_target_properties(${BASENAME} PROPERTIES RUNTIME_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/bin")
endforeach()


