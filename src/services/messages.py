from typing import Type

from src.schemas.messages import MessageAddSchema
from src.utils.storage import Storage


class MessagesService:
    def __init__(self, storage: Type[Storage]):
        self.storage = storage

    def add_new_message(self, send_name: str, data: MessageAddSchema):
        message = f'{send_name}: {data.message}'
        if self.storage.add_message(message) is not False:
            return True
        return False

    def get_messages(self):
        if (messages := self.storage.get_data_messages()) is not None:
            return messages
        return None



