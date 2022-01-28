#include "ContaminatedNormal.h"
#include <algorithm>
#include <random>
#include <stdexcept>

ContaminatedNormal::ContaminatedNormal(double mean, double sd_0, double sd_1,
    double alpha, int seed, int num_variates)
    : mean_(mean), sd_0_(sd_0), sd_1_(sd_1), alpha_(alpha), seed_(seed),
      num_variates_(num_variates) {
  check_volatilities_();
  generate();
}

double ContaminatedNormal::operator[](int k) const {
  if (k < 0)
    throw std::domain_error("ContaminatedNormal: The index is negative.");
  if (k >= cont_norm_variates_.size())
    throw std::out_of_range("ContaminatedNormal: Out of range.");
  return cont_norm_variates_[k];
}

int ContaminatedNormal::num_variates() const { return num_variates_; }

void ContaminatedNormal::generate() {
  std::default_random_engine engine(seed_);
  std::uniform_real_distribution<double> du(0., 1.);
  std::normal_distribution dn_0(mean_, sd_0_);
  std::normal_distribution dn_1(mean_, sd_1_);
  cont_norm_variates_.resize(num_variates_);
  std::transform(cont_norm_variates_.begin(), cont_norm_variates_.end(),
      cont_norm_variates_.begin(),
      [this, &engine, &du, &dn_0, &dn_1](double _) {
        return du(engine) < alpha_ ? dn_1(engine) : dn_0(engine);
      });
}

void ContaminatedNormal::generate(double mean, double sd_0, double sd_1,
    double alpha, int seed, int num_variates) {
  mean_ = mean;
  sd_0_ = sd_0;
  sd_1_ = sd_1;
  alpha_ = alpha;
  seed_ = seed;
  num_variates_ = num_variates;
  check_volatilities_();
  generate();
}

void ContaminatedNormal::check_volatilities_() const {
  if (sd_0_ <= 0 || sd_1_ <= 0)
    throw std::domain_error(
        "ContaminatedNormal: There volatility should be positive.");
  if (sd_0_ >= sd_1_)
    throw std::domain_error(
        "ContaminatedNormal: sg_0 should be less than sg_1.");
}
