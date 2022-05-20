'''
author:g
data:5.20
SaveTxt
'''
import os 
class SaveTxt():
    '''
    保存txt文件的路径
    mod是否清除原文件内容 True
    '''
    def __init__(self,name_txt,path_dir,mod) -> None:
        self.name_txt = name_txt
        self.path_dir = path_dir
        self.mod = mod
    '''
    输入的为字符串
    ''' 
    def save(self,data):
        os.makedirs(self.path_dir, exist_ok=True)
        self.path_txt = self.path_dir + "/" + self.name_txt
        if self.mod:
            with open(self.path_txt,"a") as f:
                f.write(data+"\n")
        else:
            with open(self.path_txt,"w") as f:
                f.write(data+"\n")