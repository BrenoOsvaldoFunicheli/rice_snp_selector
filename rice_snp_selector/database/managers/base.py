from abc import ABC, abstractmethod
from typing import List, Tuple
from pandas import DataFrame
import pandas as pd
import os

class Ba:

    def resumed(self):
        pass

    def expand(self):
        pass


class BaseDatabase(ABC):

    def __init__(self, conn):
        
        self.conn = conn

    def query(self, table, columns="*", where=None):

        if columns != "*":
            columns = " , ".join(columns)

        base = f"SELECT {columns} FROM {table}"

        if where:
            base+=f" WHERE {where}"

        return base

    def get_df_by_query(self, query):
        
        if os.getenv("DEBUG"):
            print(query)

        # search query 
        return pd.read_sql_query(query, self.conn)

    def format_chr(self, chromossome:int):

        str_chromossome = str(chromossome)

        format_chr = "chr"+str_chromossome
        
        return format_chr


    def process_snp(self, snp:str) -> Tuple:

        try:
            
            splited_snp = snp.split('_')

            chromossome = splited_snp[0][1:] 
            chromossome = self.format_chr(chromossome)
            
            pos = splited_snp[1]

        except Exception as e:
            raise e(f"The SNP {snp} doesn't have correct format")

        return  chromossome, pos


    def make_where_condition_with_snp(self, snp_list: List[str], chr_column="", start_column="", end_column="") -> str:

        where_condition_list = [] # will be store all where condition

        for snp in snp_list:
            # pass snp and get chromossome and position
            chromossome, pos = self.process_snp(snp)

            # format the snp to make sql query
            where_condition = f"({chr_column} = '{chromossome}' AND {start_column} <= {pos} AND {end_column} >= {pos})"

            where_condition_list.append(where_condition)

        where = " OR ".join(where_condition_list)

        return where

    def make_where_condition_with_chr(self, chromossome: int, start:int, end:int, chr_column:str="", start_column:str="", end_column:str="") -> str:

        format_chr = self.format_chr(chromossome)

        # format the snp to make sql query
        where_condition = f"({chr_column} = '{format_chr}' AND {start_column} >= {start} AND {end_column} <= {end})"

        return where_condition


class GeneDatabase(BaseDatabase):

    
    @abstractmethod
    def get_genes(self, chromossome:int, pos:int, start:int, end:int):

        if pos:
            self.get_gene_by_snp_coord(chromossome, start, end)    
        else:
            self.get_genes_by_coord(chromossome, pos)  

    @abstractmethod
    def get_genes_by_snps(self, snp_list:List[str]) -> DataFrame:
        """
        This method returns a dataframe with each position snp and 
        the correlated gene return.

        The SNP format need to be like a SX_YYYYYYY
        where X is a number of chromossome and YYYY is a position
        of SNP occur on chromossome.

        Ex:

        S5_9123231 -> Chromossome 5 on position 9123231
        S12_91231 -> Chromossome 12 on position 91231


        Args:
            snp (DataFrame): The SNP format need to be like a SX_YYYYYYY
            where X is a number of chromossome and YYYY is a position
            of SNP occur on chromossome.

            Ex:
                S5_9123231 -> Chromossome 5 on position 9123231
                S12_91231 -> Chromossome 12 on position 91231

        """
        pass

    @abstractmethod
    def get_genes_info_by_snps(self, snp_list:List[str])->DataFrame:
        """
       This method returns a dataframe with each position snp and 
        the correlated gene return and all information avaiable
        about each gene of the returned list.

        The SNP format need to be a query is like a SX_YYYYYYY
        where X is a number of chromossome and YYYY is a position
        of SNP occur on chromossome.

        Ex:

        S5_9123231 -> Chromossome 5 on position 9123231
        S12_91231 -> Chromossome 12 on position 91231


        Args:
            snp (DataFrame): The SNP format need to be like a SX_YYYYYYY
            where X is a number of chromossome and YYYY is a position
            of SNP occur on chromossome.

            Ex:
                S5_9123231 -> Chromossome 5 on position 9123231
                S12_91231 -> Chromossome 12 on position 91231

        """
        pass

    @abstractmethod
    def get_genes_on_chr(self, chromossome:int, start:int, end:int):
        """
        This method get a number of the chromossome and find 
        all genes that there are between start position
        and end position on the chromossome passed. 

        Args:
            chromossome (int): The Number of Interesset Chromossome
            start (int): Start position on chromossome
            end (int): End position on chromossome
        """
        pass

    @abstractmethod
    def get_genes_info_on_chr(self, chromossome:int, start:int, end:int):
        """
        This method get a number of the chromossome and find 
        all genes with available info, that there are between start position
        and end position on the chromossome passed. 

        Args:
            chromossome (int): The Number of Interesset Chromossome
            start (int): Start position on chromossome
            end (int): End position on chromossome
        """
        pass



