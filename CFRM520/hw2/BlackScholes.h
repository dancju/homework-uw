#ifndef BLACK_SCHOLES_H
#define BLACK_SCHOLES_H
#include <array>

enum PayoffType { CALL = 1, PUT = -1 };

using OptionData = std::array<double, 5>;

double norm_cdf(double);

std::array<double, 2> dee_fcns(double, double, double, double, double);

double black_scholes_price(double, double, double, double, double, PayoffType);

double black_scholes_price(const OptionData&, PayoffType);

#endif
