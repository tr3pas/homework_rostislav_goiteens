from pydantic import BaseModel, EmailStr, Field, field_validator


class AnimalModel(BaseModel):
    name: str = Field(...,)
    age : int = Field(...,)
    age: int = Field(...,)
    adoped: bool = Field(...,)
