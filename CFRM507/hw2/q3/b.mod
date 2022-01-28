var y{1..3} >=0;
var w;
minimize obj:  w;

s.t. c0:    y[1]    +y[2]    +y[3] == 1;
s.t. c1:  2*y[1] + 3*y[2]  -8*y[3] <= w;
s.t. c2: -5*y[1] -15*y[2]  +5*y[3] <= w;
s.t. c3:  5*y[1] +10*y[2]  -6*y[3] <= w;

solve;
display y, w;
end;
