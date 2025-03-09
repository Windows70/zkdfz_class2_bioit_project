import pandas as pd

# 加载 TSV 文件
degs_up = pd.read_csv("GSE97760_DEGs_up_mapped.tsv", sep="\t")

# 提取基因名称列并保存为纯文本文件
degs_up["GENE_SYMBOL"].to_csv("GSE97760_DEGs_up_genes.txt", index=False, header=False)

# 对另一个文件执行相同操作
degs_up_5281 = pd.read_csv("GSE5281_DEGs_up.tsv", sep="\t")
degs_up_5281["Gene.symbol"].to_csv("GSE5281_DEGs_up_genes.txt", index=False, header=False)

# 提取下调 DEGs 的基因名称
degs_down = pd.read_csv("GSE97760_DEGs_down_mapped.tsv", sep="\t")
degs_down["GENE_SYMBOL"].to_csv("GSE97760_DEGs_down_genes.txt", index=False, header=False)

degs_down_5281 = pd.read_csv("GSE5281_DEGs_down.tsv", sep="\t")
degs_down_5281["Gene.symbol"].to_csv("GSE5281_DEGs_down_genes.txt", index=False, header=False)