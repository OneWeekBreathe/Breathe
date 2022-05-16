from fastapi import APIRouter
from api.app.models.schemas.status import HealthCheck
from api.resources import strings


router = APIRouter()


@router.get("/health", name=strings.API_GET_HEALTH_STATUS)
async def health_check() -> HealthCheck:
    health_check_result = HealthCheck(strings.OK)
    return health_check_result
