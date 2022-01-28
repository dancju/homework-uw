var x{1..3} >=0;
var v;
maximize obj:  v;

s.t. c0:    x[1]    +x[2]    +x[3] == 1;
s.t. c1:  2*x[1]  -5*x[2]  +5*x[3] >= v;
s.t. c2:  3*x[1] -15*x[2] +10*x[3] >= v;
s.t. c3: -8*x[1]  +5*x[2]  -6*x[3] >= v;

solve;
display x, v;
end;
