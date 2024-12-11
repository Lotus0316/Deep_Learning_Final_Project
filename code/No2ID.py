#encoding=utf-8
#用于将预测结果还原为字符串
import pandas as pd
df_u=pd.read_csv("../cleaned_data/graph_data/user_id_and_no.csv")
df_shop=pd.read_csv("../cleaned_data/graph_data/bs_id_and_no.csv")
d={}
for x,y in zip(df_u["user_id"],df_u["user_no"]):
    d[y]=x
for x,y in zip(df_shop["bs_id"],df_shop["bs_no"]):
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