class ConcreteGeneDatabase(GeneDatabase):

    def __init__(self, conn, table):
        super().__init__(conn)
        self.table = table

    def get_genes_by_snps(self, snp_list: List[str]) -> DataFrame:        
        
        # make where query 
        where = self.make_where_condition_with_snp(snp_list,"seq_id","start","end")

        # make sql queries
        query = self.query(self.table.gene, columns=["seq_id","source","type","start","end","id"], where=where)
        
        return self.get_df_by_query(query)

    def get_genes_info_by_snps(self, snp_list:List[str]) -> DataFrame:
       
        # make where query 
        where = self.make_where_condition_with_snp(snp_list,"seq_id","start","end")

        # make sql queries
        query = self.query(self.table.gene, where=where)
        
        return self.get_df_by_query(query)


    def get_genes_info_on_chr(self, chromossome: int, start: int, end: int):
        where = self.make_where_condition_with_chr(chromossome, start, end, "seq_id","start","end")

        query = self.query(self.table.gene, where=where)
        
        return self.get_df_by_query(query)


    def get_genes_on_chr(self, chromossome: int, start: int, end: int):
        where = self.make_where_condition_with_chr(chromossome, start, end, "seq_id","start","end")

        query = self.query(self.table.gene, columns=["seq_id","source","type","start","end","id"], where=where)
        
        return self.get_df_by_query(query)

    def get_genes(self, chromossome: int, pos: int, start: int, end: int):
        return super().get_genes(chromossome, pos, start, end)

class StructureDatabase(BaseDatabase):

    def format_structure(self, structure_list):


        structure_filter = ""

        if structure_list:

            if isinstance(structure_list, list):

                structures = ["'" + stc + "'" for stc  in structure_list  ]
                structure_filter = " AND type IN ( " + " ,".join(structures) + " )"
            else:
                structure_filter = f" AND type IN '{structure_list}'"

        return structure_filter

    def get_structure_on_chr(self, chromossome:int, start:int, end:int, structure_list:str = None):
        
        where = self.make_where_condition_with_chr(chromossome, start, end, "seq_id","start","end")

        stc_filter = self.format_structure(structure_list)
        complete_where_condition = where + stc_filter

        query = self.query(self.table.all_structures, where=complete_where_condition)

        return self.get_df_by_query(query)
        

    def get_structure_by_snp(self, snp_list:str,  structure_list:str = None):
        where = self.make_where_condition_with_snp(snp_list,"seq_id","start","end")

        stc_filter = self.format_structure(structure_list)
        complete_where_condition = where + stc_filter

        query = self.query(self.table.all_structures, where=complete_where_condition)

        return self.get_df_by_query(query)

class MixDatabase(StructureDatabase, ConcreteGeneDatabase):

    def do(self):
        pass


class Others(ABC):
    @abstractmethod
    def get_gene_info_by_id(self, identifier:str) -> DataFrame :
        """Returns the information about a gene 
        from a identifier

        Args:
            identifier (str): The database identifier

        Returns:
            Dict: returns a dict with information 
            about a gene passed
        """
        pass

    
    @abstractmethod
    def get_gene_by_snp(self, snp_id):
        pass

    @abstractmethod
    def get_gene_info_by_snp(self, snp_id):
        pass
