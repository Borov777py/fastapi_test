from pydantic import BaseModel


class MessageAddSchema(BaseModel):
    message: str

    class Config:
        json_schema_extra = {
            'example': {
                'message': 'test_message'
            }
        }