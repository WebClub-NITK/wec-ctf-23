FROM nginx:1.23.3-alpine

RUN apk add iptables

COPY flag.html /usr/share/nginx/html/flag.html

COPY entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh

ENTRYPOINT [ "/entrypoint.sh" ]

CMD ["nginx", "-g", "daemon off;"]


