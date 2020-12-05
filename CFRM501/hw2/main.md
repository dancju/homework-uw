---
title: CFRM 501, 2020 Autumn, HW 2
...

# Q1

In the arithmetic return case, the final asset value would be

$$100\times(1+0.2)\times(1-0.35)=78$$

dollars. The arithmetic return does not aggregate additively because

$$100\times(1+0.2)\times(1-0.35)\ne 100\times(1+0.2-0.35).$$

In the logarithmic return case, the final asset value would be

$$100\,e^{0.2}e^{-0.35}\approx 86.07079764250578$$

dollars. The logarithmic return aggregates additively because

$$100\,e^{0.2}e^{-0.35}=100\,e^{0.2-0.35}.$$

# Q2

The values of two assets in the profolio is $3\times100=300$ and $2\times250=500$.

In the arithmetic return case, the final value of the portfolio is

$$300(1+0.1)+500(1+0.15)=905.$$

The arithmetic return of the portfolio is a weighted average of the returns of its components because

$$
\frac{300(1+0.1)+500(1+0.15)}{300+500}=\frac{300}{300+500}(1+0.01)+\frac{500}{300+500}(1+0.15).
$$

In the logarithmic return case, the final value of the portfolio is

$$300\,e^{0.1}+500\,e^{0.15}\approx 912.4683967868358.$$

# Q3

|      |       Mean |   Variance |    Skewness |    Kurtosis |
| ---- | ---------: | ---------: | ----------: | ----------: |
| AMZN | $0.001484$ | $0.000360$ |  $0.292684$ |  $8.125978$ |
| GOOG | $0.000712$ | $0.000271$ | $-0.180082$ |  $9.832814$ |
| MSFT | $0.001341$ | $0.000302$ | $-0.015453$ | $14.243744$ |

## AMZN

\includegraphics{q3/AMZN.pdf}

## GOOG

\includegraphics{q3/GOOG.pdf}

## MSFT

\includegraphics{q3/MSFT.pdf}
