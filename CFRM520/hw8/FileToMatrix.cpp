#include "FileToMatrix.h"
#include <fstream>
using std::ifstream;
using std::string;

FileToMatrix::FileToMatrix(
    long nrow, long ncol, const std::string& filePathAndName)
    : nrow_(nrow), ncol_(ncol), filePathAndName_(filePathAndName) {
  csvToMatrix_();
}

Eigen::MatrixXd FileToMatrix::operator()() const { return eigDataMatrix_; }

void FileToMatrix::csvToMatrix_() {
  eigDataVector_.resize(nrow_ * ncol_);
  dataAsString_.clear();
  ifstream file(filePathAndName_);
  double d;
  string s;
  while (file.good()) {
    getline(file, s);
    std::stringstream lineStream(s);
    std::string cell;
    while (std::getline(lineStream, cell, ',')) {
      dataAsString_.push_back(cell);
    }
  }
  for (long k = 0; k < long(dataAsString_.size()); ++k) {
    // this is not elegant as using iterators, but we don't have this
    // feature in Eigen
    d = strtod(dataAsString_.at(k).c_str(), NULL);
    eigDataVector_(k) = d;
  }
  constructEigDataMatrix_();
}

void FileToMatrix::constructEigDataMatrix_() {
  eigDataMatrix_ = eigDataVector_;
  eigDataMatrix_.resize(ncol_, nrow_);
  // This is how I got Eigen to put the data in row-wise.
  // RowVector didn't seem to work.
  eigDataMatrix_.transposeInPlace();
  // Now transpose the matrix to get the desired result.
}
