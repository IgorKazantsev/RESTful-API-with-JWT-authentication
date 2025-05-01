from fastapi import FastAPI
from app.routers import auth_router, book_router, comment_router, log_router
from app.core.database import Base, engine
from fastapi.openapi.utils import get_openapi

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Raamatute API",
    description="RESTful API JWT autentimisega. Admin ja User rollid. Võimaldab raamatute haldust ja kommenteerimist.",
    version="1.0.0"
)

# Swagger "Authorize" nupp ja JWT tugi
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title=app.title,
        version=app.version,
        description=app.description,
        routes=app.routes,
    )
    openapi_schema["components"]["securitySchemes"] = {
        "BearerAuth": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT",
        }
    }
    for path in openapi_schema["paths"].values():
        for method in path.values():
            method["security"] = [{"BearerAuth": []}]
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi

# Routerid
app.include_router(auth_router.router, prefix="/auth", tags=["Auth"])
app.include_router(book_router.router, prefix="/books", tags=["Books"])
app.include_router(comment_router.router, prefix="/comments", tags=["Comments"])
app.include_router(log_router.router, prefix="/logs", tags=["Logs"])
