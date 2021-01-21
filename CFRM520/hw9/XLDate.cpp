#include "XLDate.h"
#include "date.h"
#include <stdexcept>
using Dates::XLDate;
using std::invalid_argument;
using std::out_of_range;

/*
  This implementation borrows information from the following source:
  http://www.codeproject.com/Articles/2750/Excel-serial-date-to-Day-Month-Year-and-vise-versa
*/

// Note:  _MSC_VER >= 1900 in date.h means Visual Studio 2015 or higher

namespace Dates {
// Default:  Earliest UNIX date
XLDate::XLDate() : date_(date::year(1970) / date::month(1) / date::day(1)) {
  if (!dateToSerial_())
    // This should never happen:
    throw out_of_range(
        "XLDate::XLDate: Calendar XLDate is out of range in default "
        "constructor.");
}

XLDate::XLDate(unsigned serialDate) : serialDate_(serialDate) {
  if (!serialToDate_())
    throw out_of_range(
        "XLDate::XLDate: Serial XLDate is out of range in serialDate "
        "constructor.");
}

XLDate::XLDate(unsigned year, unsigned month, unsigned day)
    : date_(date::year(year) / date::month(month) / date::day(day)) {
  if (!dateToSerial_())
    throw out_of_range(
        "XLDate::XLDate: Calendar XLDate is out of range in YMD constructor.");
}

XLDate& XLDate::addYears(int years) {
  date_ += date::years(years);
  if (!dateToSerial_())
    throw out_of_range(
        "XLDate::XLDate::addYears(.): resulting date out of range.");
  return *this;
}

XLDate& XLDate::addMonths(int months) {
  date_ += date::months(months);
  if (!dateToSerial_())
    throw out_of_range(
        "XLDate::XLDate::addMonths(.): resulting date out of range.");
  return *this;
}

XLDate& XLDate::addDays(int days) {
  serialDate_ += days;
  if (!serialToDate_())
    throw out_of_range(
        "XLDate::XLDate::addDays(.): resulting date out of range.");
  return *this;
}

bool XLDate::endOfMonth() const {
  if (serialDate_ == 60)
    return true;
  else
    return date_ == date_.year() / date_.month() / date::last;
}

unsigned XLDate::daysInMonth() const {
  static const unsigned monthLength[]
      = { 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 };
  static const unsigned monthLeapLength[]
      = { 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 };
  return leapYear() ? monthLeapLength[month() - 1] : monthLength[month() - 1];
}

unsigned XLDate::dayOfWeek() const {
  // From Sunday to Saturday (0 to 6)
  // In accordance with Excel. The date before 3/1/1900 is wrong
  return (serialDate_ - 1) % 7;
}

bool XLDate::leapYear() const {
  if (year() == 1900)
    return true;
  else
    return date_.year().is_leap();
}

bool XLDate::weekday() const {
  unsigned day = dayOfWeek();
  if (day == 0 || day == 6)
    return false;
  else
    return true;
}

unsigned XLDate::year() const {
  return static_cast<unsigned>(static_cast<int>(date_.year()));
}

unsigned XLDate::month() const { return static_cast<unsigned>(date_.month()); }

unsigned XLDate::day() const { return static_cast<unsigned>(date_.day()); }

unsigned XLDate::serialDate() const { return serialDate_; }

void XLDate::setYear(unsigned year) {
  date_ = date::year(year) / date_.month() / date_.day();
  if (!dateToSerial_())
    throw out_of_range(
        "Dates::XLDate::setYear(.): resulting date out of range.");
}

void XLDate::setMonth(unsigned month) {
  date_ = date_.year() / date::month(month) / date_.day();
  if (!dateToSerial_())
    throw out_of_range(
        "Dates::XLDate::setMonth(.): resulting date out of range.");
}

void XLDate::setDay(unsigned day) {
  date_ = date_.year() / date_.month() / date_.day();
  if (!dateToSerial_())
    throw out_of_range(
        "Dates::XLDate::setDay(.): resulting date out of range.");
}

void XLDate::setSerialDate(unsigned serialXLDate) {
  serialDate_ = serialXLDate;
  if (!serialToDate_())
    throw out_of_range(
        "Dates::XLDate::setSerialXLDate(.): resulting date out of range.");
}

unsigned XLDate::operator()() const { return serialDate(); }

unsigned XLDate::operator-(const XLDate& rhs) const {
  return serialDate_ - rhs.serialDate_;
}

XLDate& XLDate::operator+=(int days) { return addDays(days); }

XLDate& XLDate::operator-=(int days) { return addDays(-days); }

XLDate& XLDate::operator++() { return addDays(1); }

XLDate& XLDate::operator--() { return addDays(-1); }

XLDate XLDate::operator++(int notused) {
  XLDate d(*this);
  return ++d;
}

XLDate XLDate::operator--(int notused) {
  XLDate d(*this);
  return --d;
}

bool XLDate::operator==(const XLDate& rhs) const {
  return serialDate_ == rhs.serialDate_;
}

bool XLDate::operator!=(const XLDate& rhs) const {
  return serialDate_ != rhs.serialDate_;
}

bool XLDate::operator<(const XLDate& rhs) const {
  return serialDate_ < rhs.serialDate_;
}

bool XLDate::operator>(const XLDate& rhs) const {
  return serialDate_ > rhs.serialDate_;
}

bool XLDate::operator<=(const XLDate& rhs) const {
  return serialDate_ <= rhs.serialDate_;
}

bool XLDate::operator>=(const XLDate& rhs) const {
  return serialDate_ >= rhs.serialDate_;
}

bool XLDate::serialToDate_() {
  // Check if serial date is in range
  if ((serialDate_ - minSerial_) >= maxSerial_)
    return false;
  else if (serialDate_ == 60)
    date_ = 1900_y / feb / 29;
  else
    // If serialXLDate is greater than 60, then adjust serial date accordingly
    date_ = serialDate_ > 60
        ? date::year_month_day(minDate_ + date::days(serialDate_ - 2))
        : date::year_month_day(minDate_ + date::days(serialDate_ - 1));
  return true;
}

bool XLDate::dateToSerial_() {
  // Check if date is valid
  if (date_ == 1900_y / feb / 29)
    serialDate_ = 60;
  else if (!date_.ok() || (year() - 1900) > 299)
    return false;
  else
    // If date is past Feb 29, 1900, add one to serial date value
    serialDate_ = date_ >= 1900_y / mar / 1
        ? date::days(date::sys_days(date_) - minDate_).count() + 2
        : date::days(date::sys_days(date_) - minDate_).count() + 1;
  return true;
}

std::ostream& operator<<(std::ostream& os, const XLDate& rhs) {
  os << rhs.year() << "." << rhs.month() << "." << rhs.day()
     << "; Excel serial format = " << rhs.serialDate_;
  return os;
}

}

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
  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
  SOFTWARE.
*/
