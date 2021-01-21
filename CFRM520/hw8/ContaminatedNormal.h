#ifndef CONTAMINATED_NORMAL_H
#define CONTAMINATED_NORMAL_H
#include <vector>

class ContaminatedNormal {
  double mean_, sd_0_, sd_1_, alpha_;
  int seed_, num_variates_;
  std::vector<double> cont_norm_variates_;

public:
  ContaminatedNormal(double mean, double sd_0, double sd_1, double alpha,
      int seed, int num_variates);
  double operator[](int k) const;
  int num_variates() const;
  void generate();
  void generate(double mean, double sd_0, double sd_1, double alpha, int seed,
      int num_variates);

private:
  void check_volatilities_() const;
};

#endif
