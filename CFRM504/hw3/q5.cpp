#include <cmath>
#include <iostream>
#include <vector>
using std::cerr;
using std::cout;
using std::endl;
using std::max;
using std::vector;

int main() {
  freopen("input.txt", "r", stdin);
  double price_stock_init, time, price_strike, rate_interest, volatility,
      n_step;
  scanf("%lf,%lf,%lf,%lf,%lf,%lf", &price_stock_init, &time, &price_strike,
      &rate_interest, &volatility, &n_step);
  double time_step = time / n_step;

  vector<vector<double>> price_stock(n_step + 1, vector<double>(n_step + 1));
  for (int i = 0; i <= n_step; i++)
    for (int j = 0; j <= i; j++)
      price_stock[i][j]
          = price_stock_init * exp(volatility * sqrt(time_step) * (2 * j - i));

  vector<vector<double>> price_options(n_step + 1, vector<double>(n_step + 1));
  double u = exp(volatility * sqrt(time_step));
  double d = exp(-volatility * sqrt(time_step));
  double p = (exp(rate_interest * time_step) - d) / (u - d);
  double q = 1 - p;
  p *= exp(-rate_interest * time_step);
  q *= exp(-rate_interest * time_step);
  for (int j = 0; j <= n_step; j++)
    price_options[n_step][j] = max(0., price_strike - price_stock[n_step][j]);
  for (int i = n_step - 1; i >= 0; i--)
    for (int j = 0; j <= i; j++)
      price_options[i][j] = max(max(0., price_strike - price_stock[i][j]),
          (p * price_options[i + 1][j + 1] + q * price_options[i + 1][j]));

  vector<vector<double>> n_stock(n_step + 1, vector<double>(n_step + 1));
  for (int i = 0; i < n_step; i++)
    for (int j = 0; j <= i; j++)
      n_stock[i][j] = (price_options[i + 1][j + 1] - price_options[i + 1][j])
          / (price_stock[i + 1][j + 1] - price_stock[i + 1][j]);

  freopen("debug.txt", "w", stderr);
  for (int i = 0; i <= n_step; i++) {
    for (int j = 0; j <= i; j++)
      cerr << price_stock[i][j] << '\t';
    cerr << endl;
  }
  cerr << endl;
  for (int i = 0; i <= n_step; i++) {
    for (int j = 0; j <= i; j++)
      cerr << price_options[i][j] << '\t';
    cerr << endl;
  }
  cerr << endl;
  freopen("output.txt", "w", stdout);
  cout << price_options[0][0] << ',' << n_stock[0][0] << endl;
  return 0;
}
