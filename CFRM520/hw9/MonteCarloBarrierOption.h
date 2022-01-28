#ifndef MONTE_CARLO_BARRIER_OPTION_H
#define MONTE_CARLO_BARRIER_OPTION_H
#include "DayCount.h"
#include "PricingEnums.h"
#include <map>

class MonteCarloBarrierOption {
  // Basic parameters
  double strike_, spot_, riskFreeRate_, volatility_;
  OptionType optionType_;
  // Dates parameters
  double expiry_;
  double settlement_;
  // Barrier parameters
  Barrier barrierType_;
  double barrierVal_;
  // Simulation parameters
  unsigned numTimeSteps_;
  unsigned numScenarios_;
  int seed_;
  double greekShift_;
  // Results
  std::map<OptionValues, double> results_;

public:
  MonteCarloBarrierOption(
      // Basic parameters
      double strike, double spot, double riskFreeRate, double volatility,
      OptionType optionType,
      // Date parameters
      const Dates::XLDate& valueDate, const Dates::XLDate& expiryDate,
      const Dates::XLDate& settlementDate, const Dates::DayCount& dc,
      // Barrier parameters
      Barrier barrierType, double barrierVal,
      // Simulation parameters
      unsigned numTimeSteps, unsigned numScenarios, int seed,
      double greekShift);

  std::map<OptionValues, double> operator()() const;

private:
  double computePrice_();
  double computeDelta_(double);
  double computeVega_(double);
  double computeRho_(double);
};

#endif
