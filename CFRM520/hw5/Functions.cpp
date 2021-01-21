#include "Functions.h"
#include <cmath>
#include <limits>

PolyFunction::PolyFunction(double a, double b, double c, double d)
    : a_(a), b_(b), c_(c), d_(d) { }

double PolyFunction::operator()(double x) {
  return a_ * std::pow(x, 5) + b_ * std::pow(x, 3) + c_ * x + d_;
}

LogFunction::LogFunction(double a, double b) : a_(a), b_(b) { }

double LogFunction::operator()(double x) {
  static const double zero_ = std::sqrt(std::numeric_limits<double>::epsilon());
  if (x - b_ <= zero_)
    return std::numeric_limits<double>::quiet_NaN();
  return a_ * std::log(x - b_);
}

MixFunction::MixFunction(double a, double b, double c) : a_(a), b_(b), c_(c) { }

double MixFunction::operator()(double x) {
  static const double zero_ = std::sqrt(std::numeric_limits<double>::epsilon());
  if (std::abs(x) <= zero_)
    return std::numeric_limits<double>::quiet_NaN();
  return x + std::sin(a_ * x + b_) / x + c_;
}

double secant(RealFunction& f, double x0, double x1, double tol, int maxIter) {
  for (int i = 0; i < maxIter; i++) {
    double fx0 = f(x0), fx1 = f(x1);
    double x2 = (x0 * fx1 - x1 * fx0) / (fx1 - fx0);
    x0 = x1;
    x1 = x2;
    if (std::abs(x0 - x1) < tol)
      return x2;
  }
  return std::numeric_limits<double>::quiet_NaN();
}
