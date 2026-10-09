from sqlalchemy import create_engine, Column, INTEGER, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker


engine = create_engine("sqlite:///digishop.db")
engine.connect()

Base = declarative_base()

# --------------- user database ---------------------
class User(Base):
    __tablename__ = "userInfo"

    id = Column(INTEGER, primary_key=True)
    name = Column(String)
    address = Column(String)
    score = Column(Float)

# --------------- product database ------------------
class Product(Base):
    __tablename__ = "productInfo"

    id = Column(INTEGER, primary_key=True)
    name = Column(String)
    numbers = Column(INTEGER)
    price = Column(INTEGER)
    rate = Column(Float)


Base.metadata.create_all(engine)

session = sessionmaker(bind=engine)
sessionLocal = session()

###################################################
# ------------------ user test -----------------------
# user1 = User(name="Mohammad", address="Ahwaz", score=4.9)
# user2 = User(name="Ali", address="Tehran", score=4.95)

# sessionLocal.add(user1)
# sessionLocal.add(user2)
# sessionLocal.commit()

# user3 = User(name="Mahan", address="Shiraz", score=4)
# user4 = User(name="Matin", address="Ahwaz", score=4.2)
# sessionLocal.add_all([user3, user4])
# sessionLocal.commit()

# users = sessionLocal.query(User).all()
# print(users)
# for item in users:
#     print("name: ", item.name)
#     print("add: ", item.address)
#     print("score: ", item.score)
#     print("-" * 30)

# ------------- product test --------------------
# pro1 = Product(name="Asus vivo", numbers=10, price=150000000, rate=4.9)
# pro2 = Product(name="msi katana", numbers=5, price=350000000, rate=4.8)
# pro3 = Product(name="hp", numbers=15, price=80000000, rate=4.25)
# pro4 = Product(name="Asus ROG", numbers=8, price=1500000000, rate=5)

# sessionLocal.add_all([pro1, pro2, pro3, pro4])
# sessionLocal.commit()

# --------------- Filter User ------------------------
# temp_user = sessionLocal.query(User).filter_by(address="Ahwaz").first()
# print(f"{temp_user.name}: {temp_user.address}")

# temp_user = sessionLocal.query(User).filter_by(address="Ahwaz", name="Mohammad").all()
# print(f"{temp_user[-1].name}: {temp_user[-1].address}")

# temp_user = sessionLocal.query(User).filter(User.score >= 4.9).all()
# print(temp_user)
# for item in temp_user:
#     print(item.name)
#     print(item.score)
#     print("-" * 30)

# temp_user = sessionLocal.query(User).filter(User.name.like("%Ali%")).all()
# print(temp_user)
# for item in temp_user:
#     print(item.name)
#     print(item.score)
#     print("-" * 30)

# --------------- Filter product --------------------
# temp_user = sessionLocal.query(Product).filter(Product.price > 100000000).all()
# print(temp_user)
# for item in temp_user:
#     print(item.name)
#     print(item.price)
#     print("-" * 30)


# temp_user = sessionLocal.query(Product).filter(Product.name.like("%Asus%")).all()
# print(temp_user)
# for item in temp_user:
#     print(item.name)
#     print(item.rate)
#     print("-" * 30)

# ------------- Update user --------------------
user = sessionLocal.query(User).filter_by(id=1).first()

# user.name = "Mohsen"
# user.address = "Tabriz"
# sessionLocal.commit()

# -------------- Delete user -------------------
# if user != None:
#     sessionLocal.delete(user)
#     sessionLocal.commit()

# --------------- Delete product ---------------
# Pros = sessionLocal.query(Product).filter(Product.price < 100000000).first()
# print(Pros)

# if Pros != None:
#     sessionLocal.delete(Pros)
#     sessionLocal.commit()

