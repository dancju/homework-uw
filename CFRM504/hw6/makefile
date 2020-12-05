q1 := q1/c_d.pdf q1/f.pdf

.PHONY: all clean

all: $(q1)

clean:
	@rm -f $(q1)

$(q1): q1/main.py
	@cd q1 && ./main.py
