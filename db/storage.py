import redis
import json
import os

# from config import HOST, REDIS_PASSWORD


class Storage:
    redis = redis.Redis(os.environ['REDIS_HOST'], os.environ['REDIS_PORT'], password=os.environ['REDIS_PASSWORD'], decode_responses=True)

    @classmethod
    def get_data_messages(cls):
        if (data := cls.redis.get('messages')) is not None:
            try:
                return json.loads(data)
            except:
                pass
        return None

    @classmethod
    def add_message(cls, message: str):
        if (messages := cls.get_data_messages()) is not None:
            messages.append(message)
            cls.redis.set('messages', json.dumps(messages))
            return True
        return False
