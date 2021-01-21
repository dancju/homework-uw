#include "MonteCarloBarrierOption.h"
#include "EquityPriceGenerator.h"
#include <cmath>
#include <future>
#include <numeric>
using std::exp;
using std::future;
using std::max;
using std::vector;

MonteCarloBarrierOption::MonteCarloBarrierOption(double strike, double spot,
    double riskFreeRate, double volatility, OptionType optionType,
    const Dates::XLDate& valueDate, const Dates::XLDate& expiryDate,
    const Dates::XLDate& settlementDate, const Dates::DayCount& dc,
    Barrier barrierType, double barrierVal, unsigned numTimeSteps,
    unsigned numScenarios, int seed, double greekShift)
    : strike_(strike), spot_(spot), riskFreeRate_(riskFreeRate),
      volatility_(volatility), optionType_(optionType),
      expiry_(dc.yearFraction(valueDate, expiryDate)),
      settlement_(dc.yearFraction(valueDate, settlementDate)),
      barrierType_(barrierType), barrierVal_(barrierVal),
      numTimeSteps_(numTimeSteps), numScenarios_(numScenarios), seed_(seed),
      greekShift_(greekShift) {
  double price = computePrice_();
  double delta = computeDelta_(price);
  double vega = computeVega_(price);
  double rho = computeRho_(price);
  results_ = { { OptionValues::PRICE, price }, { OptionValues::DELTA, delta },
    { OptionValues::VEGA, vega }, { OptionValues::RHO, rho } };
}

std::map<OptionValues, double> MonteCarloBarrierOption::operator()() const {
  return results_;
}

double MonteCarloBarrierOption::computePrice_() {
  EquityPriceGenerator epg(
      spot_, numTimeSteps_, expiry_, riskFreeRate_, volatility_);
  vector<future<vector<double>>> futures;
  for (unsigned i = 0; i < numScenarios_; ++i)
    futures.push_back(std::async(epg, seed_ + i));
  vector<double> payoffs(numScenarios_);
  std::transform(futures.begin(), futures.end(), payoffs.begin(),
      [this](future<vector<double>>& x) -> double {
        vector<double> path = x.get();
        if (barrierType_ == Barrier::UP_AND_OUT
            && *std::max_element(path.begin(), path.end()) > barrierVal_)
          return 0.0;
        if (barrierType_ == Barrier::DOWN_AND_OUT
            && *std::min_element(path.begin(), path.end()) < barrierVal_)
          return 0.0;
        if (optionType_ == OptionType::CALL)
          return exp(-settlement_ * riskFreeRate_)
              * max(path.back() - strike_, 0.0);
        if (optionType_ == OptionType::PUT)
          return exp(-settlement_ * riskFreeRate_)
              * max(strike_ - path.back(), 0.0);
        throw std::logic_error("");
      });
  return std::reduce(payoffs.begin(), payoffs.end(), 0.0) / numScenarios_;
}

double MonteCarloBarrierOption::computeDelta_(double price0) {
  double spot0 = spot_;
  spot_ += greekShift_ * spot_;
  double price1 = computePrice_();
  double delta = (price1 - price0) / (spot_ - spot0);
  spot_ = spot0;
  return delta;
}

double MonteCarloBarrierOption::computeVega_(double price0) {
  double volatility0 = volatility_;
  volatility_ += greekShift_ * volatility_;
  double price1 = computePrice_();
  double vega = (price1 - price0) / (volatility_ - volatility0);
  volatility_ = volatility0;
  return vega;
}

double MonteCarloBarrierOption::computeRho_(double price0) {
  double riskFreeRate0 = riskFreeRate_;
  riskFreeRate_ += greekShift_ * riskFreeRate_;
  double price1 = computePrice_();
  double rho = (price1 - price0) / (riskFreeRate_ - riskFreeRate0);
  riskFreeRate_ = riskFreeRate0;
  return rho;
}
