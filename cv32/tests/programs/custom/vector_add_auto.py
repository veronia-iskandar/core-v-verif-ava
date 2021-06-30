import os
import random

a = random.randint(0, 15)
b = random.randint(0, 15)
c = random.randint(0, 15)
d = random.randint(0, 15)
e = random.randint(0, 15)
f = random.randint(0, 15)
g = random.randint(0, 15)
h = random.randint(0, 15)

cFile = open("/home/veronia/core-v-verif-ava/cv32/tests/programs/custom/vector_add_sadd_auto/vector_add_sadd_auto.c", "w")

header="#include <stdint.h>\n#include <stdio.h>\n#include <stdlib.h>\n"

result = a + b	
add_vv_test_e8_m1 = "int add_vv_test_e8_m1(void)\n{\nuint8_t result;\nasm volatile (\n\"li t1, 64 \\n\\t\"\n\"vsetvli t0, t1, e16, m1 \\n\\t\"\n\"vmv.v.i v1, " +str(a)+ " \\n\\t\"\n\"vmv.v.i v2, " + str(b) + " \\n\\t\"\n\"vadd.vv v3, v1, v2 \\n\\t\"\n\"vmv.x.s %0, v3\"\n: \"=r\" (result) \n);\nif(result != " + str(result) + ")\n{\nprintf(\"Fail: %d\\n\", result);\nreturn(1);\n}\nelse\n{\nprintf(\"Pass: %d\\n\", result);\nreturn(0);\n}\n}\n"

add_vv_test_e16_m1 = " int add_vv_test_e16_m1(void)\n{\n  uint8_t result;\n  asm volatile (\n      \"li t1, 64 \\n\\t\"\n      \"vsetvli t0, t1, e16, m1 \\n\\t\"\n      \"vmv.v.i v1, " +str(a)+ " \\n\\t\"\n      \"vmv.v.i v2, " +str(b)+ " \\n\\t\"\n      \"vadd.vv v3, v1, v2 \\n\\t\"\n      \"vmv.x.s %0, v3\"\n      : \"=r\" (result) \n  );\n  if(result != " +str(result)+ ")\n{\n    printf(\"Fail: %d\\n\", result);\n    return(1);\n}\nelse\n{\n    printf(\"Pass: %d\\n\", result);\n    return(0);\n}\n}"

add_vv_test_e32_m1 = "int add_vv_test_e32_m1(void)\n{\n  uint8_t result;\n  asm volatile (\n      \"li t1, 64 \\n\\t\"\n      \"vsetvli t0, t1, e32, m1 \\n\\t\"\n      \"vmv.v.i v1, "+str(a)+" \\n\\t\"\n      \"vmv.v.i v2, "+str(b)+" \\n\\t\"\n      \"vadd.vv v3, v1, v2 \\n\t\"\n      \"vmv.x.s %0, v3\"\n      : \"=r\" (result) \n  );\n  if(result != "+str(result)+")\n  {\n      printf(\"Fail: %d\\n\", result);\n      return(1);\n  }\n  else\n  {\n      printf(\"Pass: %d\\n\", result);\n      return(0);\n  }\n}"

result0 = a + c
result1 = b + d
add_vv_test_e8_m2 = "int add_vv_test_e8_m2(void)\n{\nuint8_t result0 = 0, result1 = 0;\nasm volatile (\n\"li t1, 64 \\n\\t\"\n\"vsetvli t0, t1, e8, m1 \\n\\t\"\n\"vmv.v.i v2, " + str(a)+ " \\n\\t\"\n\"vmv.v.i v3, " + str(b)+ " \\n\\t\"\n\"vmv.v.i v4, " + str(c)+" \\n\\t\"\n\"vmv.v.i v5, " +str(d)+ " \\n\\t\"\n\"vsetvli t0, t1, e8, m2 \\n\\t\"\n\"vadd.vv v6, v2, v4 \\n\\t\"\n\"vsetvli t0, t1, e8, m1 \\n\\t\"\n\"vmv.x.s %0, v6\\n\\t\"\n\"vmv.x.s %1, v7\\n\\t\"\n: \"=r\" (result0), \"=r\" (result1)\n);\nif(result0 != "+str(result0)+" || result1 != "+str(result1)+")\n{\nprintf(\"Test Failed! Results: %d\\t%d\\n\", result0, result1);\nreturn(1);\n}\nelse\n{\nprintf(\"Pass: %d\\t%d\\n\", result0, result1);\nreturn(0);\n}\n}"

