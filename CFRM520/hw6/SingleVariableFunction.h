#ifndef SINGLE_VARIABLE_FUNCTION_H
#define SINGLE_VARIABLE_FUNCTION_H

class SingleVariableFunction {
public:
  virtual ~SingleVariableFunction() = default;
  virtual double operator()(double x) const = 0;
};

class SecondDegreePolynomial final : public SingleVariableFunction {
  double a_, b_, c_;

public:
  SecondDegreePolynomial(double a = 1.0, double b = 1.0, double c = 0.0);
  virtual double operator()(double x) const override;
};

class Sine final : public SingleVariableFunction {
  double a_, b_, c_, d_;

public:
  Sine(double amplitude = 1.0, double periodDenominator = 1.0,
      double horizontalShift = 1.0, double verticalShift = 0.0);
  virtual double operator()(double x) const override;
};

class Logistic final : public SingleVariableFunction {
  double m_, k_, x0_;

public:
  Logistic(double maxVal = 1.0, double steepness = 1.0, double midpoint = 0.0);
  virtual double operator()(double x) const override;
};

#endif
