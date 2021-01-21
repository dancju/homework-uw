#include "TestFunctions.h"
#include "SingleVariableFunction.h"
#include "TemplateFunctions.h"
#include <algorithm>
#include <iostream>
#include <memory>
#include <numeric>
using std::accumulate;
using std::cout;
using std::endl;
using std::make_shared;
using std::max_element;
using std::min_element;
using std::vector;

void poly_calc_real(
    const vector<double>& coeffs, const vector<double>& x_vals) {
  vector<double> y_vals;
  for (double x : x_vals)
    y_vals.push_back(polynomial(coeffs, x));
  cout << "maximum = " << *max_element(y_vals.begin(), y_vals.end()) << endl
       << "minimum = " << *min_element(y_vals.begin(), y_vals.end()) << endl
       << "sum     = " << accumulate(y_vals.begin(), y_vals.end(), 0) << endl
       << endl;
}

void poly_calc_int(const vector<int>& coeffs, const vector<int>& x_vals) {
  vector<int> y_vals;
  for (int x : x_vals)
    y_vals.push_back(polynomial(coeffs, x));
  cout << "maximum = " << *max_element(y_vals.begin(), y_vals.end()) << endl
       << "minimum = " << *min_element(y_vals.begin(), y_vals.end()) << endl
       << "sum     = " << accumulate(y_vals.begin(), y_vals.end(), 0) << endl
       << endl;
}

double shared_fcn_objects(double x) {
  vector<std::shared_ptr<SingleVariableFunction>> polyFunc;
  polyFunc.push_back(make_shared<Sine>(4.5, 2.0, 3.14, 5.0));
  polyFunc.push_back(make_shared<Logistic>(5.0, 0.25, 0.5));
  polyFunc.push_back(make_shared<SecondDegreePolynomial>(360.0, 160.0, 12.0));
  polyFunc.push_back(make_shared<SecondDegreePolynomial>(10.6, 8.74, 5.863));
  double total = 0;
  for (const auto& fcn : polyFunc)
    total += (*fcn)(x);
  return total;
}

void stl_algos(Sine fn, const vector<double>& params) {
  vector<double> res;
  std::transform(params.begin(), params.end(), std::back_inserter(res), fn);
  std::for_each(res.begin(), res.end(), print<double>);
}
