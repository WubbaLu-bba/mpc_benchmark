
add_executable(mult_test mult_test.cpp common/mult.cpp)
target_link_libraries(mult_test ABY::aby ENCRYPTO_utils::encrypto_utils)
