q1 := q1/main.pdf
q2 := q2/main.pdf

.PHONY: all clean

all: $(q1) $(q2)

clean:
	@rm -f $(q1) $(q2)

$(q1): q1/plotter-bootstrapping.py
	@cd q1 && ./plotter-bootstrapping.py

$(q2): q2/main.py
	@cd q2 && ./main.py
