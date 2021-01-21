#ifndef EMPTY_VECTOR_EXCEPTION_H
#define EMPTY_VECTOR_EXCEPTION_H
#include <exception>

class EmptyVectorException : public std::exception {
public:
  EmptyVectorException() noexcept;
  virtual const char* what() const noexcept;
};

#endif
