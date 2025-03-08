from schemas.messages import MessageAddSchema
from db.storage import Storage


class MessagesService:
    storage = Storage

    @classmethod
    def add_new_message(cls, send_name: str, data: MessageAddSchema):
        message = f'{send_name}: {data.message}'
        if cls.storage.add_message(message) is not False:
            return True
        return False

    @classmethod
    def get_messages(cls):
        if (messages := cls.storage.get_data_messages()) is not None:
            return messages
        return None



