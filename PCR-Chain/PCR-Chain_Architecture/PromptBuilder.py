import re
import os


class PromptBuilder:
    def __init__(self):
        pass

    # 用于维护prompt的函数
    @staticmethod
    def upload(PromptName, PromptPath):
        pass
        # promptConfig[PromptName] = PromptPath
        # return promptConfig

    # 用于查找对应PromptName的函数，并把inputs放进去
    # 此处的inputs是一个字典
    @staticmethod
    def createPrompt(PromptName, inputs):
        if PromptName is None:
            raise Exception("No " + PromptName + "provided")
        if not os.path.exists("../PromptTemplate/" + PromptName + ".txt"):
            raise Exception("No template found for " + PromptName)
        # 按照PromptName读取文件
        prompt_template = open("../PromptTemplate/" + PromptName + ".txt", "r").read()
        # 这里应该加一个分步的步骤，我们应该把prompt细分，例如description和demo inputs and outputs

        # 获得模板中的参数名称
        para_name = PromptBuilder.getPromptParams(prompt_template)
        prompt_replaced = ''
        if inputs is None:
            raise Exception("No inputs provided")
        else:
            for index,key in enumerate(para_name):
                if key not in inputs:
                    raise Exception("No " + key + " provided")
                # 从inputs中拿相应的参数替换模板中的参数
                else:
                    if prompt_replaced == '':
                        # 之前我们的字典中的value可以是一个list，现在我们只使用单输出的情况
                        prompt_replaced = prompt_template.replace("{{%s}}" % key, inputs[key])
                    else:
                        prompt_replaced = prompt_replaced.replace("{{%s}}" % key, inputs[key])
            # print("---------------------------------------------------------------------")
            # print("the final prompt after replacement:" + "\n" + prompt_replaced + "\n")
            a = 1
        return prompt_replaced

    # 从这个函数可以知道某一步需要什么样的输入
    @staticmethod
    def getPromptParams(prompt_template):
        if re.search(r"{{\w+}}", prompt_template):
            paraNames = re.findall(r"{{.*}}", prompt_template)
            for i in range(len(paraNames)):
                paraNames[i] = paraNames[i][2:-2]
        return paraNames