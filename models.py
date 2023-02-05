from datetime import datetime
from app import db


class MockCard:
    def __init__(self, _id=0, title="title", price=200, img_src="", counter=0):
        self.id = str(_id)
        self.title = title
        self.price = price
        self.img_src = img_src
        self.counter = counter


class Role(db.Model):
    __tablename__ = "Role"
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    name = db.Column(db.TEXT, unique=True)

    def __repr__(self):
        return f'<Role {self.name}>'


class Admin(db.Model):
    __tablename__ = "Admin"
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    login = db.Column(db.TEXT)
    password = db.Column(db.TEXT)


class User(db.Model):
    __tablename__ = "User"
    id = db.Column(db.INTEGER, primary_key=True)
    name = db.Column(db.TEXT)
    lastName = db.Column(db.TEXT)
    id_role = db.Column(db.INTEGER, db.ForeignKey("role.id"), default=1)
    role = db.relationship("Role", back_populates="user")
    orders = db.relationship("Order", back_populates="user", cascade="all, delete-orphan")


class Point(db.Model):
    __tablename__ = "Point"
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    name = db.Column(db.TEXT, default="", unique=True)
    link = db.Column(db.TEXT, unique=True)
    # order = db.relationship("Order", back_populates="point", cascade="all, delete-orphan")


class OrderProduct(db.Model):
    __tablename__ = "OrderProduct"
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)

    id_order = db.Column(db.ForeignKey("order.id"))
    id_product = db.Column(db.ForeignKey("product.id"))

    quantity = db.Column(db.INTEGER, default=0)

    order = db.relationship("Order", back_populates="products")
    product = db.relationship("Product", back_populates="orders")


class Product(db.Model):
    __tablename__ = "Product"
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)

    name = db.Column(db.TEXT)
    # description = db.Column(db.TEXT, default="")
    picture = db.Column(db.TEXT, default="/static/images/not_img.png")  # TODO: Maby blob
    price = db.Column(db.DECIMAL)
    quantity = db.Column(db.INTEGER, default=0)

    orders = db.relationship("Order", secondary="orderproduct", back_populates="orders")


class Order(db.Model):
    __tablename__ = "Order"
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)

    id_user = db.Column(db.INTEGER, db.ForeignKey("User.id"))
    id_point = db.Column(db.INTEGER, db.ForeignKey("Point.id"))
    # default = datetime.now, onupdate = datetime.now
    timestamp = db.Column(db.DATETIME, index=True, default=datetime.utcnow)
    typePay = db.Column(db.TEXT, default="Ear")  # TODO: Add table TypePay
    status = db.Column(db.TEXT, default="Pending")  # TODO: Add table Status

    user = db.relationship("User", back_populates="orders")
    point = db.relationship("Point", back_populates="order")

    products = db.relationship("Product", secondary="OrderProduct", back_populates="products")
