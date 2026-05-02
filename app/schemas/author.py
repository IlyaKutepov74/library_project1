from datetime import date, datetime

from pydantic import BaseModel, ConfigDict, Field, field_validator


class AuthorBase(BaseModel):
    full_name: str = Field(
        ...,
        min_length=2,
        max_length=255,
        examples=["Лев Николаевич Толстой"],
    )

    birth_year: int | None = Field(
        default=None,
        ge=0,  # год >= 0
        examples=[1999],
    )

    bio: str | None = Field(
        default=None,
        max_length=5000,
        examples=["Великий русский писатель, автор знаметиного романа 'Война и мир'."],
    )

    @field_validator("full_name")
    @classmethod
    def validate_full_name(cls, value: str) -> str:
        """
        Валидация имени
        """
        value = value.strip()
        if not value:
            raise ValueError("ФИО автора не может быть пустым")
        return value

    @field_validator("birth_year")
    @classmethod
    def validate_birth_year(cls, value: int | None) -> int | None:
        """
        Валидация года рождения
        """
        if value is not None and value > date.today().year:
            raise ValueError("Год рождения не может быть в будущем")

        return value


class AuthorCreate(AuthorBase):
    pass


class AuthorUpdate(BaseModel):
    full_name: str = Field(
        ...,
        min_length=2,
        max_length=255,
    )

    birth_year: int | None = Field(
        default=None,
        ge=0,  # год >= 0
    )

    bio: str | None = Field(
        default=None,
        max_length=5000,
    )

    @field_validator("full_name")
    @classmethod
    def validate_full_name(cls, value: str | None) -> str | None:
        """
        Валидация имени
        """
        if value is None:
            return value

        value = value.strip()
        if not value:
            raise ValueError("ФИО автора не может быть пустым")
        return value

    @field_validator("birth_year")
    @classmethod
    def validate_birth_year(cls, value: int | None) -> int | None:
        """
        Валидация года рождения
        """
        if value is not None and value > date.today().year:
            raise ValueError("Год рождения не может быть в будущем")

        return value


class AuthorRead(BaseModel):
    id: int
    full_name: str
    birth_year: int | None
    bio: str | None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
