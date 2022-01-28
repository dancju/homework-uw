.PHONY: all clean

all: q4/a.pdf q4/c.pdf

clean:
	@rm -f q4/a.pdf
	@rm -f q4/c.pdf

q4/a.pdf: q4/a.py
	@cd q4 && ./a.py

q4/c.pdf: q4/c.py
	@cd q4 && ./c.py
