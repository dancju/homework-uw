targets := src/tracking_error.pdf src/excess_return.pdf

.PHONY: all clean

all: $(targets)

clean:
	@rm -f $(targets)

$(targets): src/main.py
	@cd src && ./main.py
