import pandas as pd

# 加载 GPL 文件
gpl_annotation = pd.read_csv("GPL16699-15607.txt", sep="\t", comment="#")

# 提取 ID 和 GENE_SYMBOL 列
probe_to_gene = gpl_annotation[["ID", "GENE_SYMBOL"]]

# 去除空值（如果某些探针没有对应的基因符号）
probe_to_gene = probe_to_gene.dropna()

# 保存映射表
probe_to_gene.to_csv("probe_to_gene_mapping.tsv", sep="\t", index=False)

# 加载 GSE97760_DEGs_down.tsv
degs_97760 = pd.read_csv("GSE97760_DEGs_up.tsv", sep="\t")

# 加载探针到基因符号的映射表
probe_to_gene = pd.read_csv("probe_to_gene_mapping.tsv", sep="\t")

# 将 DEGs 的 ID 列映射到基因符号
degs_97760_mapped = degs_97760.merge(probe_to_gene, left_on="ID", right_on="ID", how="left")

# 保存映射后的结果
degs_97760_mapped.to_csv("GSE97760_DEGs_up_mapped.tsv", sep="\t", index=False)