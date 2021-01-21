targets := $(addprefix q2/, cdf_y.pdf pmf_l_10.pdf pmf_l_25.pdf pmf_l_50.pdf hist_l.pdf)

.PHONY: all clean

all: $(targets)

clean:
	@rm -f $(targets)

q2/cdf_y.pdf: q2/cdf_y.py
	@cd q2 && ./cdf_y.py

q2/pmf_l_10.pdf q2/pmf_l_25.pdf q2/pmf_l_50.pdf: q2/pmf_l.py
	@cd q2 && ./pmf_l.py

q2/hist_l.pdf: q2/hist_l.py
	@cd q2 && ./hist_l.py
