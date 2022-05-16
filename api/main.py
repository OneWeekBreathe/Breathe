import uvicorn

from fastapi import FastAPI

from starlette.middleware.errors import ServerErrorMiddleware

from api.app.routes.api import router as api_router
from api.app.errors.generic_error import generic_error_handler
from api.core import config
from api.core.events import create_start_app_handler, create_stop_app_handler


def get_application() -> FastAPI:
    application = FastAPI(
        title=config.PROJECT_NAME,
        debug=config.DEBUG,
        description=config.API_DESCRIPTION,
        version=config.VERSION,
        docs_url=None,
        redoc_url=None,
        openapi_url=None
    )

    application.add_event_handler("startup", create_start_app_handler(application))
    application.add_event_handler("shutdown", create_stop_app_handler(application))

    application.add_middleware(ServerErrorMiddleware, handler=generic_error_handler)

    application.include_router(api_router)
    return application


app = get_application()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
