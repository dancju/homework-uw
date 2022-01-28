#include "RootTests.h"
#include "Functions.h"
#include <iostream>

void PolyRootTests() {
  PolyFunction f(0.1, 0.25, -3, -1);
  std::cout << "The 1st root of the PolyFunction example is\t"
            << secant(f, -2, -1, 0.00001, 1000) << std::endl;
  std::cout << "The 2nd root of the PolyFunction example is\t"
            << secant(f, -1, 0, 0.00001, 1000) << std::endl;
  std::cout << "The 3rd root of the PolyFunction example is\t"
            << secant(f, 2, 3, 0.00001, 1000) << std::endl;
}

void LogRootTests() {
  LogFunction f(10, 0.5);
  std::cout << "The root of the LogFunction example is\t\t"
            << secant(f, 1, 2, 0.00001, 1000) << std::endl;
}

void MixRootTests() {
  MixFunction f(25, 5, -10);
  std::cout << "The 1st root of the MixFunction example is\t"
            << secant(f, 9.9, 9.95, 0.00001, 1000) << std::endl;
  std::cout << "The 2nd root of the MixFunction example is\t"
            << secant(f, 9.95, 10, 0.00001, 1000) << std::endl;
  std::cout << "The 3rd root of the MixFunction example is\t"
            << secant(f, 10, 10.1, 0.00001, 1000) << std::endl;
}
