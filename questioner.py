import pandas as pd
import random

df = pd.read_csv ('output_metrologiya_otvety.csv')

rand_list = [x for x in range(df.shape[0])]

random.shuffle(rand_list)
vopros_no = 0
reshennye = [451,97,321,72,256,343,57,99,519,55,53,52,200,102,
             111,534,475,171,459,568,563,40,353,247,278,204,89,
             328,93,497,145,192,382,61,450,449,369,79,524,96,373,
             186,240,100,21,472,533,322,337,223,460]
random.shuffle(reshennye)
for i in rand_list:
    vopros_no+=1
    print(vopros_no,"(",i,")",'. Тема вопроса: ', df.loc[i][6], sep = "")
    print(df.loc[i][0])  # row, column
    rand_list_mini = [x for x in range(1,5)]
    random.shuffle(rand_list_mini)
    n=0
    for j in rand_list_mini:
        n+=1
        print(n, ") ", df.loc[i][j][2:], sep = "")
    input()
    print("правильный ответ:", df.loc[i][1])
    print(df.loc[i][7],"\n")
