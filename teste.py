from rice_snp_selector import database

e = database.get_engine("sqlite:///rice_i_easy.db")

# searcher = database.rap(e)
class Table:
    gene="ic4r_bigd_gene"
    all_structures="ic4r_all_structure"

a = database.managers.MixDatabase(e, Table)

print(a.get_genes_by_snps(["S1_69675"]))

# r = searcher.get_genes_by_snps(["S1_69675"])

# print(r)


# r = searcher.get_genes_info_by_snps(["S1_69675","S1_69675","S1_69675","S1_69675"])

# print(r)

r = a.get_genes_on_chr(chromossome=1, start=1, end=200000)
print(r)

r = a.get_structure_on_chr(1,1,2000000, ["gene"])
print(r)


# r = searcher.get_genes_info_on_chr(chromossome=1, start=60675, end=100000)

# print(r)