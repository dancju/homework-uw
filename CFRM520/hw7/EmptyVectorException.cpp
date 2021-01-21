#include "EmptyVectorException.h"

EmptyVectorException::EmptyVectorException() noexcept { }

const char* EmptyVectorException::what() const noexcept {
  return "ERROR: vector is empty";
}
