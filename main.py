import fastapi

from dogs import views as dog_views
from cats import views as cat_views

app = fastapi.FastAPI(docs_url="/api/docs")

app.include_router(router=dog_views.router)
app.include_router(router=cat_views.router)
