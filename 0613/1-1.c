#include <stdio.h>

int print_bit (unsigned char s) {
  int i;
  printf("0x%02x : ", s);
  for (i = 0; i < 8; i++) {
    printf("%c", ((0x80)&s)?'1':'0');
    s = s << 1;
  }
  printf("\n");
}

int main (int argc, char* argv[]) {
  int i;
  unsigned char u1, u2, u3;

  // 学籍番号:03213003 下2桁-上2桁
  u1 = 03;
  printf("u1      = "); print_bit(u1);
  printf("u1      = %d\n", u1);
  // 2's complement
  u2 = (0xff ^ 03) + 0x01;
  printf("u2      = "); print_bit(u2);
  printf("u2      = %d\n", (char)u2);
  u3 = u1 + u2;
  printf("u1 - u2 = ");  print_bit(u3);
  printf("u1 - u2 = %d\n", (char)u3);
  
}
