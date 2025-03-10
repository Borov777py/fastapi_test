import redis
import json
import os

from schemas.messages import MessageAddSchema


class MessagesService:
    _key = 'messages'

    _storage = redis.Redis(host=os.environ['REDIS_HOST'], port=os.environ['REDIS_PORT'], password=os.environ['REDIS_PASSWORD'], decode_responses=True)
    _storage.auth(password=os.environ['REDIS_PASSWORD'])

    @classmethod
    def add_new_message(cls, send_name: str, data: MessageAddSchema):
        message = f'{send_name}: {data.message}'

        if (messages := cls.get_messages()) is not None:
            messages.append(message)
            cls._storage.set(name=cls._key, value=json.dumps(messages))
            return True
        return False

    @classmethod
    def get_messages(cls):
        if (messages := cls._storage.get(name=cls._key)) is None:
            cls._storage.set(name=cls._key, value=json.dumps([]))
            cls.get_messages()
        else:
            try:
                return json.loads(messages)
            except:
                return None



