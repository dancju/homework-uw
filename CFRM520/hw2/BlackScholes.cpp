#include "BlackScholes.h"
#include <cmath>

double norm_cdf(double x) {
  const double S = 1 / std::sqrt(2.);
  return 0.5 * std::erfc(-S * x);
}

std::array<double, 2> dee_fcns(
    double strike, double spot, double rate, double sigma, double year_frac) {
  double t0 = std::sqrt(year_frac);
  double t1 = (std::log(spot / strike) / t0 + rate * t0) / sigma;
  double t2 = sigma * t0 / 2;
  return { t1 + t2, t1 - t2 };
}

double black_scholes_price(double strike, double spot, double rate,
    double sigma, double year_frac, PayoffType type) {
  if (rate < 0.0 || sigma < 0.0)
    return NAN;
  if (year_frac == 0)
    return std::max(0.0, type * (spot - strike));
  auto dee = dee_fcns(strike, spot, rate, sigma, year_frac);
  return type
      * (norm_cdf(type * dee[0]) * spot
          - norm_cdf(type * dee[1]) * strike * std::exp(-rate * year_frac));
}

double black_scholes_price(const OptionData& data, PayoffType type) {
  auto [t0, t1, t2, t3, t4] = data;
  return black_scholes_price(t0, t1, t2, t3, t4, type);
}
