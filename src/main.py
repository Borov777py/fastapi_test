import asyncio
import uvicorn
from fastapi import FastAPI

from db.database import Base, engine
from api.authentication import router as auth_router
from api.users import router as user_router
from api.messages import router as chat_router

app = FastAPI()


for router in (auth_router, user_router, chat_router):
    app.include_router(router)


async def main():
    async with engine.begin() as connect:
        await connect.run_sync(Base.metadata.create_all)

    uvicorn.run(app='main:app', reload=True, host='0.0.0.0', port=8000)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Closed')
