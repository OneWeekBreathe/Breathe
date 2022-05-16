from collections import defaultdict
from typing import Any, DefaultDict, Dict, Optional

from fastapi import APIRouter, Request
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.openapi.utils import get_openapi

from api.core import config

from api.app.routes import health

core_tags_metadata = [
    {"name": "health", "description": "Verify that the API is up and running"},
]

router = APIRouter()

# Core API
core_router = APIRouter(prefix=config.API_PREFIX)
core_router.include_router(health.router, tags=["health"])

core_swagger_router = APIRouter()

openapi_definitions: DefaultDict[str, Optional[Dict[str, Any]]] = defaultdict(lambda: None)


@core_swagger_router.get("/openapi.json", include_in_schema=False, name="core_openapi")
async def core_openapi(request: Request):
    global openapi_definitions

    if openapi_definitions["core"] is None:
        openapi_definitions["core"] = get_openapi(
            title=f"{config.PROJECT_NAME}",
            description=config.API_DESCRIPTION,
            version=config.VERSION,
            routes=core_router.routes,
            tags=core_tags_metadata
        )

    return openapi_definitions["core"]


@core_swagger_router.get("/docs", include_in_schema=False, name="core_swagger")
async def get_swagger(request: Request):
    swagger_ui_html = get_swagger_ui_html(
        openapi_url="openapi.json",
        title=request.app.title + " - Swagger UI",
    )

    return swagger_ui_html

core_router.include_router(core_swagger_router)
router.include_router(core_router)
