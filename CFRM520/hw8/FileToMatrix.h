#ifndef FILE_TO_MATRIX_H
#define FILE_TO_MATRIX_H
#include <Eigen/Dense>
#include <vector>

class FileToMatrix {
  Eigen::MatrixXd eigDataMatrix_;
  Eigen::VectorXd eigDataVector_;
  long nrow_, ncol_;
  std::vector<std::string> dataAsString_;
  std::string filePathAndName_;

public:
  FileToMatrix(long nrow, long ncol, const std::string& filePathAndName);
  Eigen::MatrixXd operator()() const;

private:
  void constructEigDataMatrix_();
  void csvToMatrix_();
};

#endif
