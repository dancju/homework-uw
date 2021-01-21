#include "BlackScholes.h"
#include <cmath>

double BlackScholes::norm_cdf(double x) {
  const double S = 1 / std::sqrt(2.);
  return 0.5 * std::erfc(-S * x);
}

std::array<double, 2> BlackScholes::dee_fcns(double spot) const {
  double t0 = std::sqrt(year_frac);
  double t1 = (std::log(spot / strike) / t0 + rate * t0) / sigma;
  double t2 = sigma * t0 / 2;
  return { t1 + t2, t1 - t2 };
}

BlackScholes::BlackScholes(double strike, double rate, double sigma,
    double year_frac, PayoffType type) {
  this->strike = strike;
  this->rate = rate;
  this->sigma = sigma;
  this->year_frac = year_frac;
  this->type = type;
}

double BlackScholes::operator()(double spot) const {
  if (rate < 0.0 || sigma < 0.0)
    return NAN;
  if (year_frac == 0)
    return std::max(0.0, type * (spot - strike));
  auto dee = dee_fcns(spot);
  return type
      * (norm_cdf(type * dee[0]) * spot
          - norm_cdf(type * dee[1]) * strike * std::exp(-rate * year_frac));
}
