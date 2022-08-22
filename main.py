import fastapi

from dogs import views as dog_views

app = fastapi.FastAPI(docs_url="/api/docs")

app.include_router(router=dog_views.router)
