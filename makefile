pdf := $(patsubst %.md, %.pdf, $(shell find . -name 'main.md'))

.PHONY: all clean

all:
	@cd CFRM501 && make all
	@cd CFRM503 && make all
	@cd CFRM504 && make all
	@cd CFRM505 && make all
	@cd CFRM507 && make all
	@make $(pdf)

clean:
	@rm -f $(pdf)
	@cd CFRM501 && make clean
	@cd CFRM503 && make clean
	@cd CFRM504 && make clean
	@cd CFRM505 && make clean
	@cd CFRM507 && make clean

%.pdf: %.md
	@cd $(abspath $(shell dirname $^)) && pandoc --pdf-engine=xelatex --template homework --pdf-engine-opt=-shell-escape -o $(notdir $@) $(notdir $^)
