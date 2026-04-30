from fastapi import FastAPI

app = FastAPI(title="Electronic Library API") #создает объект под приложение. Точка входа

@app.get("/health") #запрос на работоспособность сервера
async def health(): 
    return {"status": "ok"}


