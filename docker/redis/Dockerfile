FROM redis:latest

WORKDIR /redis

COPY .env /redis

RUN mkdir -p /usr/local/etc/redis
RUN echo "bind 0.0.0.0" > /usr/local/etc/redis/redis.conf
RUN echo "requirepass $REDIS_PASSWORD" >> /usr/local/etc/redis/redis.conf
RUN cat /usr/local/etc/redis/redis.conf

CMD [ "redis-server", "/usr/local/etc/redis/redis.conf" ]

RUN redis-cli
RUN AUTH $REDIS_PASSWORD
RUN SET messages []
RUN exit