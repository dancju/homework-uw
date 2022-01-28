#include <cmath>

double trig_shift(double x, double y, double phi) {
  return std::sin(x + phi * y) + std::cos(x - phi * y);
}

double norm_cdf(double x) {
  const double sqrt_two = std::sqrt(2);
  return .5 + std::erf(x / sqrt_two) / 2;
}

int sum_abs(int j, int k) { return std::abs(j) + std::abs(k); }

int abs_sum(int j, int k) { return std::abs(j + k); }
