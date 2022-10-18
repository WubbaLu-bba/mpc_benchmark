
add_executable(and_test and_test.cpp common/and.cpp)
target_link_libraries(and_test ABY::aby ENCRYPTO_utils::encrypto_utils)
