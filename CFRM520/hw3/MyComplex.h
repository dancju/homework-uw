#ifndef MY_COMPLEX_H
#define MY_COMPLEX_H

class MyComplex {
  double real_, imag_, radius_, theta_;

public:
  MyComplex();
  MyComplex(double);
  MyComplex(double, double);
  void print() const;
  double real() const;
  double imag() const;
  double radius() const;
  double theta() const;
  void reset(double, double);
  MyComplex add(const MyComplex&) const;

private:
  void calcPolar_();
};

#endif
