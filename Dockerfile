FROM python:3
WORKDIR /usr/src/ampnado
COPY ampnado .
RUN \
	pip install --no-cache-dir -r requirements.txt && \
	rm -f ./requirements.txt
CMD [ "python", "./ampnado.py" ]
