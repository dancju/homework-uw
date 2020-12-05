q1 := q1/corr_resid.pdf q1/corr_return.pdf q1/IBM.pdf q1/MCD.pdf q1/MMM.pdf q1/WMT.pdf
q2 := q2/1.pdf q2/3.pdf

.PHONY: all clean

all: $(q1) $(q2)

clean:
	@rm -f $(q1) $(q2)

$(q1): q1/main.py
	@cd q1 && ./main.py

$(q2): q2/main.py
	@cd q2 && ./main.py
