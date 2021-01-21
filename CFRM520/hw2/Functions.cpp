#include "Functions.h"
#include <cmath>
#include <numeric>

double expMultiply(double x, double y) { return std::exp(x) * y; }

double expMultiply(double x, const std::vector<double>& v) {
  return std::exp(x) * accumulate(v.begin(), v.end(), 0);
}
