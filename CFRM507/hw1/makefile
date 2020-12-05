q2 := q2/main.pdf

.PHONY: all clean

all: $(q2)

clean:
	@rm -f $(q2)

$(q2): q2/main.py
	@cd q2 && ./main.py
