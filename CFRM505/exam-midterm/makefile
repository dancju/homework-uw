.PHONY: all clean

all: q1/b.pdf q1/c.pdf q2/main.pdf q3/main.pdf q4/main.pdf

clean:
	@rm -f q1/b.pdf
	@rm -f q1/c.pdf
	@rm -f q2/main.pdf
	@rm -f q3/main.pdf
	@rm -f q4/main.pdf

q1/b.pdf: q1/b.py
	@cd q1 && ./b.py

q1/c.pdf: q1/c.py
	@cd q1 && ./c.py

q2/main.pdf: q2/main.py
	@cd q2 && ./main.py

q3/main.pdf: q3/main.py
	@cd q3 && ./main.py

q4/main.pdf: q4/main.py
	@cd q4 && ./main.py
