#ifndef EGARCH_H
#define EGARCH_H

class Egarch {
  double alphaZero_, alphaOne_, gamma_, beta_;

public:
  Egarch(double alphaZero, double alphaOne, double gamma, double beta);

  double operator()(double prevSigma, double norm) const;
};

#endif
