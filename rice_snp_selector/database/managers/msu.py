from typing import List
from .base import GeneDatabase, StructureDatabase
import pandas as pd
from pandas import DataFrame

class Table:
    """
    This class handle the database tables that
    have data belong the rapdb
    """
    # generic
    gene = 'msu_msu_osa1r7_gene'
    mrna = 'msu_msu_osa1r7_mRNA'
    exon = 'msu_msu_osa1r7_exon'
    five_utr = 'msu_msu_osa1r7_five_prime_utr'
    cds = 'msu_msu_osa1r7_cds'
    three_utr = 'msu_msu_osa1r7_three_prime_utr'

    all_structures="msu"