add_vv_test_e16_m2 = "int add_vv_test_e16_m2(void)\n{\n  uint8_t result0 = 0, result1 = 0;\n  asm volatile (\n      \"li t1, 64 \\n\\t\"\n      \"vsetvli t0, t1, e16, m1 \\n\\t\"\n      \"vmv.v.i v2, "+str(a)+" \\n\\t\"\n      \"vmv.v.i v3, "+str(b)+" \\n\\t\"\n      \"vmv.v.i v4, "+str(c)+" \\n\\t\"\n      \"vmv.v.i v5, "+str(d)+" \\n\\t\"\n      \"vsetvli t0, t1, e16, m2 \\n\\t\"\n      \"vadd.vv v6, v2, v4 \\n\\t\"\n      \"vsetvli t0, t1, e16, m1 \\n\\t\"\n      \"vmv.x.s %0, v6\\n\\t\"\n      \"vmv.x.s %1, v7\\n\\t\"\n      : \"=r\" (result0), \"=r\" (result1)\n  );\n  if(result0 != "+str(result0)+" || result1 != "+str(result1)+")\n  {\n     printf(\"Test Failed! Results: %d\\t%d\\n\", result0, result1);\n   return(1);\n}\nelse\n{\n   printf(\"Pass: %d\\t%d\\n\", result0, result1);\n return(0);\n}\n}"

add_vv_test_e32_m2 = "int add_vv_test_e32_m2(void)\n{\n  uint8_t result0 = 0, result1 = 0;\n  asm volatile (\n      \"li t1, 64 \\n\\t\"\n      \"vsetvli t0, t1, e32, m1 \\n\\t\"\n    \"vmv.v.i v2, "+str(a)+" \\n\\t\"\n    \"vmv.v.i v3, "+str(b)+" \\n\\t\"\n    \"vmv.v.i v4, "+str(c)+" \\n\\t\"\n    \"vmv.v.i v5, "+str(d)+" \\n\\t\"\n    \"vsetvli t0, t1, e32, m2 \\n\\t\"\n    \"vadd.vv v6, v2, v4 \\n\\t\"\n    \"vsetvli t0, t1, e32, m1 \\n\\t\"\n    \"vmv.x.s %0, v6\\n\\t\"\n    \"vmv.x.s %1, v7\\n\\t\"\n    : \"=r\" (result0), \"=r\" (result1)\n);\nif(result0 != "+str(result0)+" || result1 != "+str(result1)+")\n{\n      printf(\"Test Failed! Results: %d\\t%d\\n\", result0, result1);\n      return(1);\n  }\n  else\n  {\n      printf(\"Pass: %d\\t%d\\n\", result0, result1);\n      return(0);\n  }\n}"

result0= a + e
result1= b + f
result2= c + g
result3= d + h

add_vv_test_e8_m4 = "int add_vv_test_e8_m4(void)\n{\nuint8_t result0, result1, result2, result3;\nasm volatile (\n\"li t1, 64 \\n\\t\"\n\"vsetvli t0, t1, e8, m1 \\n\\t\"\n\"vmv.v.i v4, " +str(a)+ " \\n\\t\"\n\"vmv.v.i v5, "+str(b)+" \\n\\t\"\n\"vmv.v.i v6, "+str(c)+" \\n\\t\"\n\"vmv.v.i v7, "+str(d)+" \\n\\t\"\n\"vmv.v.i v8, "+str(e)+" \\n\\t\"\n\"vmv.v.i v9, "+str(f)+" \\n\\t\"\n\"vmv.v.i v10, "+str(g)+" \\n\\t\"\n\"vmv.v.i v11, "+str(h)+" \\n\\t\"\n\"vsetvli t0, t1, e8, m4 \\n\\t\"\n\"vadd.vv v12, v4, v8 \\n\\t\"\n\"vsetvli t0, t1, e8, m1 \\n\\t\"\n\"vmv.x.s %0, v12\\n\\t\"\n\"vmv.x.s %1, v13\\n\\t\"\n\"vmv.x.s %2, v14\\n\\t\"\n\"vmv.x.s %3, v15\\n\\t\"\n: \"=r\" (result0), \"=r\" (result1), \"=r\" (result2), \"=r\" (result3)\n);\nif(result0 != "+str(result0)+" || result1 != "+str(result1)+" || result2 != "+str(result2)+" || result3 != "+str(result3)+")\n{\n  printf(\"Test Failed! Results: %d %d %d %d\\n\", result0, result1, result2, result3);\nreturn(1);\n}\nelse\n{\n  printf(\"Pass: %d %d %d %d\\n\", result0, result1, result2, result3);\nreturn(0);\n}\n}"


