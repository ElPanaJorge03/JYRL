import os
import bcrypt
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.exc import IntegrityError
from .models import Base, User, Product

# Database configuration
DATABASE_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "database")
DATABASE_PATH = os.path.join(DATABASE_DIR, "store.db")
DATABASE_URL = f"sqlite:///{DATABASE_PATH}"

# Create database directory if it doesn't exist
os.makedirs(DATABASE_DIR, exist_ok=True)

# Create engine and session
engine = create_engine(DATABASE_URL, echo=False, connect_args={"check_same_thread": False})
session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)


def init_db():
    Base.metadata.create_all(engine)
    print(f"Database initialized at: {DATABASE_PATH}")


class DatabaseService:
    
    def __init__(self):
        self.session = Session()
    
    def __del__(self):
        if hasattr(self, 'session'):
            self.session.close()
    
    def signup(self, email: str, password: str, fecha_nacimiento: str = "", pais: str = "") -> dict:
        try:
            # Check if user already exists
            existing_user = self.session.query(User).filter_by(email=email).first()
            if existing_user:
                return {"error": "El usuario ya existe."}
            
            # Hash password
            password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            
            # Create new user
            new_user = User(
                email=email,
                password_hash=password_hash,
                fecha_nacimiento=fecha_nacimiento,
                pais=pais
            )
            
            self.session.add(new_user)
            self.session.commit()
            
            return {"success": "Cuenta creada exitosamente."}
            
        except IntegrityError:
            self.session.rollback()
            return {"error": "El usuario ya existe."}
        except Exception as e:
            self.session.rollback()
            return {"error": f"Error al crear cuenta: {str(e)}"}
    
    def login(self, email: str, password: str) -> dict:
        try:
            user = self.session.query(User).filter_by(email=email).first()
            
            if not user:
                return {"error": "Credenciales incorrectas."}
            
            # Verify password
            if bcrypt.checkpw(password.encode('utf-8'), user.password_hash.encode('utf-8')):
                return {"success": "Inicio de sesión exitoso."}
            else:
                return {"error": "Credenciales incorrectas."}
                
        except Exception as e:
            return {"error": "Credenciales incorrectas."}
    
    # ==================== Product Query Methods ====================
    
    def get_products_by_category_and_brand(self, categoria: str, marca: str) -> list[dict]:
        try:
            products = self.session.query(Product).filter_by(
                categoria=categoria,
                marca=marca
            ).all()
            
            return [self._product_to_dict(p) for p in products]
        except Exception as e:
            print(f"Error querying products: {e}")
            return []
    
    def get_all_products(self) -> list[dict]:
        """Get all products."""
        try:
            products = self.session.query(Product).all()
            return [self._product_to_dict(p) for p in products]
        except Exception as e:
            print(f"Error querying all products: {e}")
            return []
    
    def _product_to_dict(self, product: Product) -> dict:
        """Convert Product model to dictionary."""
        return {
            "id": product.id,
            "nombre": product.nombre,
            "precio": product.precio,
            "imagen": product.imagen or "",
            "categoria": product.categoria,
            "marca": product.marca,
            "socket": product.socket,
            "stock": product.stock
        }


init_db()

db_service = DatabaseService()
