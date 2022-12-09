.PHONY: build publish shell

build:
	docker build -t kyokley/quick-word .

shell: build-dev
	docker run --rm -it --entrypoint /bin/bash kyokley/quick-word

publish: build
	docker push kyokley/quick-word