add_vv_test_e16_m4 = "int add_vv_test_e16_m4(void)\n{\n  uint8_t result0, result1, result2, result3;\n  asm volatile (\n      \"li t1, 64 \\n\\t\"\n      \"vsetvli t0, t1, e16, m1 \\n\\t\"\n      \"vmv.v.i v4, "+str(a)+" \\n\\t\"\n      \"vmv.v.i v5, "+str(b)+" \\n\\t\"\n      \"vmv.v.i v6, "+str(c)+" \\n\\t\"\n      \"vmv.v.i v7, "+str(d)+" \\n\\t\"\n      \"vmv.v.i v8, "+str(e)+" \\n\\t\"\n      \"vmv.v.i v9, "+str(f)+" \\n\\t\"\n      \"vmv.v.i v10, "+str(g)+" \\n\\t\"\n      \"vmv.v.i v11, "+str(h)+" \\n\\t\"\n      \"vsetvli t0, t1, e16, m4 \\n\\t\"\n      \"vadd.vv v12, v4, v8 \\n\\t\"\n      \"vsetvli t0, t1, e16, m1 \\n\\t\"\n      \"vmv.x.s %0, v12\\n\\t\"\n      \"vmv.x.s %1, v13\\n\\t\"\n      \"vmv.x.s %2, v14\\n\\t\"\n      \"vmv.x.s %3, v15\\n\\t\"\n      : \"=r\" (result0), \"=r\" (result1), \"=r\" (result2), \"=r\" (result3)\n );\n if(result0 != "+str(result0)+" || result1 != "+str(result1)+" || result2 != "+str(result2)+" || result3 != "+str(result3)+")\n{\n  printf(\"Test Failed! Results: %d %d %d %d\\n\", result0, result1, result2, result3);\n  return(1);\n}\nelse\n{\n  printf(\"Pass: %d %d %d %d\\n\", result0, result1, result2, result3);\n  return(0);\n}\n}"


add_vv_test_e32_m4 = "int add_vv_test_e32_m4(void)\n{\n  uint8_t result0, result1, result2, result3;\n  asm volatile (\n      \"li t1, 64 \\n\t\"\n      \"vsetvli t0, t1, e32, m1 \\n\\t\"\n      \"vmv.v.i v4, "+str(a)+" \\n\\t\"\n      \"vmv.v.i v5, "+str(b)+" \\n\\t\"\n      \"vmv.v.i v6, "+str(c)+" \\n\\t\"\n      \"vmv.v.i v7, "+str(d)+" \\n\\t\"\n      \"vmv.v.i v8, "+str(e)+" \\n\\t\"\n      \"vmv.v.i v9, "+str(f)+" \\n\\t\"\n      \"vmv.v.i v10, "+str(g)+" \\n\\t\"\n      \"vmv.v.i v11, "+str(h)+" \\n\\t\"\n      \"vsetvli t0, t1, e32, m4 \\n\\t\"\n      \"vadd.vv v12, v4, v8 \\n\\t\"\n      \"vsetvli t0, t1, e32, m1 \\n\\t\"\n      \"vmv.x.s %0, v12\\n\\t\"\n      \"vmv.x.s %1, v13\\n\\t\"\n      \"vmv.x.s %2, v14\\n\\t\"\n      \"vmv.x.s %3, v15\\n\\t\"\n      : \"=r\" (result0), \"=r\" (result1), \"=r\" (result2), \"=r\" (result3)\n  );\n  if(result0 != "+str(result0)+" || result1 != "+str(result1)+" || result2 != "+str(result2)+" || result3 != "+str(result3)+")\n  {\n      printf(\"Test Failed! Results: %d %d %d %d\\n\", result0, result1, result2, result3);\n      return(1);\n  }\n  else\n  {\n      printf(\"Pass: %d %d %d %d\\n\", result0, result1, result2, result3);\n      return(0);\n  }\n}"

addend = random.randint(0, 127)
result = addend + a

