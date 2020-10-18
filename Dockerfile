FROM debian:buster-slim
RUN mkdir /usr/share/Ampnado
COPY ampnado /usr/share/Ampnado
WORKDIR /usr/share/Ampnado
RUN \
	chmod -R 0755 /usr/share/Ampnado && \
	chown -R root:root /usr/share/Ampnado && \
	apt-get update && \
	apt-get dist-upgrade -y && \
	apt-get autoclean -y && \
	apt-get autoremove -y && \
	apt-get install python3-pip -y && \
	pip3 install --no-cache-dir -r /usr/share/Ampnado/requirements.txt && \
	rm -f /usr/share/Ampnado/requirements.txt

CMD [ "python3", "/usr/share/Ampnado/ampnado.py" ]
