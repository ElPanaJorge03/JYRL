import bcrypt
from .database_service import Session, init_db
from .models import User, Product


def seed_database():
    """Populate database with test data."""
    session = Session()
    
    try:
        # Clear existing data
        print("Clearing existing data...")
        session.query(Product).delete()
        session.query(User).delete()
        session.commit()
        
        # ==================== Create Users ====================
        print("Creating users...")
        
        # Admin user
        admin_password = bcrypt.hashpw("123456".encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        admin = User(
            email="admin@gmail.com",
            password_hash=admin_password,
            fecha_nacimiento="1990-01-01",
            pais="Colombia"
        )
        session.add(admin)
        
        # Test user
        test_password = bcrypt.hashpw("test123".encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        test_user = User(
            email="test@example.com",
            password_hash=test_password,
            fecha_nacimiento="1995-05-15",
            pais="México"
        )
        session.add(test_user)
        
        session.commit()
        print("✓ Users created")
        
        # ==================== Create Products ====================
        print("Creating products...")
        
        products = [
            # ========== AMD Motherboards (AM5) ==========
            Product(
                nombre="ASUS ROG STRIX X670E-E GAMING WIFI",
                precio=449.99,
                imagen="https://dlcdnwebimgs.asus.com/gain/8F7F3C8D-6D3E-4F4E-8F3D-0E3F5E5F5F5F/w800",
                categoria="mobo",
                marca="amd",
                socket="am5",
                stock=10
            ),
            Product(
                nombre="MSI MAG B650 TOMAHAWK WIFI",
                precio=249.99,
                imagen="https://storage-asset.msi.com/global/picture/image/feature/mb/B650/MAG-B650-TOMAHAWK-WIFI/msi-mag-b650-tomahawk-wifi-motherboard.png",
                categoria="mobo",
                marca="amd",
                socket="am5",
                stock=10
            ),
            Product(
                nombre="GIGABYTE B650 AORUS ELITE AX",
                precio=229.99,
                imagen="https://static.gigabyte.com/StaticFile/Image/Global/d5c5e5f5e5f5e5f5/Product/32767/png/500",
                categoria="mobo",
                marca="amd",
                socket="am5",
                stock=10
            ),
            Product(
                nombre="ASRock B650M Pro RS",
                precio=159.99,
                imagen="https://pg.asrock.com/mb/photo/B650M%20Pro%20RS(L1).png",
                categoria="mobo",
                marca="amd",
                socket="am5"
            ),
            
            # ========== Intel Motherboards (LGA1700) ==========
            Product(
                nombre="ASUS ROG MAXIMUS Z790 HERO",
                precio=629.99,
                imagen="https://dlcdnwebimgs.asus.com/gain/A5B5C5D5-E5F5-4F4E-8F3D-0E3F5E5F5F5F/w800",
                categoria="mobo",
                marca="intel",
                socket="lga1700",
                stock=10
            ),
            Product(
                nombre="MSI MAG B760 TOMAHAWK WIFI",
                precio=219.99,
                imagen="https://storage-asset.msi.com/global/picture/image/feature/mb/B760/MAG-B760-TOMAHAWK-WIFI-DDR4/msi-mag-b760-tomahawk-wifi-ddr4-motherboard.png",
                categoria="mobo",
                marca="intel",
                socket="lga1700",
                stock=10
            ),
            Product(
                nombre="GIGABYTE Z790 AORUS ELITE AX",
                precio=279.99,
                imagen="https://static.gigabyte.com/StaticFile/Image/Global/f5e5d5c5b5a5/Product/32768/png/500",
                categoria="mobo",
                marca="intel",
                socket="lga1700",
                stock=10
            ),
            Product(
                nombre="ASRock B760M Pro RS",
                precio=139.99,
                imagen="https://pg.asrock.com/mb/photo/B760M%20Pro%20RS(L1).png",
                categoria="mobo",
                marca="intel",
                socket="lga1700"
            ),
            
            # ========== AMD CPUs (AM5) ==========
            Product(
                nombre="AMD Ryzen 9 7950X",
                precio=549.99,
                imagen="https://www.amd.com/system/files/2022-08/616656-amd-ryzen-9-7950x-pib-1260x709.png",
                categoria="cpu",
                marca="amd",
                socket="am5",
                stock=10
            ),
            Product(
                nombre="AMD Ryzen 7 7800X3D",
                precio=449.99,
                imagen="https://www.amd.com/system/files/2023-04/709811-amd-ryzen-7-7800X3D-pib-1260x709.png",
                categoria="cpu",
                marca="amd",
                socket="am5",
                stock=10
            ),
            Product(
                nombre="AMD Ryzen 7 7700X",
                precio=299.99,
                imagen="https://www.amd.com/system/files/2022-08/616654-amd-ryzen-7-7700x-pib-1260x709.png",
                categoria="cpu",
                marca="amd",
                socket="am5",
                stock=10
            ),
            Product(
                nombre="AMD Ryzen 5 7600X",
                precio=229.99,
                imagen="https://www.amd.com/system/files/2022-08/616650-amd-ryzen-5-7600x-pib-1260x709.png",
                categoria="cpu",
                marca="amd",
                socket="am5",
                stock=10
            ),
            Product(
                nombre="AMD Ryzen 5 7600",
                precio=199.99,
                imagen="https://www.amd.com/system/files/2023-01/709809-amd-ryzen-5-7600-pib-1260x709.png",
                categoria="cpu",
                marca="amd",
                socket="am5",
                stock=10
            ),
            
            # ========== Intel CPUs (LGA1700 + LGA1200 for exception) ==========
            Product(
                nombre="Intel Core i9-14900K",
                precio=589.99,
                imagen="https://www.intel.com/content/dam/www/central-libraries/us/en/images/2023-10/14th-gen-core-i9-badge-rwd.png",
                categoria="cpu",
                marca="intel",
                socket="lga1700",
                stock=10
            ),
            Product(
                nombre="Intel Core i7-14700K",
                precio=409.99,
                imagen="https://www.intel.com/content/dam/www/central-libraries/us/en/images/2023-10/14th-gen-core-i7-badge-rwd.png",
                categoria="cpu",
                marca="intel",
                socket="lga1700",
                stock=10
            ),
            Product(
                nombre="Intel Core i5-14600K",
                precio=319.99,
                imagen="https://www.intel.com/content/dam/www/central-libraries/us/en/images/2023-10/14th-gen-core-i5-badge-rwd.png",
                categoria="cpu",
                marca="intel",
                socket="lga1700",
                stock=10
            ),
            Product(
                nombre="Intel Core i5-13400F",
                precio=199.99,
                imagen="https://www.intel.com/content/dam/www/central-libraries/us/en/images/2022-09/13th-gen-core-i5-badge-rwd.png",
                categoria="cpu",
                marca="intel",
                socket="lga1700",
                stock=10
            ),
            # Special exception case: LGA1200 CPU that works with specific LGA1700 board
            Product(
                nombre="Intel Core i7-10700K",
                precio=279.99,
                imagen="https://www.intel.com/content/dam/www/central-libraries/us/en/images/2020-04/10th-gen-core-i7-badge-rwd.png",
                categoria="cpu",
                marca="intel",
                socket="lga1200",
                stock=10
            ),
        ]
        
        session.add_all(products)
        session.commit()
        print(f"✓ {len(products)} products created")
        
        print("\n" + "="*50)
        print("Database seeded successfully!")
        print("="*50)
        print("\nTest Credentials:")
        print("  Admin: admin@gmail.com / 123456")
        print("  User:  test@example.com / test123")
        print(f"\nDatabase location: {session.bind.url}")
        
    except Exception as e:
        session.rollback()
        print(f"Error seeding database: {e}")
        raise
    finally:
        session.close()


if __name__ == "__main__":
    init_db()
    seed_database()
