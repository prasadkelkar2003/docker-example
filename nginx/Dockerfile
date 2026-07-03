FROM nginx:alpine

# Install custom nginx config
COPY nginx.conf /etc/nginx/
COPY docker-example.nginx.conf /etc/nginx/conf.d/

# The alpine variant configuration takes care of routing out of the box,
# but replacing the default configuration ensures our custom mappings take over.
RUN rm -f /etc/nginx/conf.d/default.conf
