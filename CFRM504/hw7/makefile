q1 := q1/call.pdf q1/delta.pdf q1/gamma.pdf q1/vega.pdf

.PHONY: all clean

all: $(q1)

clean:
	@rm -f $(q1)

$(q1): q1/main.py
	@cd q1 && ./main.py
