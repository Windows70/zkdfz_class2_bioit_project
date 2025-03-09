import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
# 加载 TSV 文件
data = pd.read_csv("GSE5281.top.table.tsv", sep="\t")

# 筛选 DEGs
degs = data[(abs(data["logFC"]) >= 1) & (data["adj.P.Val"] < 0.05)]


# 设置绘图风格
sns.set(style="whitegrid")

# 绘制火山图
plt.figure(figsize=(10, 6))
plt.scatter(data["logFC"], -np.log10(data["adj.P.Val"]),
            c=["red" if (abs(row["logFC"]) >= 1 and row["adj.P.Val"] < 0.05) else "black" for _, row in data.iterrows()],
            alpha=0.6)
plt.xlabel("log2 Fold Change")
plt.ylabel("-log10 Adjusted P-value")
plt.title("Volcano Plot - GSE5281")
plt.axhline(-np.log10(0.05), color="gray", linestyle="--")  # 添加 p 值阈值线
plt.axvline(-1, color="gray", linestyle="--")  # 添加 log2FC 阈值线
plt.axvline(1, color="gray", linestyle="--")  # 添加 log2FC 阈值线
plt.show()

# 保存上调和下调 DEGs
degs_up = degs[degs["logFC"] > 0]
degs_down = degs[degs["logFC"] < 0]

degs_up.to_csv("GSE5281_DEGs_up.tsv", sep="\t", index=False)
degs_down.to_csv("GSE5281_DEGs_down.tsv", sep="\t", index=False)

