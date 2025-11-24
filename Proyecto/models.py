"""
SQLAlchemy models for the PC Store database.
"""
from sqlalchemy import Column, Integer, String, Float, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
import uuid

Base = declarative_base()


class User(Base):
    """User model for authentication and profile information."""
    __tablename__ = 'users'
    
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    email = Column(String(255), unique=True, nullable=False, index=True)
    password_hash = Column(String(255), nullable=False)
    fecha_nacimiento = Column(String(50), nullable=True)
    pais = Column(String(100), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f"<User(id={self.id}, email='{self.email}')>"


class Product(Base):
    """Product model for PC components."""
    __tablename__ = 'products'
    
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    nombre = Column(String(255), nullable=False)
    precio = Column(Float, nullable=False)
    imagen = Column(String(500), nullable=True)
    categoria = Column(String(50), nullable=False, index=True)  # 'mobo' or 'cpu'
    marca = Column(String(50), nullable=False, index=True)      # 'amd' or 'intel'
    socket = Column(String(50), nullable=False)                 # 'am5', 'lga1700', etc.
    stock = Column(Integer, nullable=False, default=0)          # Stock disponible
    
    def __repr__(self):
        return f"<Product(id={self.id}, nombre='{self.nombre}', stock={self.stock})>"
