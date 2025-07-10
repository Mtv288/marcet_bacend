from __future__ import annotations
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, validates
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, Date, DateTime, Enum, BigInteger


class Base(AsyncAttrs, DeclarativeBase):
    pass


class User(Base):
    """
    id: индификатор в бд
    email = емаил пользователя
    hashed_password = верефекационный пароль высланый на емаил
    name = имя, или имя представителя если выбрана компания
    city = город пользователя или представителя компании
    phone_number = Column(String, index=True)
    name_company = Column(String, nullable=True)
    company = True если не individual = True и не retoucher = True по дефолту False
    individual = True если не company = True и не retoucher = True по дефолту False
    agreement = принятое соглашение должно быть True по дефолту False
    bad_token = устаревший токен если разлогинен
    """
    __tablename__ = "sideuser"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String, index=True)
    company = Column(Boolean, index=True, default=False)
    individual = Column(Boolean, index=True, default=False)
    agreement = Column(Boolean, index=True, default=False)
    admin = Column(Boolean, index=True, default=False)
    phone_number = Column(String, index=True)
    name_company = Column(String, index=True)
    name = Column(String, index=True)
    city = Column(String, index=True)



