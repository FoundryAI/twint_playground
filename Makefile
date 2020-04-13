build:
	@docker build -t twint_playground .

run:
	@docker run \
			--name twint_playground \
			--rm \
			-e PYTHONDONTWRITEBYTECODE=1 \
			-v $(PWD):/src \
			twint_playground
