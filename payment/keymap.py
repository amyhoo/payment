# -*- coding: utf-8 -*-
#######################################################################################
# 内部字典与外部字典之间的对应与转换
# 使用该程序能够保持模块的独立性，外部的改动只需要改变字典的映射关系，无需改动内部模块代码
#######################################################################################

def output_info(info_dict,key_list,interface):
    '''
    将info_dict的信息按照kwargs中的字段收集起来，进行INTERFACE字典转换
    :param info_dict:内部信息字典
    :param key_list:本模块内部使用的key,用来过滤所需要的信息
    :param interface:内部key到外部key的映射
    :return:
    '''
    #out_key 不能重复
    if not isinstance(info_dict,dict):
        return info_dict

    if interface:
        if key_list:
            return  {out_key:info_dict[key] for key ,out_key in interface if key in key_list and key in info_dict}
        else:
            return  {out_key:info_dict[key] for key ,out_key in interface if key in info_dict}
    else:
        if key_list:
            return  {key:info_dict[key] for key  in key_list if key in info_dict}
        else:
            return  info_dict

def collect_info(info_dict,key_list,interface):
    '''
    将info_dict中的信息按照kwargs中的字段收集起来,进行INTERFACE字典转换
    :param info_dict:外部信息字典
    :param key_list:本模块内部使用的key,用来过滤所需要的信息
    :param interface:内部key到外部key的映射
    :return:
    '''
    #key 不能重复
    if not isinstance(info_dict,dict):
        return info_dict

    if interface:
        if  key_list:
            return  {key:info_dict[out_key] for key,out_key in interface if key in key_list and out_key in info_dict}
        else:
            return  {key:info_dict[out_key] for key,out_key in interface if  out_key in info_dict}
    else:
        if key_list:
            return  {key:info_dict[key] for key  in key_list if key in info_dict}
        else:
            return  info_dict
def get_value(interface,key,mode=0):
    '''
    :param interface:值对列表
    :param key:
    :return:
    '''
    if not mode:
        return [out_key for in_key,out_key in interface if in_key==key]
    else:
        return [in_key for in_key,out_key in interface if out_key==key]


if __name__=="__main__":
    print(collect_info({"good":1,"bad":"2"},None,None))