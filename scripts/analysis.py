import pandas as pd
import matplotlib.pyplot as plt
import os

path = "results"
# Check whether the specified path exists or not
isExist = os.path.exists(path)
if not isExist:
# Create a new directory because it does not exist
    os.makedirs(path)

df=pd.read_csv('data/iris/iris.csv')
df.columns=['sepal length','sepal width','petal length','petal width','class']

Setosa=df[df["class"]=="Iris-setosa"]
Versicolor=df[df["class"]=="Iris-versicolor"]
virginica=df[df["class"]=="Iris-virginica"]

#Compute Average Values for Three Classes
setosa_sp_len=round(Setosa["sepal length"].mean(),3)
setosa_sp_wid=round(Setosa["sepal width"].mean(),3)
setosa_pe_len=round(Setosa["petal length"].mean(),3)
setosa_pe_wid=round(Setosa["petal width"].mean(),3)
versi_sp_len=round(Versicolor["sepal length"].mean(),3)
versi_sp_wid=round(Versicolor["sepal width"].mean(),3)
versi_pe_len=round(Versicolor["petal length"].mean(),3)
versi_pe_wid=round(Versicolor["petal width"].mean(),3)
vir_sp_len=round(virginica["sepal length"].mean(),3)
vir_sp_wid=round(virginica["sepal width"].mean(),3)
vir_pe_len=round(virginica["petal length"].mean(),3)
vir_pe_wid=round(virginica["petal width"].mean(),3)
f = open("results/Average_Values.txt", "w")
f.write("Average Values for Three Classes\n")
f.write("Setosa:  sepal length:"+str(setosa_sp_len)+", sepal width:"+str(setosa_sp_wid)
        +", petal length:"+str(setosa_pe_len)+", petal width:"+str(setosa_pe_wid)+"\n")
f.write("Versicolor:  sepal length:"+str(versi_sp_len)+", sepal width:"+str(versi_sp_wid)
        +", petal length:"+str(versi_pe_len)+", petal width:"+str(versi_pe_wid)+"\n")
f.write("Virginica:  sepal length:"+str(vir_sp_len)+", sepal width:"+str(vir_sp_wid)
        +", petal length:"+str(vir_pe_len)+", petal width:"+str(vir_pe_wid)+"\n")
f.close()

#Analysis of Setosa
fig_setosa, (setosa1, setosa2) = plt.subplots(1, 2)
fig_setosa.suptitle('Setosa')
setosa1.scatter(Setosa["sepal length"],Setosa["sepal width"])
setosa1.set_xlabel("sepal length")
setosa1.set_ylabel("sepal width")
setosa1.set_title("sepal")
setosa2.scatter(Setosa["petal length"],Setosa["petal width"])
setosa2.set_xlabel("petal length")
setosa2.set_ylabel("petal width")
setosa2.set_title("petal")
fig_setosa.tight_layout()
plt.savefig("results/Setosa.png")

#Analysis of versicolor
fig_versi, (versi1, versi2) = plt.subplots(1, 2)
fig_versi.suptitle('Versicolor')
versi1.scatter(Versicolor["sepal length"],Versicolor["sepal width"])
versi1.set_xlabel("sepal length")
versi1.set_ylabel("sepal width")
versi1.set_title("sepal")
versi2.scatter(Versicolor["petal length"],Versicolor["petal width"])
versi2.set_xlabel("petal length")
versi2.set_ylabel("petal width")
versi2.set_title("petal")
fig_versi.tight_layout()
plt.savefig("results/Versicolor.png")

#Analysis of virginica
fig_virginica, (virginica1, virginica2) = plt.subplots(1, 2)
fig_virginica.suptitle('virginica')
virginica1.scatter(virginica["sepal length"],virginica["sepal width"])
virginica1.set_xlabel("sepal length")
virginica1.set_ylabel("sepal width")
virginica1.set_title("sepal")
virginica2.scatter(virginica["petal length"],virginica["petal width"])
virginica2.set_xlabel("petal length")
virginica2.set_ylabel("petal width")
virginica2.set_title("petal")
fig_virginica.tight_layout()
plt.savefig("results/virginica.png")