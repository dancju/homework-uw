var x{1..5} >=0;
var y{1..3} >=0;
var z{1..6} >=0;
maximize obj: z[6];

s.t. c1: x[1] +      y[1]                          - z[1] =  150;
s.t. c2: x[2] +      y[2] - 1.01*x[1] + 1.003*z[1] - z[2] =  100;
s.t. c3: x[3] +      y[3] - 1.01*x[2] + 1.003*z[2] - z[3] = -200;
s.t. c4: x[4] - 1.02*y[1] - 1.01*x[3] + 1.003*z[3] - z[4] =  200;
s.t. c5: x[5] - 1.02*y[2] - 1.01*x[4] + 1.003*z[4] - z[5] = -50;
s.t. c6:      - 1.02*y[3] - 1.01*x[5] + 1.003*z[5] - z[6] = -300;

solve;
display x, y, z;
end;