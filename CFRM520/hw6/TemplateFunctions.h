#ifndef TEMPLATE_FUNCTIONS_H
#define TEMPLATE_FUNCTIONS_H
#include <vector>

template <typename T> T polynomial(const std::vector<T>& coeffs, const T& x) {
  T t0(1), t1(0);
  for (const T& i : coeffs) {
    t0 *= x;
    t1 += i * t0;
  }
  return t1;
}

#endif
