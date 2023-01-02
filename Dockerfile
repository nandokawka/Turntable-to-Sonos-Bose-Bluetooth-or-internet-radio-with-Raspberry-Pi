FROM alpine:3.17.0

RUN apk add \
	alsa-lib \
	alsa-ucm-conf \
	alsa-utils \
	alsa-utils-doc \
	alsaconf \ 
	darkice \
	icecast

COPY ./src/startup.sh /bin/startup.sh

ENTRYPOINT ["/bin/startup.sh"]
