from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from models.database import Base

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    customer_name = Column(String, nullable=False)
    order_time = Column(DateTime, default=datetime.utcnow)
    status = Column(String, default="в обработке")

    dishes = relationship("Dish", secondary="order_dish_association", back_populates="orders")