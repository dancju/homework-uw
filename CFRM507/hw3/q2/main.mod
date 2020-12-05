set citi;
set loca;
param a{loca, citi};
param b{loca};
var x{loca, citi} binary;
var y{loca} binary;

minimize obj:
  (sum {j in loca} b[j]*y[j])
  +(sum {i in citi} sum {j in loca} a[j,i]*x[j,i])
;

s.t. C0{i in citi, j in loca}: x[j,i] <= y[j];
s.t. C1{i in citi}: sum {j in loca} x[j,i] = 1;

data;
set citi := A B C D E F G H I J;
set loca := 1 2 3 4 5;
param a:
    A B C D E F G  H I J :=
  1 2 1 8 5 7 1 4  6 5 9
  2 4 9 4 3 9 4 4  2 7 2
  3 5 8 7 6 7 9 3 10 4 5
  4 3 5 7 9 7 6 6  5 4 5
  5 8 7 3 6 8 5 7  4 8 7
;
param b :=
  1 10
  2 12
  3  7
  4  8
  5  6
;

option solver cplex;
solve;
display x, y;
