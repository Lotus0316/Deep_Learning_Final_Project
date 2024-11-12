#encoding=utf-8
#用于将预测结果还原为字符串
import pandas as pd
df_u=pd.read_csv(r"用户名和用户编号.csv")
df_shop=pd.read_csv(r"店铺名和店铺编号.csv")
d={}
for x,y in zip(df_u["用户名"],df_u["用户编号"]):
    d[y]=x
for x,y in zip(df_shop["店铺名"],df_shop["店铺编号"]):
    d[y]=x
    

with open("edge_ID.txt","w") as f0:
    with open("G_edges.txt","r") as f:
        data=f.readlines()
        for x in data:
            try:
                x = x.strip("\n").split("\t")
                print(x)
                f0.write(d[int(x[0])])
                f0.write("\t")
                f0.write(d[int(x[1])])
                f0.write("\t")
                f0.write(x[2])
                f0.write("\n")
            except:
                pass

with open("node_type_ID.txt","w") as f0:
    with open("node_type.txt","r") as f:
        data=f.readlines()
        for x in data:
            try:
                x = x.strip("\n").split("\t")
                print(x)
                f0.write(d[int(x[0])])
                f0.write("\t")
                f0.write(x[1])
                f0.write("\n")
            except:
                pass