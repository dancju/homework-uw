targets := q1/hist.pdf q1/path.pdf q3/hist.pdf q3/hist_cumulative.pdf q4/hist.pdf q4/hist_cumulative.pdf q5/path.pdf q5/drawdown.pdf

.PHONY: all clean

all: $(targets)

clean:
	@rm -f $(targets)

q1/hist.pdf q1/path.pdf: q1/main.py
	@cd q1 && ./main.py

q3/hist.pdf q3/hist_cumulative.pdf: q3/main.py
	@cd q3 && ./main.py

q4/hist.pdf q4/hist_cumulative.pdf: q4/main.py
	@cd q4 && ./main.py

q5/path.pdf q5/drawdown.pdf: q5/main.py
	@cd q5 && ./main.py
