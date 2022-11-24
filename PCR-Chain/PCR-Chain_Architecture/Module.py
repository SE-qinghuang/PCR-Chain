from Unit import *

class Module:
    # 这里的一些值需要在执行完一个链后进行更新
    def __init__(self):
        # 这里unit用来装AI_Unit和Non_AI_Unit
        self.unit = []
        # 这里module用来装Module
        self.module = []
        # 设置每一个module的前置module
        self.premodules = []
        # 来自上一个module的最后一个unit的输出
        self.input = ""
        # 是这个module的最后一个unit的输出
        self.output = []
        # 这个module的最后一个unit的输出描述
        self.output_des = ""

    def contain(self, obj):
        if isinstance(obj, AI_Unit) or isinstance(obj, Non_AI_Unit):
            self.unit.append(obj)
        elif(isinstance(obj, Module)):
            self.module.append(obj)
        else:
            print("Error: The object is not a unit or module")