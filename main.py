import asyncio
import uvicorn
from fastapi import FastAPI

from config import HOST
from database import Base, engine
from routes.authentication import router as auth_router
from routes.user import router as user_router
from routes.chat import router as chat_router

app = FastAPI()

app.include_router(auth_router)
app.include_router(user_router)
app.include_router(chat_router)


async def main():
    async with engine.begin() as connect:
        await connect.run_sync(Base.metadata.create_all)

    uvicorn.run(app='main:app', reload=True, host=HOST)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Closed')


