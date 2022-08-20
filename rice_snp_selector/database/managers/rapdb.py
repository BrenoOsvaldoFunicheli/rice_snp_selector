from typing import List
from .base import GeneDatabase, StructureDatabase
import pandas as pd
from pandas import DataFrame

class Table:
    """
    This class handle the database tables that
    have data belong the rapdb
    """

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

def query(table, columns="*", where=None):
    base = f"SELECT {columns} FROM {table}"

    if where:
        base+=f" WHERE {where}"

    return base

class RapDB(GeneDatabase):

    def get_genes_by_snps(self, snp_list: List[str]) -> DataFrame:        
        
        where = self.make_where_condition_with_snp(snp_list)

        # make sql queries
        rep_q = query(Table.rep_gene, where=where)
        pred_q = query(Table.pred_gene, where=where)
        
        # search genes on predicted and representative database
        predict_genes = pd.read_sql_query(pred_q, self.conn)
        representativ_genes = pd.read_sql_query(rep_q, self.conn)

        return pd.concat([predict_genes,representativ_genes])

    def get_genes_info_by_ref(self, snp_list) -> DataFrame:
        where = self.make_where_condition_by_snp(snp_list)

        # make sql queries
        rep_q = query(Table.rep_gene, where)
        pred_q = query(Table.pred_gene, where)
        
        # search genes on predicted and representative database
        predict_genes = pd.read_sql_query(pred_q, self.conn)
        representativ_genes = pd.read_sql_query(rep_q, self.conn)

        return pd.concat([predict_genes,representativ_genes])


    def get_gene_info_by_ref(self, snp) -> DataFrame:
        return super().get_gene_info_by_ref(snp)

    def get_genes_info_on_chr(self, chromossome: int, start: int, end: int):
        return super().get_genes_info_on_chr(chromossome, start, end)

    def get_genes_on_chr(self, chromossome: int, start: int, end: int):
        return super().get_genes_on_chr(chromossome, start, end)

    def get_genes(self, chromossome: int, pos: int, start: int, end: int):
        return super().get_genes(chromossome, pos, start, end)