### Hosting:
This is the server version and needs to be hosted.
`docker build . -t server`
`docker run --cap-add NET_ADMIN -d -p 80:80 server`
