#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
int add_vv_test_e8_m1(void)
{
uint8_t result;
asm volatile (
"li t1, 64 \n\t"
"vsetvli t0, t1, e16, m1 \n\t"
"vmv.v.i v1, 6 \n\t"
"vmv.v.i v2, 6 \n\t"
"vadd.vv v3, v1, v2 \n\t"
"vmv.x.s %0, v3"
: "=r" (result) 
);
if(result != 12)
{
printf("Fail: %d\n", result);
return(1);
}
else
{
printf("Pass: %d\n", result);
return(0);
}
}
 int add_vv_test_e16_m1(void)
{
  uint8_t result;
  asm volatile (
      "li t1, 64 \n\t"
      "vsetvli t0, t1, e16, m1 \n\t"
      "vmv.v.i v1, 6 \n\t"
      "vmv.v.i v2, 6 \n\t"
      "vadd.vv v3, v1, v2 \n\t"
      "vmv.x.s %0, v3"
      : "=r" (result) 
  );
  if(result != 12)
{
    printf("Fail: %d\n", result);
    return(1);
}
else
{
    printf("Pass: %d\n", result);
    return(0);
}
}int add_vv_test_e32_m1(void)
{
  uint8_t result;
  asm volatile (
      "li t1, 64 \n\t"
      "vsetvli t0, t1, e32, m1 \n\t"
      "vmv.v.i v1, 6 \n\t"
      "vmv.v.i v2, 6 \n\t"
      "vadd.vv v3, v1, v2 \n	"
      "vmv.x.s %0, v3"
      : "=r" (result) 
  );
  if(result != 12)
  {
      printf("Fail: %d\n", result);
      return(1);
  }
  else
  {
      printf("Pass: %d\n", result);
      return(0);
  }
}int add_vv_test_e8_m2(void)
{
uint8_t result0 = 0, result1 = 0;
asm volatile (
"li t1, 64 \n\t"
"vsetvli t0, t1, e8, m1 \n\t"
"vmv.v.i v2, 6 \n\t"
"vmv.v.i v3, 6 \n\t"
"vmv.v.i v4, 15 \n\t"
"vmv.v.i v5, 1 \n\t"
"vsetvli t0, t1, e8, m2 \n\t"
"vadd.vv v6, v2, v4 \n\t"
"vsetvli t0, t1, e8, m1 \n\t"
"vmv.x.s %0, v6\n\t"
"vmv.x.s %1, v7\n\t"
: "=r" (result0), "=r" (result1)
);
if(result0 != 21 || result1 != 7)
{
printf("Test Failed! Results: %d\t%d\n", result0, result1);
return(1);
}
else
{
printf("Pass: %d\t%d\n", result0, result1);
return(0);
}
}int add_vv_test_e16_m2(void)
{
  uint8_t result0 = 0, result1 = 0;
  asm volatile (
      "li t1, 64 \n\t"
      "vsetvli t0, t1, e16, m1 \n\t"
      "vmv.v.i v2, 6 \n\t"
      "vmv.v.i v3, 6 \n\t"
      "vmv.v.i v4, 15 \n\t"
      "vmv.v.i v5, 1 \n\t"
      "vsetvli t0, t1, e16, m2 \n\t"
      "vadd.vv v6, v2, v4 \n\t"
      "vsetvli t0, t1, e16, m1 \n\t"
      "vmv.x.s %0, v6\n\t"
      "vmv.x.s %1, v7\n\t"
      : "=r" (result0), "=r" (result1)
  );
  if(result0 != 21 || result1 != 7)
  {
     printf("Test Failed! Results: %d\t%d\n", result0, result1);
   return(1);
}
else
{
   printf("Pass: %d\t%d\n", result0, result1);
 return(0);
}
}int add_vv_test_e32_m2(void)
{
  uint8_t result0 = 0, result1 = 0;
  asm volatile (
      "li t1, 64 \n\t"
      "vsetvli t0, t1, e32, m1 \n\t"
    "vmv.v.i v2, 6 \n\t"
    "vmv.v.i v3, 6 \n\t"
    "vmv.v.i v4, 15 \n\t"
    "vmv.v.i v5, 1 \n\t"
    "vsetvli t0, t1, e32, m2 \n\t"
    "vadd.vv v6, v2, v4 \n\t"
    "vsetvli t0, t1, e32, m1 \n\t"
    "vmv.x.s %0, v6\n\t"
    "vmv.x.s %1, v7\n\t"
    : "=r" (result0), "=r" (result1)
);
if(result0 != 21 || result1 != 7)
{
      printf("Test Failed! Results: %d\t%d\n", result0, result1);
      return(1);
  }
  else
  {
      printf("Pass: %d\t%d\n", result0, result1);
      return(0);
  }
}int add_vv_test_e8_m4(void)
{
uint8_t result0, result1, result2, result3;
asm volatile (
"li t1, 64 \n\t"
"vsetvli t0, t1, e8, m1 \n\t"
"vmv.v.i v4, 6 \n\t"
"vmv.v.i v5, 6 \n\t"
"vmv.v.i v6, 15 \n\t"
"vmv.v.i v7, 1 \n\t"
"vmv.v.i v8, 7 \n\t"
"vmv.v.i v9, 7 \n\t"
"vmv.v.i v10, 14 \n\t"
"vmv.v.i v11, 11 \n\t"
"vsetvli t0, t1, e8, m4 \n\t"
"vadd.vv v12, v4, v8 \n\t"
"vsetvli t0, t1, e8, m1 \n\t"
"vmv.x.s %0, v12\n\t"
"vmv.x.s %1, v13\n\t"
"vmv.x.s %2, v14\n\t"
"vmv.x.s %3, v15\n\t"
: "=r" (result0), "=r" (result1), "=r" (result2), "=r" (result3)
);
if(result0 != 13 || result1 != 13 || result2 != 29 || result3 != 12)
{
  printf("Test Failed! Results: %d %d %d %d\n", result0, result1, result2, result3);
return(1);
}
else
{
  printf("Pass: %d %d %d %d\n", result0, result1, result2, result3);
return(0);
}
}int add_vv_test_e16_m4(void)
{
  uint8_t result0, result1, result2, result3;
  asm volatile (
      "li t1, 64 \n\t"
      "vsetvli t0, t1, e16, m1 \n\t"
      "vmv.v.i v4, 6 \n\t"
      "vmv.v.i v5, 6 \n\t"
      "vmv.v.i v6, 15 \n\t"
      "vmv.v.i v7, 1 \n\t"
      "vmv.v.i v8, 7 \n\t"
      "vmv.v.i v9, 7 \n\t"
      "vmv.v.i v10, 14 \n\t"
      "vmv.v.i v11, 11 \n\t"
      "vsetvli t0, t1, e16, m4 \n\t"
      "vadd.vv v12, v4, v8 \n\t"
      "vsetvli t0, t1, e16, m1 \n\t"
      "vmv.x.s %0, v12\n\t"
      "vmv.x.s %1, v13\n\t"
      "vmv.x.s %2, v14\n\t"
      "vmv.x.s %3, v15\n\t"
      : "=r" (result0), "=r" (result1), "=r" (result2), "=r" (result3)
 );
 if(result0 != 13 || result1 != 13 || result2 != 29 || result3 != 12)
{
  printf("Test Failed! Results: %d %d %d %d\n", result0, result1, result2, result3);
  return(1);
}
else
{
  printf("Pass: %d %d %d %d\n", result0, result1, result2, result3);
  return(0);
}
}int add_vv_test_e32_m4(void)
{
  uint8_t result0, result1, result2, result3;
  asm volatile (
      "li t1, 64 \n	"
      "vsetvli t0, t1, e32, m1 \n\t"
      "vmv.v.i v4, 6 \n\t"
      "vmv.v.i v5, 6 \n\t"
      "vmv.v.i v6, 15 \n\t"
      "vmv.v.i v7, 1 \n\t"
      "vmv.v.i v8, 7 \n\t"
      "vmv.v.i v9, 7 \n\t"
      "vmv.v.i v10, 14 \n\t"
      "vmv.v.i v11, 11 \n\t"
      "vsetvli t0, t1, e32, m4 \n\t"
      "vadd.vv v12, v4, v8 \n\t"
      "vsetvli t0, t1, e32, m1 \n\t"
      "vmv.x.s %0, v12\n\t"
      "vmv.x.s %1, v13\n\t"
      "vmv.x.s %2, v14\n\t"
      "vmv.x.s %3, v15\n\t"
      : "=r" (result0), "=r" (result1), "=r" (result2), "=r" (result3)
  );
  if(result0 != 13 || result1 != 13 || result2 != 29 || result3 != 12)
  {
      printf("Test Failed! Results: %d %d %d %d\n", result0, result1, result2, result3);
      return(1);
  }
  else
  {
      printf("Pass: %d %d %d %d\n", result0, result1, result2, result3);
      return(0);
  }
}
int add_vx_test_e8_m1(void)
{  
  uint8_t addend = 8;
  uint8_t result;
  asm volatile (
    "li t1, 64 \n\t"
    "vsetvli t0, t1, e8, m1 \n\t"
  "vmv.v.i v1, 6 \n\t"
"vadd.vx v3, v1, %1 \n\t"
 "vmv.x.s %0, v3"
: "=r" (result) 
: "r"  (addend)
);
if(result != 14)
{
  printf("Fail: %d\n", result);
return(1);
}
else
{
  printf("Pass: %d\n", result);
 return(0);
}
}
int add_vx_test_e16_m1(void)
{  
  uint8_t addend = 8;
uint8_t result;
asm volatile (
   "li t1, 64 \n\t"
  "vsetvli t0, t1, e16, m1 \n\t"
"vmv.v.i v1, 6 \n\t"
"vadd.vx v3, v1, %1 \n\t"
"vmv.x.s %0, v3"
: "=r" (result) 
: "r"  (addend)
);
if(result != 14)
{
   printf("Fail: %d\n", result);
 return(1);
}
else
{
  printf("Pass: %d\n", result);
return(0);
}
}
int add_vx_test_e32_m1(void)
{  
  uint8_t addend = 8;
uint8_t result;
asm volatile (
   "li t1, 64 \n\t"
 "vsetvli t0, t1, e32, m1 \n\t"
"vmv.v.i v1, 6 \n\t"
"vadd.vx v3, v1, %1 \n\t"
"vmv.x.s %0, v3"
: "=r" (result) 
: "r"  (addend)
);
if(result != 14)
{
  printf("Fail: %d\n", result);
return(1);
}
else
{
  printf("Pass: %d\n", result);
return(0);
}
}
int add_vx_test_e8_m2(void)
{  
  uint8_t addend = 8;
uint8_t result0, result1;
asm volatile (
  "li t1, 64 \n\t"
"vsetvli t0, t1, e8, m1 \n\t"
"vmv.v.i v2, 6 \n\t"
"vmv.v.i v3, 6 \n\t"
"vsetvli t0, t1, e8, m2\n\t"
"vadd.vx v6, v2, %2 \n\t"
"vsetvli t0, t1, e8, m1 \n\t"
"vmv.x.s %0, v6\n\t"
"vmv.x.s %1, v7\n\t"
: "=r" (result0), "=r" (result1) 
: "r"  (addend)
);
if(result0 != 14 || result1 != 14)
{
  printf("Fail: %d %d\n", result0, result1);
return(1);
}
else
{
  printf("Pass: %d %d\n", result0, result1);
return(0);
}
}
int add_vx_test_e16_m2(void)
{ 
  uint8_t addend = 8;
  uint8_t result0, result1;
 asm volatile (
   "li t1, 64 \n\t"
 "vsetvli t0, t1, e16, m1 \n\t"
"vmv.v.i v2, 6 \n\t"
"vmv.v.i v3, 6 \n\t"
"vsetvli t0, t1, e16, m2\n\t"
"vadd.vx v6, v2, %2 \n\t"
 "vsetvli t0, t1, e16, m1 \n\t"
"vmv.x.s %0, v6\n\t"
"vmv.x.s %1, v7\n\t"
: "=r" (result0), "=r" (result1) 
: "r"  (addend)
);
if(result0 != 14 || result1 != 14)
{
  printf("Fail: %d %d\n", result0, result1);
 return(1);
}
else
{
  printf("Pass: %d %d\n", result0, result1);
return(0);
}
}
int add_vx_test_e32_m2(void)
{  
  uint8_t addend = 8;
uint8_t result0, result1;
asm volatile (
  "li t1, 64 \n\t"
 "vsetvli t0, t1, e32, m1 \n\t"
"vmv.v.i v2, 6 \n\t"
"vmv.v.i v3, 6 \n\t"
"vsetvli t0, t1, e32, m2\n\t"
"vadd.vx v6, v2, %2 \n\t"
"vsetvli t0, t1, e32, m1 \n\t"
"vmv.x.s %0, v6\n\t"
"vmv.x.s %1, v7\n\t"
: "=r" (result0), "=r" (result1) 
: "r"  (addend)
);
if(result0 != 14 || result1 != 14)
{
  printf("Fail: %d %d\n", result0, result1);
return(1);
}
else
{
   printf("Pass: %d %d\n", result0, result1);
 return(0);
}
}
int add_vx_test_e8_m4(void)
{  
  uint8_t addend = 8;
uint8_t result0, result1, result2, result3;
asm volatile (
   "li t1, 64 \n\t"
 "vsetvli t0, t1, e8, m1 \n\t"
"vmv.v.i v4, 6 \n\t"
"vmv.v.i v5, 6 \n\t"
"vmv.v.i v6, 15 \n\t"
"vmv.v.i v7, 1 \n\t"
"vsetvli t0, t1, e8, m4\n\t"
"vadd.vx v8, v4, %4  \n\t"
"vsetvli t0, t1, e8, m1 \n\t"
"vmv.x.s %0, v8\n\t"
"vmv.x.s %1, v9\n\t"
"vmv.x.s %2, v10\n\t"
"vmv.x.s %3, v11\n\t"
: "=r" (result0),"=r" (result1), "=r" (result2), "=r" (result3)
: "r"  (addend)
);
if(result0 != 14 || result1 != 14 || result2 != 23 || result3 != 9)
{
   printf("Fail: %d %d %d %d\n", result0, result1, result2, result3);
 return(1);
 }
else
{
  printf("Pass: %d %d %d %d\n", result0, result1, result2, result3);
return(0);
}
}
int add_vx_test_e16_m4(void)
{  
  uint8_t addend = 8;
 uint8_t result0, result1, result2, result3;
asm volatile (
   "li t1, 64 \n\t"
  "vsetvli t0, t1, e16, m1 \n\t"
 "vmv.v.i v4, 6 \n\t"
"vmv.v.i v5, 6 \n\t"
"vmv.v.i v6, 15 \n\t"
"vmv.v.i v7, 1 \n\t"
"vsetvli t0, t1, e16, m4\n\t"
"vadd.vx v8, v4, %4  \n\t"
"vsetvli t0, t1, e16, m1 \n\t"
"vmv.x.s %0, v8\n\t"
"vmv.x.s %1, v9\n\t"
"vmv.x.s %2, v10\n\t"
"vmv.x.s %3, v11\n\t"
: "=r" (result0), "=r" (result1), "=r" (result2), "=r" (result3)
: "r"  (addend)
);
if(result0 != 14 || result1 != 14 || result2 != 23 || result3 != 9)
{
   printf("Fail: %d %d %d %d\n", result0, result1, result2, result3);
 return(1);
}
else
{
  printf("Pass: %d %d %d %d\n", result0, result1, result2, result3);
 return(0);
}
}
int add_vx_test_e32_m4(void)
{  
  uint8_t addend = 8;
 uint8_t result0, result1, result2, result3;
asm volatile (
  "li t1, 64 \n\t"
 "vsetvli t0, t1, e32, m1 \n\t"
"vmv.v.i v4, 6 \n\t"
"vmv.v.i v5, 6 \n\t"
"vmv.v.i v6, 15 \n\t"
"vmv.v.i v7, 1 \n\t"
"vsetvli t0, t1, e32, m4\n\t"
"vadd.vx v8, v4, %4  \n\t"
"vsetvli t0, t1, e32, m1 \n\t"
"vmv.x.s %0, v8\n\t"
"vmv.x.s %1, v9\n\t"
"vmv.x.s %2, v10\n\t"
"vmv.x.s %3, v11\n\t"
: "=r" (result0), "=r" (result1), "=r" (result2), "=r" (result3)
: "r"  (addend)
);
if(result0 != 14 || result1 != 14 || result2 != 23 || result3 != 9)
{
  printf("Fail: %d %d %d %d\n", result0, result1, result2, result3);
 return(1);
}
else
{
  printf("Pass: %d %d %d %d\n", result0, result1, result2, result3);
return(0);
}
}int main(void)
{
printf("Testing Vector Addition\n");
int errors = 0;
    printf("vadd.vv\n");
errors += add_vv_test_e8_m1();
errors += add_vv_test_e8_m2();
errors += add_vv_test_e8_m4();
errors += add_vv_test_e16_m1();
errors += add_vv_test_e16_m2();
errors += add_vv_test_e16_m4();
errors += add_vv_test_e32_m1();
errors += add_vv_test_e32_m2();
errors += add_vv_test_e32_m4();
printf("\n");
printf("\n");
printf("vadd.vx\n");
errors += add_vx_test_e8_m1();
errors += add_vx_test_e8_m2();
errors += add_vx_test_e8_m4();
errors += add_vx_test_e16_m1();
errors += add_vx_test_e16_m2();
errors += add_vx_test_e16_m4();
errors += add_vx_test_e32_m1();
errors += add_vx_test_e32_m2();
errors += add_vx_test_e32_m4();
printf("\n");
if(errors > 0)
{
printf("\nErrors Detected!\nError Count: %d\n", errors);
return(EXIT_FAILURE);
}
printf("\nAll Tests Completed\nNo Errors Detected!\n");
return(EXIT_SUCCESS);
}