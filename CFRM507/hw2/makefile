qe5 := qe5/main.pdf

.PHONY: all clean

all: $(qe5)

clean:
	@rm -f $(qe5)

$(qe5): qe5/main.py
	@cd qe5 && ./main.py
