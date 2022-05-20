'''
author:g
data:2022.5.20
ParamsFlops
data:
'''
from thop import profile,clever_format
class ParamsFlops():
    '''model,input保持一致
    input:tuple类型
    计算模型的参数量
    '''
    def __init__(self,model,inputs) -> None:
        super().__init__()
        self.model = model
        self.inputs = inputs
        self.flops,self.params = profile(self.model,inputs=(self.inputs))
        self.flops,self.params = clever_format([self.flops,self.params],"%f")
    def getparams(self):
        '''
        返回参数量 单位M
        '''
        return self.params
    def getflops(self):
        '''
        返回浮点数运算数量 单位M
        '''
        return self.flops
    def getparamsflops(self):
        '''
        返回参数量 单位M
        返回浮点数运算数量 单位M
        '''
        return self.params,self.flops
    def getmodel(self):#->dict  
        '''
        返回输入的模型
        '''      
        return self.model
    def getinput(self):#->tensor
        '''
        返回输入的tensor
        '''
        return self.input

if __name__ == "__main__":
    pass