from logging import getLogger

from fastapi import APIRouter, HTTPException, UploadFile, status

from filters.blur.schemas import BlurFilterResponse
from filters.constants import ALLOWED_FILE_EXTENSIONS

router = APIRouter(prefix="/blur", tags=["Фильтрация"])

logger = getLogger("filters")

@router.post(
    path="/",
    summary="Фильтр размытия изображения",
)
async def post_image_gaussian_blur(radius: float, image: UploadFile) -> BlurFilterResponse:
    logger.info("Got new request for %s blur on image of size %s", radius, image.size)
    extension = image.filename.split(".")[-1] if image.filename and "." in image.filename else "None"
    if extension not in ALLOWED_FILE_EXTENSIONS:
        logger.warning("Got file of unkown extension: %s", extension)

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=(
                f"Unsupported file extension: {extension}. "
                f"Following extensions are allowed: {", ".join(ALLOWED_FILE_EXTENSIONS)}"
            ),
        )

    return BlurFilterResponse()
