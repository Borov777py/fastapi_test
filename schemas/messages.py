from pydantic import BaseModel
from typing import List


class MessageAddSchema(BaseModel):
    message: str

    class Config:
        json_schema_extra = {
            'example': {
                'message': 'test_message'
            }
        }
