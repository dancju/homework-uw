set s_x;
set s_j;
var f{s_x};
var g{s_j, s_x};
var t{s_j};
var r{s_x};

minimize obj: sum{i in s_x} r[i];

s.t. c_f {x in s_x} : f[x] = exp(abs(x)) + 10 * cos(x+1);
s.t. c_g {j in s_j, x in s_x} : g[j, x] = x ** j;
s.t. c_0 {x in s_x} : abs(f[x] - sum {j in s_j} t[j]*g[j, x]) <= r[x];

data;
set s_x := -3 -2 -1 0 1 2 3 4;
set s_j := 0 1 2 3; # or 0 1 2 3 4

option solver baron;
solve;
display t;
