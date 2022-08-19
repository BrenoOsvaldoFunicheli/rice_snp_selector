from sqlalchemy import create_engine, MetaData, Table, Column, ForeignKey
from sqlalchemy.ext.automap import automap_base

def get_engine(path="sqlite:///mydatabase.db"):
    # engine, suppose it has two tables 'user' and 'address' set up
    return create_engine(path)

def get_metadata(engine):
    # produce our own MetaData object
    metadata = MetaData()

    # we can reflect it ourselves from a database, using options
    # such as 'only' to limit what tables we look at...
    metadata.reflect(engine)

    return metadata

def reflect_schema(metadata):
    # we can then produce a set of mappings from this MetaData.
    Base = automap_base(metadata=metadata)

    # calling prepare() just sets up mapped classes and relationships.
    Base.prepare()

    return Base

