#include <iostream>
#include <map>
#include <tuple>
using std::cout;
using std::endl;
using std::make_tuple;
using std::map;
using std::tuple;

map<tuple<int, int, double>, double> m_f0;

double f0(int i_month, int i_com, double d_return_past);
double f1(int i_month, int i_com, double d_return_past, double d_return_next);

double f0(int i_month, int i_com, double d_return_past) {
  try {
    return m_f0.at(make_tuple(i_month, i_com, d_return_past));
  } catch (const std::out_of_range& e) {
    double res;
    if (i_com > 16)
      res = 0;
    else if (i_month == 36)
      res = d_return_past - 0.04 * std::max(0, 14 - i_com);
    else
      res = 0.1 * f1(i_month, i_com, d_return_past, 0.2)
          + 0.15 * f1(i_month, i_com, d_return_past, 0.15)
          + 0.2 * f1(i_month, i_com, d_return_past, 0.10)
          + 0.55 * f1(i_month, i_com, d_return_past, 0.);
    m_f0[make_tuple(i_month, i_com, d_return_past)] = res;
    return res;
  }
}

double f1(int i_month, int i_com, double d_return_past, double d_return_next) {
  double f_c = f0(i_month + 1, i_com + 1,
      (d_return_past * i_com + d_return_next) / (i_com + 1));
  double f_d = f0(i_month + 1, i_com, d_return_past);
  double res1;
  bool res2;
  if (f_c > f_d) {
    res1 = f_c;
    res2 = true;
  } else {
    res1 = f_d;
    res2 = false;
  }
  cout << i_month << '\t' << i_com << '\t' << d_return_past << '\t'
       << d_return_next << '\t' << f_c << '\t' << f_d << '\t' << res1 << '\t'
       << res2 << endl;
  return res1;
}

int main() {
  cout.precision(6);
  cout << std::fixed;
  f1(32, 12, 0.14, 0.1);
  return 0;
}
