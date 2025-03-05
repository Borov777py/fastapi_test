from pydantic import BaseModel


class UserAuthSchema(BaseModel):
    name: str
    password: str

    class Config:
        json_schema_extra = {
            'example': {
                'name': 'test',
                'password': 'test'
            }
        }


class UserDataSchema(BaseModel):
    id: int
    name: str
    password: str
    balance: int

    class Config:
        json_schema_extra = {
            'example': {
                'id': 0,
                'name': 'test',
                'password': 'test',
                'balance': 0
            }
        }