add_vx_test_e8_m1 = "\nint add_vx_test_e8_m1(void)\n{  \n  uint8_t addend = "+str(addend)+";\n  uint8_t result;\n  asm volatile (\n    \"li t1, 64 \\n\\t\"\n    \"vsetvli t0, t1, e8, m1 \\n\\t\"\n  \"vmv.v.i v1, "+str(a)+" \\n\\t\"\n\"vadd.vx v3, v1, %1 \\n\\t\"\n \"vmv.x.s %0, v3\"\n: \"=r\" (result) \n: \"r\"  (addend)\n);\nif(result != "+str(result)+")\n{\n  printf(\"Fail: %d\\n\", result);\nreturn(1);\n}\nelse\n{\n  printf(\"Pass: %d\\n\", result);\n return(0);\n}\n}"

add_vx_test_e16_m1 = "\nint add_vx_test_e16_m1(void)\n{  \n  uint8_t addend = "+str(addend)+";\nuint8_t result;\nasm volatile (\n   \"li t1, 64 \\n\\t\"\n  \"vsetvli t0, t1, e16, m1 \\n\\t\"\n\"vmv.v.i v1, "+str(a)+" \\n\\t\"\n\"vadd.vx v3, v1, %1 \\n\\t\"\n\"vmv.x.s %0, v3\"\n: \"=r\" (result) \n: \"r\"  (addend)\n);\nif(result != "+str(result)+")\n{\n   printf(\"Fail: %d\\n\", result);\n return(1);\n}\nelse\n{\n  printf(\"Pass: %d\\n\", result);\nreturn(0);\n}\n}"

add_vx_test_e32_m1 = "\nint add_vx_test_e32_m1(void)\n{  \n  uint8_t addend = "+str(addend)+";\nuint8_t result;\nasm volatile (\n   \"li t1, 64 \\n\\t\"\n \"vsetvli t0, t1, e32, m1 \\n\\t\"\n\"vmv.v.i v1, "+str(a)+" \\n\\t\"\n\"vadd.vx v3, v1, %1 \\n\\t\"\n\"vmv.x.s %0, v3\"\n: \"=r\" (result) \n: \"r\"  (addend)\n);\nif(result != "+str(result)+")\n{\n  printf(\"Fail: %d\\n\", result);\nreturn(1);\n}\nelse\n{\n  printf(\"Pass: %d\\n\", result);\nreturn(0);\n}\n}"

result0 = addend + a
result1 = addend + b

add_vx_test_e8_m2 = "\nint add_vx_test_e8_m2(void)\n{  \n  uint8_t addend = "+str(addend)+";\nuint8_t result0, result1;\nasm volatile (\n  \"li t1, 64 \\n\\t\"\n\"vsetvli t0, t1, e8, m1 \\n\\t\"\n\"vmv.v.i v2, "+str(a)+" \\n\\t\"\n\"vmv.v.i v3, "+str(b)+" \\n\\t\"\n\"vsetvli t0, t1, e8, m2\\n\\t\"\n\"vadd.vx v6, v2, %2 \\n\\t\"\n\"vsetvli t0, t1, e8, m1 \\n\\t\"\n\"vmv.x.s %0, v6\\n\\t\"\n\"vmv.x.s %1, v7\\n\\t\"\n: \"=r\" (result0), \"=r\" (result1) \n: \"r\"  (addend)\n);\nif(result0 != "+str(result0)+" || result1 != "+str(result1)+")\n{\n  printf(\"Fail: %d %d\\n\", result0, result1);\nreturn(1);\n}\nelse\n{\n  printf(\"Pass: %d %d\\n\", result0, result1);\nreturn(0);\n}\n}"

add_vx_test_e16_m2 = "\nint add_vx_test_e16_m2(void)\n{ \n  uint8_t addend = "+str(addend)+";\n  uint8_t result0, result1;\n asm volatile (\n   \"li t1, 64 \\n\\t\"\n \"vsetvli t0, t1, e16, m1 \\n\\t\"\n\"vmv.v.i v2, "+str(a)+" \\n\\t\"\n\"vmv.v.i v3, "+str(b)+" \\n\\t\"\n\"vsetvli t0, t1, e16, m2\\n\\t\"\n\"vadd.vx v6, v2, %2 \\n\\t\"\n \"vsetvli t0, t1, e16, m1 \\n\\t\"\n\"vmv.x.s %0, v6\\n\\t\"\n\"vmv.x.s %1, v7\\n\\t\"\n: \"=r\" (result0), \"=r\" (result1) \n: \"r\"  (addend)\n);\nif(result0 != "+str(result0)+" || result1 != "+str(result1)+")\n{\n  printf(\"Fail: %d %d\\n\", result0, result1);\n return(1);\n}\nelse\n{\n  printf(\"Pass: %d %d\\n\", result0, result1);\nreturn(0);\n}\n}"

