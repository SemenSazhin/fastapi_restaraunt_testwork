from sqlalchemy import Table, Column, Integer, ForeignKey
from models.database import Base

order_dish_association = Table(
    "order_dish_association",
    Base.metadata,
    Column("order_id", Integer, ForeignKey("orders.id")),
    Column("dish_id", Integer, ForeignKey("dishes.id"))
)