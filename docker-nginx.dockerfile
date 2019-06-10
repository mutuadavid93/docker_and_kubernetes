# Dockerfile which will be used to create the reverse proxy image.

FROM nginx:latest

# copy nginx.conf after copying to the proxy container
COPY ./.docker/config/nginx.conf /etc/nginx/nginx.conf

ENTRYPOINT [ "nginx" ]
CMD [ "-g","daemon off;" ]