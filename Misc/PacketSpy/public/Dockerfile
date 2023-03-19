FROM nginx:1.23.3-alpine

RUN apk add iptables

COPY red_herring /red_herring

RUN mkdir /WEC

COPY hidden_treasure /WEC/hidden_treasure

COPY flag.txt /WEC/flag.txt

COPY README.md /README.md

COPY top_secret.pdf /WEC/top_secret.pdf

COPY flag.txt /flag.txt

COPY flag.html /usr/share/nginx/html/flag.html

COPY entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh



