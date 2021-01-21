#ifndef DAY_COUNT_H
#define DAY_COUNT_H
#include "XLDate.h"

namespace Dates {

class DayCount {
public:
  // The operator should just call the member function yearFraction(.)
  virtual double operator()(
      const Dates::XLDate& date1, const Dates::XLDate& date2) const = 0;
  virtual double yearFraction(
      const Dates::XLDate& date1, const Dates::XLDate& date2) const = 0;
  virtual ~DayCount() {};
};

class Thirty360 final : public DayCount {
public:
  virtual double operator()(
      const Dates::XLDate& date1, const Dates::XLDate& date2) const override;
  virtual double yearFraction(
      const Dates::XLDate& date1, const Dates::XLDate& date2) const override;

private:
  // Maybe we should make this public and virtual on all derived classes (?)
  unsigned dateDiff_(
      const Dates::XLDate& date1, const Dates::XLDate& date2) const;
};

class Thirty360Eur final : public DayCount {
public:
  virtual double operator()(
      const Dates::XLDate& date1, const Dates::XLDate& date2) const;
  virtual double yearFraction(
      const Dates::XLDate& date1, const Dates::XLDate& date2) const;

private:
  // Maybe we should make this public and virtual on all derived classes (?)
  unsigned dateDiff_(
      const Dates::XLDate& date1, const Dates::XLDate& date2) const;
};

class Act365 final : public DayCount {
public:
  virtual double operator()(
      const Dates::XLDate& date1, const Dates::XLDate& date2) const;
  virtual double yearFraction(
      const Dates::XLDate& date1, const Dates::XLDate& date2) const;
};

class Act360 final : public DayCount {
public:
  virtual double operator()(
      const Dates::XLDate& date1, const Dates::XLDate& date2) const;
  virtual double yearFraction(
      const Dates::XLDate& date1, const Dates::XLDate& date2) const;
};

}

#endif

/*
  The MIT License (MIT)

  Copyright (c) 2020 Daniel Hanson
  Contributors: Reeta Khare, Gregory Brownson, Steven Zhang

  Permission is hereby granted, free of charge, to any person obtaining a copy
  of this software and associated documentation files (the "Software"), to deal
  in the Software without restriction, including without limitation the rights
  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
  copies of the Software, and to permit persons to whom the Software is
  furnished to do so, subject to the following conditions:

  The above copyright notice and this permission notice shall be included in all
  copies or substantial portions of the Software.

  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
  FITNESS  FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
  AUTHORS OR  COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
  LIABILITY, WHETHER  IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
  OUT OF OR IN  CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
  SOFTWARE.
*/
