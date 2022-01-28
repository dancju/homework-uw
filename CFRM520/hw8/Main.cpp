#include "ContaminatedNormal.h"
#include "CovarianceMtx.h"
#include "FileToMatrix.h"
#include <Eigen/Dense>
#include <chrono>
#include <iostream>
using Eigen::InnerStride;
using Eigen::Map;
using Eigen::MatrixXd;
using std::cout;
using std::endl;

void compute_cov_mtx() {
  MatrixXd m0 = FileToMatrix(4, 5, "CovarianceData.csv")();
  Map<MatrixXd, 0, InnerStride<1>> vol(m0.data(), 4, 1);
  Map<MatrixXd, 0, InnerStride<1>> cor(m0.data() + 4, 4, 4);
  CovarianceMtx cov_mtx(vol, cor);
  cout << cov_mtx() << endl << cov_mtx.cholesky() << endl;
}

void contaminated_normal() {
  unsigned seed = std::chrono::system_clock::now().time_since_epoch().count();
  ContaminatedNormal generator(0, 1, 2, 0.05, seed, 1024);
  for (int i = 0; i < generator.num_variates(); i++)
    cout << generator[i] << endl;
}

int main() {
  compute_cov_mtx();
  // contaminated_normal();
  return 0;
}