add_vx_test_e32_m2 = "\nint add_vx_test_e32_m2(void)\n{  \n  uint8_t addend = "+str(addend)+";\nuint8_t result0, result1;\nasm volatile (\n  \"li t1, 64 \\n\\t\"\n \"vsetvli t0, t1, e32, m1 \\n\\t\"\n\"vmv.v.i v2, "+str(a)+" \\n\\t\"\n\"vmv.v.i v3, "+str(b)+" \\n\\t\"\n\"vsetvli t0, t1, e32, m2\\n\\t\"\n\"vadd.vx v6, v2, %2 \\n\\t\"\n\"vsetvli t0, t1, e32, m1 \\n\\t\"\n\"vmv.x.s %0, v6\\n\\t\"\n\"vmv.x.s %1, v7\\n\\t\"\n: \"=r\" (result0), \"=r\" (result1) \n: \"r\"  (addend)\n);\nif(result0 != "+str(result0)+" || result1 != "+str(result1)+")\n{\n  printf(\"Fail: %d %d\\n\", result0, result1);\nreturn(1);\n}\nelse\n{\n   printf(\"Pass: %d %d\\n\", result0, result1);\n return(0);\n}\n}"

result0 = addend + a
result1 = addend + b
result2 = addend + c
result3 = addend + d

add_vx_test_e8_m4 = "\nint add_vx_test_e8_m4(void)\n{  \n  uint8_t addend = "+str(addend)+";\nuint8_t result0, result1, result2, result3;\nasm volatile (\n   \"li t1, 64 \\n\\t\"\n \"vsetvli t0, t1, e8, m1 \\n\\t\"\n\"vmv.v.i v4, "+str(a)+" \\n\\t\"\n\"vmv.v.i v5, "+str(b)+" \\n\\t\"\n\"vmv.v.i v6, "+str(c)+" \\n\\t\"\n\"vmv.v.i v7, "+str(d)+" \\n\\t\"\n\"vsetvli t0, t1, e8, m4\\n\\t\"\n\"vadd.vx v8, v4, %4  \\n\\t\"\n\"vsetvli t0, t1, e8, m1 \\n\\t\"\n\"vmv.x.s %0, v8\\n\\t\"\n\"vmv.x.s %1, v9\\n\\t\"\n\"vmv.x.s %2, v10\\n\\t\"\n\"vmv.x.s %3, v11\\n\\t\"\n: \"=r\" (result0),\"=r\" (result1), \"=r\" (result2), \"=r\" (result3)\n: \"r\"  (addend)\n);\nif(result0 != "+str(result0)+" || result1 != "+str(result1)+" || result2 != "+str(result2)+" || result3 != "+str(result3)+")\n{\n   printf(\"Fail: %d %d %d %d\\n\", result0, result1, result2, result3);\n return(1);\n }\nelse\n{\n  printf(\"Pass: %d %d %d %d\\n\", result0, result1, result2, result3);\nreturn(0);\n}\n}"


add_vx_test_e16_m4 = "\nint add_vx_test_e16_m4(void)\n{  \n  uint8_t addend = "+str(addend)+";\n uint8_t result0, result1, result2, result3;\nasm volatile (\n   \"li t1, 64 \\n\\t\"\n  \"vsetvli t0, t1, e16, m1 \\n\\t\"\n \"vmv.v.i v4, "+str(a)+" \\n\\t\"\n\"vmv.v.i v5, "+str(b)+" \\n\\t\"\n\"vmv.v.i v6, "+str(c)+" \\n\\t\"\n\"vmv.v.i v7, "+str(d)+" \\n\\t\"\n\"vsetvli t0, t1, e16, m4\\n\\t\"\n\"vadd.vx v8, v4, %4  \\n\\t\"\n\"vsetvli t0, t1, e16, m1 \\n\\t\"\n\"vmv.x.s %0, v8\\n\\t\"\n\"vmv.x.s %1, v9\\n\\t\"\n\"vmv.x.s %2, v10\\n\\t\"\n\"vmv.x.s %3, v11\\n\\t\"\n: \"=r\" (result0), \"=r\" (result1), \"=r\" (result2), \"=r\" (result3)\n: \"r\"  (addend)\n);\nif(result0 != "+str(result0)+" || result1 != "+str(result1)+" || result2 != "+str(result2)+" || result3 != "+str(result3)+")\n{\n   printf(\"Fail: %d %d %d %d\\n\", result0, result1, result2, result3);\n return(1);\n}\nelse\n{\n  printf(\"Pass: %d %d %d %d\\n\", result0, result1, result2, result3);\n return(0);\n}\n}"



