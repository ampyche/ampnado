#FROM python:3
FROM arm32v7/python3.8-alpine3.10
WORKDIR /usr/src/ampnado
COPY ampnado .
RUN \
	pip install --no-cache-dir -r requirements.txt && \
	rm -f ./requirements.txt
CMD [ "python", "./ampnado.py" ]
