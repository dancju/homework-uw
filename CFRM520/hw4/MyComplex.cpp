#include "MyComplex.h"
#include <cmath>
#include <iostream>

void MyComplex::calcPolar_() {
  radius_ = std::sqrt(real_ * real_ + imag_ * imag_);
  theta_ = std::atan2(imag_, real_);
}

MyComplex::MyComplex() : MyComplex(0, 0) { }

MyComplex::MyComplex(double r) : MyComplex(r, 0) { }

MyComplex::MyComplex(double r, double i) : real_(r), imag_(i) { calcPolar_(); }

void MyComplex::print() const {
  std::cout << real_ << (imag_ < 0 ? " - " : " + ") << std::abs(imag_) << "i"
            << std::endl;
}

double MyComplex::real() const { return real_; }

double MyComplex::imag() const { return imag_; }

double MyComplex::radius() const { return radius_; }

double MyComplex::theta() const { return theta_; }

void MyComplex::reset(double r, double i) {
  real_ = r;
  imag_ = i;
  calcPolar_();
}

MyComplex MyComplex::add(const MyComplex& that) const {
  return MyComplex(real_ + that.real_, imag_ + that.imag_);
}

void MyComplex::operator()() const { print(); }

bool MyComplex::operator==(const MyComplex& that) const {
  return real_ == that.real_ && imag_ == that.imag_;
}

bool MyComplex::operator!=(const MyComplex& that) const {
  return !(*this == that);
}

MyComplex MyComplex::operator+(const MyComplex& that) const {
  return add(that);
}

MyComplex MyComplex::operator-(const MyComplex& that) const {
  return MyComplex(real_ - that.real_, imag_ - that.imag_);
}

MyComplex MyComplex::operator*(const MyComplex& that) const {
  return MyComplex(real_ * that.real_ - imag_ * that.imag_,
      real_ * that.imag_ + imag_ * that.real_);
}

MyComplex& MyComplex::operator+=(const MyComplex& that) {
  *this = *this + that;
  return *this;
}

MyComplex& MyComplex::operator-=(const MyComplex& that) {
  *this = *this - that;
  return *this;
}

MyComplex& MyComplex::operator*=(const MyComplex& that) {
  *this = *this * that;
  return *this;
}
