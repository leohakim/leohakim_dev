FROM nginx:1.27-alpine

RUN rm -f /etc/nginx/conf.d/default.conf \
  && mkdir -p /usr/src/app/staticfiles /usr/src/app/media

COPY nginx.conf /etc/nginx/conf.d/default.conf
