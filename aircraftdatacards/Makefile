.SUFFIXES: .json .pdf

.json.pdf:
	python3 aircraftdatacards.py $*.json

all						:	\
	sandbox.pdf				\
	australian.pdf			\
	british.pdf				\
	canadian.pdf			\
	chinese.pdf				\
	european.pdf			\
	french.pdf				\
	italian.pdf				\
	bombers.pdf 			\
	bomber-fighters.pdf		\
	all.pdf

# We force these since in most cases the aircraft data files will have changed.
sandbox.pdf				:	.FORCE
all.pdf					:	.FORCE
australian.pdf			:	.FORCE
british.pdf				:	.FORCE
canadian.pdf			:	.FORCE
chinese.pdf				:	.FORCE
european.pdf			:	.FORCE
french.pdf				:	.FORCE
italian.pdf				:	.FORCE
bombers.pdf				:	.FORCE
bomber-fighters.pdf		:	.FORCE

format		:
	python3 format.py

types					:	.FORCE
	rm -f types/*.json
	python3 make-types.py
	$(MAKE) -j3 types-for-version-1 types-for-version-2 types-for-version-3
	rm -f types/*.json

types-for-version-1		:	.FORCE
	version=1 make types-for-version
types-for-version-2		:	.FORCE
	version=2 make types-for-version
types-for-version-3		:	.FORCE
	version=3 make types-for-version

types-for-version		:	.FORCE
	mkdir -p types/version-$$version
	ls types/*.json |														\
	sed 's:.*/::;s/\.json//' | 												\
	while read typename; do 												\
		cp types/"$$typename".json type-$$version.json; 					\
		version=$$version python3 aircraftdatacards.py type-$$version.json;	\
	  	version=$$version python3 aircraftdatacards.py type-$$version.json;	\
	  	mv type-$$version.pdf types/version-$$version/"$$typename".pdf;		\
	  	rm type-$$version.*; 												\
	done

collections				:	.FORCE
	ls collections/*.json | \
	sed 's/\.json//' | \
	while read basename; do \
	  echo "$$basename"; \
	  cp "$$basename".json collection.json; \
	  python3 aircraftdatacards.py collection.json; \
	  python3 aircraftdatacards.py collection.json; \
	  mv collection.pdf "$$basename".pdf; \
	done

example-adcs:
	version=1 make example-adc.pdf && mv example-adc.pdf example-adc-v1.pdf
	version=2 make example-adc.pdf && mv example-adc.pdf example-adc-v2.pdf
	version=3 make example-adc.pdf && mv example-adc.pdf example-adc-v3.pdf

push-descriptions:
	python3 push-descriptions.py

pull-descriptions:
	python3 pull-descriptions.py

clean		:
	rm -f *.pdf *.aux *.log *.synctex.gz *.fls *.toc *.out

blacken		:
	blacken .

.FORCE		:
