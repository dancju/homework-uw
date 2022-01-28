#ifndef COVARIANCE_MTX_H
#define COVARIANCE_MTX_H
#include <Eigen/Dense>

class CovarianceMtx {
  Eigen::VectorXd vols_;
  Eigen::MatrixXd corr_mtx_;
  Eigen::MatrixXd vols_mtx_;
  Eigen::MatrixXd cov_mtx_;

public:
  CovarianceMtx(Eigen::VectorXd&& vols, Eigen::MatrixXd&& corr_mtx);
  Eigen::MatrixXd operator()() const;
  Eigen::MatrixXd cholesky() const;

private:
  void validate_vols_() const;
  void validate_corr_mtx_() const;
  void compute_vols_mtx_() noexcept;
  void compute_cov_mtx_() noexcept;
};

#endif
