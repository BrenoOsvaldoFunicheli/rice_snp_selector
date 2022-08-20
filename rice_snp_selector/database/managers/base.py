from abc import ABC, abstractmethod
from typing import List, Tuple
from pandas import DataFrame


class Ba:

    def resumed(self):
        pass

    def expand(self):
        pass


class BaseDatabase(ABC):

    def __init__(self, conn):
        
        self.conn = conn

    def process_snp(self, snp:str) -> Tuple:

        try:
            
            splited_snp = snp.split('_')
            chromossome = splited_snp[0][1:] 

            if len(chromossome) == 1:
                chromossome = "chr0"+chromossome
            else:
                chromossome = "chr"+chromossome

            pos = splited_snp[1]

        except Exception as e:
            raise e(f"The SNP {snp} doesn't have correct format")

        return  chromossome, pos

    def make_where_condition_with_snp(self, snp_list: List[str]) -> str:

        where_condition_list = [] # will be store all where condition

        for snp in snp_list:
            # pass snp and get chromossome and position
            chromossome, pos = self.process_snp(snp)

            # format the snp to make sql query
            where_condition = f"(seq_id = '{chromossome}' AND start <= {pos} AND end >= {pos})"

            where_condition_list.append(where_condition)

        where = " OR ".join(where_condition_list)

        return where

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
    def get_genes_info_by_ref(self, snp)->DataFrame:
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

class StructureDatabase(ABC):

    @abstractmethod
    def get_structure_on_chr(self, chromossome:int, start:int, end:int):
        pass

    @abstractmethod
    def get_structure_by_snp(self, snp:str):
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
