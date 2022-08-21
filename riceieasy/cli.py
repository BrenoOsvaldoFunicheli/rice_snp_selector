"""Console script for riceieasy."""
import sys
import click
import pandas as pd
from sys import path 
from sqlalchemy import create_engine



@click.group()
def main(args=None):
    """Console script for riceieasy."""
    click.echo("Replace this message by putting your code into "
               "riceieasy.cli.main")
    click.echo("See click documentation at https://click.palletsprojects.com/")
    return 0

@main.command()
def download():
    base_path = path[0] # + '/database/data/'
    
    database_path = base_path+'/rice_i_easy.db'

    engine = create_engine(f"sqlite:///{database_path}")
    
    print(pd.DataFrame(engine.execute("select * from sqlite_master")))
    # print(__name__)
    """Simple program that greets NAME for a total of COUNT times."""
    pd.DataFrame(["a","b"]).to_csv("d.csv")


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
