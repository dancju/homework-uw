set date;
set factor;

param return_factor{date, factor};
param return_fund{date};

var alpha;
var beta{factor} >= 0;

minimize obj: sum {i in date} (
    - return_fund[i]
    + alpha
    + sum{j in factor} beta[j] * return_factor[i, j]
) ** 2;

s.t. c: sum {j in factor} beta[j] == 1;
