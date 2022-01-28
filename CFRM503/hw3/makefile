q3 := q3/rf.pdf q3/mu.pdf q3/sigma2.pdf

.PHONY: all clean

all: $(q3)

clean:
	@rm -f $(q3)

$(q3): q3/main.py
	@cd q3 && ./main.py
