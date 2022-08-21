from .config import get_schema, get_engine
from . import managers 
from .managers import rap_table, msu_table

class Search:
    def __init__(self, conn) -> None:
        self.conn = conn

    @property
    def rapdb(self):
        return managers.ConcreteGeneDatabase(self.conn, rap_table)