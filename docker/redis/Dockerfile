FROM redis:latest

ARG password

RUN mkdir -p /usr/local/etc/redis
RUN echo "bind 0.0.0.0" > /usr/local/etc/redis/redis.conf
RUN echo "requirepass $password" >> /usr/local/etc/redis/redis.conf

CMD [ "redis-server", "/usr/local/etc/redis/redis.conf" ]

RUN redis-cli
RUN "AUTH $password"
RUN SET messages []
RUN exit