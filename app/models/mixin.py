from sqlalchemy.orm import declared_attr, Mapped, mapped_column
from sqlalchemy import func
from datetime import datetime


class CommonMixin:
    @declared_attr.directive
    def __tablename__(cls) -> str:
        return cls.__name__.lower()

    id: Mapped[int] = mapped_column(primary_key=True, unique=True, autoincrement=True)


class TimestampMixin:
    created_at: Mapped[datetime] = mapped_column(default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        default=func.now(), onupdate=func.now()
    )