add_vx_test_e32_m4 = "\nint add_vx_test_e32_m4(void)\n{  \n  uint8_t addend = "+str(addend)+";\n uint8_t result0, result1, result2, result3;\nasm volatile (\n  \"li t1, 64 \\n\\t\"\n \"vsetvli t0, t1, e32, m1 \\n\\t\"\n\"vmv.v.i v4, "+str(a)+" \\n\\t\"\n\"vmv.v.i v5, "+str(b)+" \\n\\t\"\n\"vmv.v.i v6, "+str(c)+" \\n\\t\"\n\"vmv.v.i v7, "+str(d)+" \\n\\t\"\n\"vsetvli t0, t1, e32, m4\\n\\t\"\n\"vadd.vx v8, v4, %4  \\n\\t\"\n\"vsetvli t0, t1, e32, m1 \\n\\t\"\n\"vmv.x.s %0, v8\\n\\t\"\n\"vmv.x.s %1, v9\\n\\t\"\n\"vmv.x.s %2, v10\\n\\t\"\n\"vmv.x.s %3, v11\\n\\t\"\n: \"=r\" (result0), \"=r\" (result1), \"=r\" (result2), \"=r\" (result3)\n: \"r\"  (addend)\n);\nif(result0 != "+str(result0)+" || result1 != "+str(result1)+" || result2 != "+str(result2)+" || result3 != "+str(result3)+")\n{\n  printf(\"Fail: %d %d %d %d\\n\", result0, result1, result2, result3);\n return(1);\n}\nelse\n{\n  printf(\"Pass: %d %d %d %d\\n\", result0, result1, result2, result3);\nreturn(0);\n}\n}"




main="int main(void)\n{\nprintf(\"Testing Vector Addition\\n\");\nint errors = 0;\n    printf(\"vadd.vv\\n\");\nerrors += add_vv_test_e8_m1();\nerrors += add_vv_test_e8_m2();\nerrors += add_vv_test_e8_m4();\nerrors += add_vv_test_e16_m1();\nerrors += add_vv_test_e16_m2();\nerrors += add_vv_test_e16_m4();\nerrors += add_vv_test_e32_m1();\nerrors += add_vv_test_e32_m2();\nerrors += add_vv_test_e32_m4();\nprintf(\"\\n\");\nprintf(\"\\n\");\nprintf(\"vadd.vx\\n\");\nerrors += add_vx_test_e8_m1();\nerrors += add_vx_test_e8_m2();\nerrors += add_vx_test_e8_m4();\nerrors += add_vx_test_e16_m1();\nerrors += add_vx_test_e16_m2();\nerrors += add_vx_test_e16_m4();\nerrors += add_vx_test_e32_m1();\nerrors += add_vx_test_e32_m2();\nerrors += add_vx_test_e32_m4();\nprintf(\"\\n\");\nif(errors > 0)\n{\nprintf(\"\\nErrors Detected!\\nError Count: %d\\n\", errors);\nreturn(EXIT_FAILURE);\n}\nprintf(\"\\nAll Tests Completed\\nNo Errors Detected!\\n\");\nreturn(EXIT_SUCCESS);\n}"


text=header + add_vv_test_e8_m1 + add_vv_test_e16_m1 + add_vv_test_e32_m1 + add_vv_test_e8_m2 + add_vv_test_e16_m2 + add_vv_test_e32_m2 + add_vv_test_e8_m4 + add_vv_test_e16_m4 + add_vv_test_e32_m4 + add_vx_test_e8_m1 + add_vx_test_e16_m1 + add_vx_test_e32_m1 + add_vx_test_e8_m2 + add_vx_test_e16_m2 + add_vx_test_e32_m2 + add_vx_test_e8_m4 + add_vx_test_e16_m4 + add_vx_test_e32_m4 + main

cFile.write(text)
cFile.close()
