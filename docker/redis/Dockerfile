FROM redis:latest

RUN mkdir -p /usr/local/etc/redis
RUN echo "bind 0.0.0.0" > /usr/local/etc/redis/redis.conf
RUN echo "requirepass $REDIS_PASSWORD" >> /usr/local/etc/redis/redis.conf

CMD [ "redis-server", "/usr/local/etc/redis/redis.conf" ]

CMD [ "redis-cli", "AUTH", "$REDIS_PASSWORD"]
CMD [ "redis-cli", "SET", "messages", "[]" ]