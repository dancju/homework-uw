#ifndef BLACK_SCHOLES_H
#define BLACK_SCHOLES_H
#include <array>

class BlackScholes {
public:
  enum PayoffType { CALL = 1, PUT = -1 };

private:
  double strike, rate, sigma, year_frac;
  PayoffType type;

public:
  BlackScholes(double, double, double, double, PayoffType);
  double operator()(double) const;

private:
  static double norm_cdf(double);
  std::array<double, 2> dee_fcns(double) const;
};

#endif
