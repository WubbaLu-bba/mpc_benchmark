
add_executable(xor_test xor_test.cpp common/xor.cpp)
target_link_libraries(xor_test ABY::aby ENCRYPTO_utils::encrypto_utils)
