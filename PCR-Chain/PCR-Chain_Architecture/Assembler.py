from Unit import AI_Unit, Non_AI_Unit
from Module import Module
import os
import pandas as pd
import time
class Assembler:
    def __init__(self):
        pass
    def assemble(self, obj, input = "", preunits = [], premodules = [], value4Conditon = "", assertion = []):
        if isinstance(obj, (AI_Unit, Non_AI_Unit)):
            obj.preunits = preunits
            obj.value4Conditon = value4Conditon
            obj.inputs = input
            obj.assertion = assertion
        elif(isinstance(obj, Module)):
            obj.premodules = premodules
            obj.value4Conditon = value4Conditon
        else:
            print("Error: The object is not a unit or module")

    def Run(self, obj):
        if isinstance(obj, (AI_Unit, Non_AI_Unit)):
            pass
        elif(isinstance(obj, Module)):
            # 查找module中的unit
            if obj.unit == []:
                if obj.module == []:
                    print("Error: The module is empty")
                else:
                    for i in range(len(obj.module)):
                        # 递归执行module
                        self.Run(obj.module[i])
            else:
                dict = {}
                for unit in obj.unit:
                    for u in unit.preunits:
                        dict[u.output_des] = u.output
                    # 执行unit
                    if unit.condition == True:
                        # 第0个是code，第1个是assertion
                        if unit.preunits[1].output in unit.assertion:
                            if isinstance(unit, AI_Unit):
                                unit.output = unit.AIRun(dict)
                            elif isinstance(unit, Non_AI_Unit):
                                unit.output = unit.NonAIRun(dict)
                            else:
                                print("Error: The unit is not a AI_Unit or Non_AI_Unit")
                        else:
                            print(unit.output)
                    else:
                        if isinstance(unit, AI_Unit):
                            unit.output = unit.AIRun(dict)
                        elif isinstance(unit, Non_AI_Unit):
                            unit.output = unit.Non_AIRun(dict)
                        else:
                            print("Error: The unit is not a AI_Unit or Non_AI_Unit")
        else:
            print("Error: The object is not a unit or module")


if __name__ == "__main__":
    if not os.path.exists("../data/java_code.txt"):
        raise Exception("Not found java_code.txt")
    code = open("../data/java_code.txt", "r").read()
    # 存数据的unit0，不需要执行
    data_unit = Non_AI_Unit(output = code, output_des="code")
    AI_Unit1 = AI_Unit(promptName="Simplename_Extraction", output_des="simplename")
    AI_Unit2 = AI_Unit(promptName="Simplename_to_FQN", output_des="FQN")
    Non_AI_Unit1 = Non_AI_Unit(output_des="code")
    Sub_module1 = Module()
    Sub_module1.contain(AI_Unit1)
    Sub_module1.contain(AI_Unit2)
    Sub_module1.contain(Non_AI_Unit1)
    AI_Unit3 = AI_Unit(promptName="Code_Check", output_des="assertion")
    AI_Unit4 = AI_Unit(promptName="Code_Fix", output_des="code", condition=True)
    Sub_module2 = Module()
    Sub_module2.contain(AI_Unit3)
    Sub_module2.contain(AI_Unit4)
    assembler = Assembler()
    # partical code reuse module
    Root_module = Module()
    Root_module.contain(Sub_module1)
    Root_module.contain(Sub_module2)
    # link of module in root module
    assembler.assemble(Sub_module1, premodules=[])
    assembler.assemble(Sub_module2, premodules=[Sub_module1])
    # link of unit in sub module1
    assembler.assemble(AI_Unit1, preunits=[data_unit])
    assembler.assemble(AI_Unit2, preunits=[data_unit, AI_Unit1])
    assembler.assemble(Non_AI_Unit1, preunits=[data_unit, AI_Unit2])
    # link of unit in sub module2
    assembler.assemble(AI_Unit3, preunits=[Non_AI_Unit1])
    assembler.assemble(AI_Unit4, preunits=[Non_AI_Unit1, AI_Unit3], assertion=["Yes"])
    assembler.Run(Root_module)
