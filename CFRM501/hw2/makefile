pdf := $(patsubst %_d.csv, %.pdf, $(shell find q3/ -name '*csv'))

.PHONY: all clean

all: $(pdf)

clean:
	@rm -f $(pdf)

q3/%.pdf: q3/main.py
	@cd q3 && ./main.py
