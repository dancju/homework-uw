q4 := q4/main.pdf

.PHONY: all clean

all: $(q4)

clean:
	@rm -f $(q4)

$(q4): q4/plot.py
	@cd q4 && ./plot.py
