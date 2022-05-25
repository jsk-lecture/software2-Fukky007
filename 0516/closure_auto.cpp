#include <iostream>

auto f(auto a)
{
  auto b = 100;
  return [a, b](auto c) {return a + b + c; };
}

int main() {
  auto a = -10;
  auto b = -100;
  auto c = -1000;

  auto h = f(10);
  std::cerr << h(1000) << std::endl;
}
