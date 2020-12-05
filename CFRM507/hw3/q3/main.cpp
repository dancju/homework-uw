#include <array>
#include <iostream>

int main() {
  std::array<std::array<double, 3>, 20> f, g;
  f[19][0] = 25;
  f[19][1] = 5;
  f[19][2] = 1;
  g[19][0] = 1;
  g[19][1] = 1;
  g[19][2] = 0;
  for (int i = 18; i >= 0; i--) {
    double f_skip = 0.02 * f[i + 1][0] + 0.2 * f[i + 1][1] + 0.78 * f[i + 1][2];
    // Exceptional
    f[i][0] = 25;
    g[i][0] = 1;
    // Acceptable
    if (5 > f_skip) {
      f[i][1] = 5;
      g[i][1] = 1;
    } else {
      f[i][1] = f_skip;
      g[i][1] = 0;
    }
    // Unsuitable
    f[i][2] = f_skip;
    g[i][2] = 0;
  }
  for (int i = 0; i < 20; i++) {
    for (int j = 0; j < 3; j++)
      std::cout << f[i][j] << '\t';
    std::cout << std::endl;
  }
  std::cout << std::endl;
  for (int i = 0; i < 20; i++) {
    for (int j = 0; j < 3; j++)
      std::cout << g[i][j] << '\t';
    std::cout << std::endl;
  }
  return 0;
}
