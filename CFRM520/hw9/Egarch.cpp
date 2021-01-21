#include "Egarch.h"
#include <cmath>

Egarch::Egarch(double alphaZero, double alphaOne, double gamma, double beta)
    : alphaZero_(alphaZero), alphaOne_(alphaOne), gamma_(gamma), beta_(beta) { }

double Egarch::operator()(double prevSigma, double norm) const {
  return std::exp(
             (alphaZero_ + alphaOne_ * (std::abs(norm) + gamma_ * norm)) / 2)
      * std::pow(prevSigma, beta_);
}
