var c >= 0;
var t >= 0;

maximize obj: 10 * c * log(c) + 90 * c + 250 * t * log(t) + 80 * t;

s.t. c0: 5 * c + 40 * t <= 4000;
s.t. c1: 3 * c + 10 * t <= 1800;
s.t. c2: -c + 4 * t <= 23;

option solver baron;
solve;
display c, t;
