var x1;
var x2;
var r;
maximize obj: r;

s.t. c1:   x1  +8*x2  +65**.5*r <=  800;
s.t. c2: 3*x1 +10*x2 +109**.5*r <= 1800;
s.t. c3:  -x1  +4*x2  +17**.5*r <=   23;
s.t. c4:  -x1                +r <=    0;
s.t. c5:         -x2         +r <=    0;

solve;
display x1, x2, r;
end;
