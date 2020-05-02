build:
	@docker build -t twint_playground .

run:
	@docker run \
			--name twint_playground \
			--rm \
			-e PYTHONDONTWRITEBYTECODE=1 \
			-v $(PWD):/src \
			twint_playground

jupyter-start:
	@docker run \
		--name jupyter \
		-d \
		-e JUPYTER_ENABLE_LAB=yes \
		-p 8888:8888 \
		-v $(PWD)/data:/home/jovyan/data \
		-v $(PWD)/notebooks:/home/jovyan/notebooks \
		jupyter/scipy-notebook
	@sleep 1
	@make -s jupyter-url

jupyter-url:
	@docker exec -it jupyter jupyter notebook list

jupyter-stop:
	@docker stop jupyter
	@docker rm jupyter
