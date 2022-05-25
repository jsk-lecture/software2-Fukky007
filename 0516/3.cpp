#include <iostream>
template <class t> class Square {
public:
  t data;
  Square (t _data) { data = _data * _data; }
  ~Square () {};
};

int main () {
  Square<int> a(10);
  Square<double> b(10.0);
  std::cerr << "a(10)   = " << a.data << std::endl;
  std::cerr << "b(10.0) = " << b.data << std::endl;
}
