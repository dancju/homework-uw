#ifndef FUNCTIONS_H
#define FUNCTIONS_H

class RealFunction {
public:
  virtual ~RealFunction() = default;
  virtual double operator()(double) = 0;
};

class PolyFunction : public RealFunction {
  double a_, b_, c_, d_;

public:
  PolyFunction(double, double, double, double);
  double operator()(double) override;
};

class LogFunction : public RealFunction {
  double a_, b_;

public:
  LogFunction(double, double);
  double operator()(double) override;
};

class MixFunction : public RealFunction {
  double a_, b_, c_;

public:
  MixFunction(double, double, double);
  double operator()(double) override;
};

double secant(RealFunction&, double, double, double, int);

#endif
