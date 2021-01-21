#ifndef PRICING_ENUMS_H
#define PRICING_ENUMS_H

enum class OptionType { CALL, PUT };

enum class OptionValues { PRICE, DELTA, VEGA, RHO };

enum class BondAnalytics { PRICE, YTM, DURATION };

enum class Barrier { UP_AND_OUT, DOWN_AND_OUT };

#endif
