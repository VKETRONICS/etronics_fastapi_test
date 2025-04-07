import logging
from fastapi import FastAPI, Request

app = FastAPI()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("test-webhook")

@app.post("/webhook")
async def webhook_test(request: Request):
    data = await request.body()
    logger.info(f"📩 Получен POST /webhook: {data}")
    return {"ok": True}

@app.get("/")
async def root():
    return {"status": "бот работает, ждёт POST на /webhook"}
