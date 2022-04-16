# 保存数据--txt文件
import os

fold = "Basic/run/test"
os.makedirs(fold,exist_ok=True)
path = fold+"test.txt"
# 使用"a"不会消除上次的数据,"w"会消除
with open(path,"a") as f:
    f.write("只是简单的测试文件")
    f.write('\n') #换行
# 存储数据
epoch = 1
batch_size =2
# 两个数据 *2
s = ("%10.4g  "*2) % (epoch, batch_size)
with open(path,"a") as f:
    f.write(s)
    f.write('\n') #换行

