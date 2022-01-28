#include "SingleVariableFunction.h"
#include <cmath>

SecondDegreePolynomial::SecondDegreePolynomial(double a, double b, double c)
    : a_(a), b_(b), c_(c) { }

double SecondDegreePolynomial::operator()(double x) const {
  return a_ * x * (x + b_) + c_;
}

Sine::Sine(double amplitude, double periodDenominator, double horizontalShift,
    double verticalShift)
    : a_(amplitude), b_(periodDenominator), c_(horizontalShift),
      d_(verticalShift) { }

double Sine::operator()(double x) const {
  return a_ * std::sin(b_ * x + c_) + d_;
}

Logistic::Logistic(double maxVal, double steepness, double midpoint)
    : m_(maxVal), k_(steepness), x0_(midpoint) { }

double Logistic::operator()(double x) const {
  return m_ / (1 + std::exp(-k_ * (x - x0_)));
}
