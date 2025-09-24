from pydantic import BaseModel


class BlurFilterResponse(BaseModel):
    message: str = "Placeholder message"
    errors: list[str] | None = None
