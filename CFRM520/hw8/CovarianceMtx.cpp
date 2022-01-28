#include "CovarianceMtx.h"
#include <stdexcept>

CovarianceMtx::CovarianceMtx(Eigen::VectorXd&& vols, Eigen::MatrixXd&& corr_mtx)
    : vols_(vols), corr_mtx_(corr_mtx) {
  validate_vols_();
  validate_corr_mtx_();
  compute_vols_mtx_();
  compute_cov_mtx_();
}

Eigen::MatrixXd CovarianceMtx::operator()() const { return cov_mtx_; }

Eigen::MatrixXd CovarianceMtx::cholesky() const {
  return Eigen::LLT<Eigen::MatrixXd>(cov_mtx_).matrixL();
}

void CovarianceMtx::validate_vols_() const {
  if (std::count_if(vols_.data(), vols_.data() + vols_.size(),
          [](double i) { return i <= 0; }))
    throw std::domain_error(
        "CovarianceMtx: There is non-positive value(s) in the volatility "
        "vector.");
}

void CovarianceMtx::validate_corr_mtx_() const {
  if (corr_mtx_.cols() != corr_mtx_.rows())
    throw std::length_error(
        "CovarianceMtx: The correlation matrix is not square.");
  if (vols_.rows() != corr_mtx_.cols())
    throw std::length_error(
        "CovarianceMtx: The volatility vector is not of matching length with "
        "the correlation matrix.");
  if (corr_mtx_ != corr_mtx_.transpose())
    throw std::domain_error(
        "CovarianceMtx: The correlation matrix is not symmetric.");
}

void CovarianceMtx::compute_vols_mtx_() noexcept {
  vols_mtx_ = vols_.asDiagonal();
}

void CovarianceMtx::compute_cov_mtx_() noexcept {
  cov_mtx_ = vols_mtx_ * corr_mtx_ * vols_mtx_;
}
