import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel('나트륨.xlsx')

plt.figure(num="나이별 나트륨 섭취량 그래프")

plt.rcParams.update({'font.family': 'malgun gothic','font.size': 12})

plt.title("나이별 나트륨 섭취량")

plt.xlabel('섭취량')
plt.ylabel('나이')


plt.show()