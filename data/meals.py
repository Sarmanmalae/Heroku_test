import sqlalchemy

from data.db_session import SqlAlchemyBase


class Meals(SqlAlchemyBase):
    __tablename__ = 'menu'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    category = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    price = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    in_stock = sqlalchemy.Column(sqlalchemy.Boolean)
