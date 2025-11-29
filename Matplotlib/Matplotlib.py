import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np  # 加上这行，给numpy起别名np，就能用np来调用numpy的功能了

# 模拟数据：不同样本的某指标测量值（带组别信息）
data = pd.DataFrame({
    "组别": ["样本A"]*30 + ["样本B"]*30 + ["样本C"]*30,
    "指标值": np.concatenate([
        np.random.normal(5, 1, 30),  # 样本A：均值5，标准差1
        np.random.normal(7, 1.2, 30),# 样本B：均值7，标准差1.2
        np.random.normal(6, 0.8, 30) # 样本C：均值6，标准差0.8
    ])
})

# 用seaborn画箱线图（展示分布和异常值）
sns.boxplot(x="组别", y="指标值", data=data, palette="Set2")
sns.swarmplot(x="组别", y="指标值", data=data, color="black", size=3)  # 叠加原始数据点

plt.title("不同样本的指标值分布", fontsize=12)
plt.ylabel("指标值", fontsize=10)
plt.savefig("指标分布箱线图.png", dpi=300)
plt.show()