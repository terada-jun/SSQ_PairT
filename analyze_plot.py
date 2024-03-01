import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib
df=pd.read_csv('SSQ_0126.csv')#データフレームに格納
df = pd.DataFrame(df).T#データフレーム転置
list= df.to_numpy().tolist()#二次元配列に変換
##List=[list[][i] for i in range(df.shape[1])]



data1=(list[0],list[1]) #タプルを作成
data2=(list[2],list[3])
data3=(list[4],list[5])
data4=(list[6],list[7])

fig, ax = plt.subplots(2,2,figsize=(8,8))
ax[0,0].set_title('Nausea-吐き気')
ax[0,0].set_xticklabels(['base','control'])
ax[0,0].boxplot(data1)


ax[0,1].set_title('Oculomotor-眼球疲労')
ax[0,1].set_xticklabels(['base','control'])
ax[0,1].boxplot(data2)

ax[1,0].set_title('Disorientation-方向感覚の喪失')
ax[1,0].set_xticklabels(['base','control'])
ax[1,0].boxplot(data3)

ax[1,1].set_title('TS-トータルスコア')
ax[1,1].set_xticklabels(['base','control'])
ax[1,1].boxplot(data4)
plt.show()
