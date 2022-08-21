from typing import List
from .base import ConcreteGeneDatabase, StructureDatabase
import pandas as pd
from pandas import DataFrame

class Table:
    """
    This class handle the database tables that
    have data belong the rapdb
    """
    # generic
    gene ='rapdb_all_gene'
    mrna ='rapdb_all_mRNA'
    exon ='rapdb_all_exon'
    cds ='rapdb_all_CDS'
    five_utr ='rapdb_all_five_prime_UTR'
    three_utr ='rapdb_all_three_prime_UTR'

    all_structures='rapdb_all_structure',
    

    # specific tables
    rep_gene ='rapdb_irgsp1_locus_gene'
    pred_gene ='rapdb_irgsp1_predicted_locus_gene'
    pred_cds = 'rapdb_irgsp1_prediction_CDS'
    pred_exon = 'rapdb_irgsp1_prediction_exon'
    pred_mrna = 'rapdb_irgsp1_prediction_mRNA'
    rep_cds = 'rapdb_irgsp1_rep_CDS'
    rep_exon = 'rapdb_irgsp1_rep_exon'
    rep_5utr = 'rapdb_irgsp1_rep_five_prime_UTR'
    rep_mrna = 'rapdb_irgsp1_rep_mRNA'
    rep_3utr = 'rapdb_irgsp1_rep_three_prime_UTR'



