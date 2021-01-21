#include "Egarch.h"
#include "MonteCarloBarrierOption.h"
#include <boost/circular_buffer.hpp>
#include <iostream>
#include <random>
using Dates::Act365;
using Dates::XLDate;
using std::cout;
using std::endl;
using std::for_each;
using std::map;

void mcBarrCall() {
  double strike = 102, spot = 100, riskFreeRate = .025, volatility = .06;
  OptionType optionType = OptionType::CALL;
  XLDate valueDate(2015, 10, 1);
  XLDate expiryDate(2017, 9, 30);
  XLDate settlementDate(expiryDate() + 1);
  Barrier barrierType = Barrier::UP_AND_OUT;
  double barrierVal = 103;
  unsigned numTimeSteps = 720, numScenarios = 10000;
  int seed = -106;
  double greekShift = .01;
  map<OptionValues, double> result = MonteCarloBarrierOption(strike, spot,
      riskFreeRate, volatility, optionType, valueDate, expiryDate,
      settlementDate, Act365(), barrierType, barrierVal, numTimeSteps,
      numScenarios, seed, greekShift)();
  cout << "Price = " << result.at(OptionValues::PRICE) << endl
       << "Delta = " << result.at(OptionValues::DELTA) << endl
       << "Vega  = " << result.at(OptionValues::VEGA) << endl
       << "Rho   = " << result.at(OptionValues::RHO) << endl
       << endl;
}

void mcBarrPut() {
  double strike = 102, spot = 100, riskFreeRate = .025, volatility = .06;
  OptionType optionType = OptionType::PUT;
  XLDate valueDate(2015, 10, 1);
  XLDate expiryDate(2017, 9, 30);
  XLDate settlementDate(expiryDate() + 1);
  Barrier barrierType = Barrier::DOWN_AND_OUT;
  double barrierVal = 93;
  unsigned numTimeSteps = 720, numScenarios = 10000;
  int seed = -106;
  double greekShift = .01;
  map<OptionValues, double> result = MonteCarloBarrierOption(strike, spot,
      riskFreeRate, volatility, optionType, valueDate, expiryDate,
      settlementDate, Act365(), barrierType, barrierVal, numTimeSteps,
      numScenarios, seed, greekShift)();
  cout << "Price = " << result.at(OptionValues::PRICE) << endl
       << "Delta = " << result.at(OptionValues::DELTA) << endl
       << "Vega  = " << result.at(OptionValues::VEGA) << endl
       << "Rho   = " << result.at(OptionValues::RHO) << endl
       << endl;
}

void simVolatilties(double alphaZero, double alphaOne, double gamma,
    double beta, double initSigma, int seed, int bufferSize) {
  Egarch egarch(alphaZero, alphaOne, gamma, beta);
  boost::circular_buffer<double> buffer(bufferSize);
  std::mt19937_64 generator(seed);
  std::normal_distribution distribution;
  buffer.push_back(initSigma);
  for (int i = 1; i < bufferSize; i++)
    buffer.push_back(egarch(buffer.back(), distribution(generator)));
  auto printDouble = [](double x) { cout << x << ' '; };
  for_each(buffer.begin(), buffer.begin() + 3, printDouble);
  cout << "... ";
  for_each(buffer.end() - 3, buffer.end(), printDouble);
  cout << endl;
}

int main() {
  mcBarrCall();
  mcBarrPut();
  simVolatilties(-0.0883, 0.1123, -0.0925, 0.9855, 0.25, 520, 100);
  return 0;
}
