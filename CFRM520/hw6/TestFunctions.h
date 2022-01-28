#ifndef TEST_FUNCTIONS_H
#define TEST_FUNCTIONS_H
#include "SingleVariableFunction.h"
#include <iostream>
#include <vector>

template <typename T> void print(const T& t) { std::cout << t << " "; }

void poly_calc_real(const std::vector<double>&, const std::vector<double>&);

void poly_calc_int(const std::vector<int>&, const std::vector<int>&);

double shared_fcn_objects(double);

void stl_algos(Sine, const std::vector<double>&);

#endif
