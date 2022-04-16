# 各种各样的函数
import torch
import math 
# 学习率函数
# warmup加余弦退货函数
def adjust_learning_rate(optimizer, current_epoch, max_epoch, lr_min=0, lr_max=0.1, warmup=True, warmup_epochs=15):
    warmup_epoch = warmup_epochs if warmup else 0
    current_epoch += 1
    if current_epoch <= warmup_epoch:
        lr = lr_max * current_epoch / warmup_epoch
    else:
        lr = lr_min + (lr_max-lr_min)*(1 + math.cos(math.pi * (current_epoch -
                                                     warmup_epoch) / (max_epoch - warmup_epoch))) / 2
    for param_group in optimizer.param_groups:
        param_group['lr'] = lr