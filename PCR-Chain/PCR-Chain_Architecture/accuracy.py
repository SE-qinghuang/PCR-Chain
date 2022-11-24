import os
import pandas as pd

df = pd.read_csv("../data/data_add_import.csv")
orignal_data = "FQN"
success_data = "true_FQN"
orignal = df[orignal_data].tolist()
success = df[success_data]
true_num = 0
num = 0
for i in range(len(orignal)):
    p_true_num = 0
    p_num = 0
    orignal[i] = orignal[i].split('\n')
    success[i] = eval(success[i])
    num += len(success[i])
    p_true_num = len(success[i])
    for j in success[i]:
        if j in orignal[i]:
            true_num += 1
            p_num += 1
    if p_num / p_true_num <= 1 :
        print(success[i])
        print(orignal[i])
    print("precision: ", p_num / p_true_num)
    print(str(p_num)+" / "+str(p_true_num) + "\n")
print(true_num/num)
print("\n")
print(true_num)
print("\n")
print(num)
# with open("../data_1/test_FQN_ground_truth.jsonl", "r", encoding="utf-8") as f:
    # read the file line by line
    # true_simplenames = []
    # i = 0
    # for line in f:
    #     sns = []
    #     FQNs = []
    #     keys=list(eval(line).keys())[0]
    #     val = eval(line).values()
    #     sn_FQN_pair = list(val)[0]
    #     for i in range(len(sn_FQN_pair)):
    #         sn = list(sn_FQN_pair[i].keys())[0]
    #         sns.append(sn)
    #         FQN = list(sn_FQN_pair[i].values())[0]
    #         FQNs.append(FQN)
    #     true_simplenames.append(sns)
    #     # 存到与df["code_name"]对应的位置
    #     # df.loc[df["code_name"] == keys, "true_simplenames"] = str(sns)
    #     df.loc[df["code_name"] == keys, "true_FQN"] = str(FQNs)
    #
    #
    # # 存到csv文件中
    # df.to_csv("../data/data.csv", index=False)