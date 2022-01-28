#include "EmptyVectorException.h"
#include "Quadratic.h"
#include "VectorAlgos.h"
#include <iomanip>
#include <iostream>
#include <numeric>
#include <vector>
using std::cout;
using std::endl;
using std::iota;
using std::move;
using std::vector;

void testQuadraticAlgos() {
  Quadratic quad1(-2, -4, 2), quad2(-1, -2, 1);
  vector<double> data1(15), data2(15);
  iota(data1.begin(), data1.end(), -10);
  iota(data2.begin(), data2.end(), 0.75);
  VectorAlgos valgo(move(data1), move(quad1));
  auto res1 = valgo.results();
  valgo.resetCalc(move(data2), move(quad2));
  auto res2 = valgo.results();
  cout << "          mean      norm       max       min       std" << endl
       << "------------------------------------------------------" << endl;
  auto display_results = [](const char* id, std::map<CalcType, double> res) {
    cout << id;
    for (auto const& [k, v] : res)
      cout << std::setw(10) << v;
    cout << endl;
  };
  display_results("res1", res1);
  display_results("res2", res2);
  try {
    vector<double> data3;
    VectorAlgos valgo1(move(data3), move(quad1));
  } catch (const EmptyVectorException& e) { std::cerr << e.what() << endl; }
}

int main() {
  testQuadraticAlgos();
  return 0;
}
