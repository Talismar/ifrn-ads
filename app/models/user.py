from .base_model import BaseModel
from .mixin import CommonMixin, TimestampMixin
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String


class User(CommonMixin, TimestampMixin, BaseModel):
    name: Mapped[str] = mapped_column(String(length=120))
    email: Mapped[str] = mapped_column(String(length=120), unique=True)
    password: Mapped[str]
    tasks: Mapped["Task"] = relationship(back_populates="created_by")
