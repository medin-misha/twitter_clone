from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, declare_attr

class Base(DeclarativeBase):
    __abstract__ = True
    @declared_attr.DeclarativeBase
    def __tablename__(cls) -> str:
        return f"{cls.__name__.lower()}"
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    