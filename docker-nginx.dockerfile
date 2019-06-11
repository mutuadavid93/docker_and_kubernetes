# Dockerfile which will be used to create the reverse proxy image.

FROM nginx:latest

# copy nginx.conf after copying to the proxy container
COPY ./.docker/config/nginx.conf /etc/nginx/nginx.conf

# copy self-signing certificates.
COPY ./.certs/server.crt /etc/nginx/server.crt
COPY ./.certs/server.key /etc/nginx/server.key

# Make cert only available to owner
RUN chmod 600 /etc/nginx/server.key

EXPOSE 80 443

ENTRYPOINT [ "nginx" ]
CMD [ "-g","daemon off;" ]