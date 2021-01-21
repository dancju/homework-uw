#include "VectorAlgos.h"
#include "EmptyVectorException.h"
#include <algorithm>
#include <cmath>
#include <numeric>
using std::accumulate;
using std::back_inserter;
using std::sqrt;
using std::transform;
using std::vector;

VectorAlgos::VectorAlgos(vector<double>&& data, Quadratic&& quad)
    : data_(data), quad_(quad) {
  if (data.empty())
    throw EmptyVectorException();
  runCalculations_();
}

std::map<CalcType, double> VectorAlgos::results() const { return results_; }

void VectorAlgos::resetCalc(vector<double>&& data, Quadratic&& quad) {
  if (data.empty())
    throw EmptyVectorException();
  data_ = data;
  quad_ = quad;
  image_.clear();
  results_.clear();
  runCalculations_();
}

void VectorAlgos::runCalculations_() {
  transform(data_.begin(), data_.end(), back_inserter(image_), quad_);
  calcMeanAndStdDev_();
  calcNorm_();
  calcMaxAndMin_();
}

void VectorAlgos::calcMeanAndStdDev_() {
  double mean = accumulate(image_.begin(), image_.end(), 0.) / image_.size();
  results_[CalcType::MEAN] = mean;
  auto sdElem = [mean](double i) { return (i - mean) * (i - mean); };
  vector<double> sdElems;
  transform(image_.begin(), image_.end(), back_inserter(sdElems), sdElem);
  results_[CalcType::STD_DEV]
      = sqrt(accumulate(sdElems.begin(), sdElems.end(), 0.) / sdElems.size());
}

void VectorAlgos::calcNorm_() {
  results_[CalcType::NORM] = sqrt(
      std::inner_product(image_.begin(), image_.end(), image_.begin(), 0.));
}

void VectorAlgos::calcMaxAndMin_() {
  results_[CalcType::MAX] = *std::max_element(image_.begin(), image_.end());
  results_[CalcType::MIN] = *std::min_element(image_.begin(), image_.end());
}
