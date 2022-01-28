#ifndef VECTOR_ALGOS_H
#define VECTOR_ALGOS_H
#include "Quadratic.h"
#include <map>
#include <vector>

enum class CalcType { MEAN, NORM, MAX, MIN, STD_DEV };

class VectorAlgos {
  std::vector<double> data_;
  std::vector<double> image_;
  Quadratic quad_;
  std::map<CalcType, double> results_;

public:
  VectorAlgos(std::vector<double>&& data, Quadratic&& quad);
  std::map<CalcType, double> results() const;
  void resetCalc(std::vector<double>&& data, Quadratic&& quad);

private:
  void runCalculations_();
  void calcMeanAndStdDev_();
  void calcNorm_();
  void calcMaxAndMin_();
};
#endif
