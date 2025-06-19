from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from models.database import Base

class Dish(Base):
    __tablename__ = "dishes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String)
    price = Column(Float, nullable=False)
    category = Column(String)

    orders = relationship("Order", secondary="order_dish_association", back_populates="dishes")