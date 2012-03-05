#coding=utf-8
from types import StringTypes


def parse_list(values,message):
    '''parse list to protobuf message'''
    if isinstance(values[0],dict):#value needs to be further parsed
        des = message._message_descriptor
        class_name = des.name
        for v in values:
            cmd = message.add()
            parse_dict(v,cmd)
    else:#value can be set
        message.extend(values)


def parse_dict(values,message):
    for k,v in values.iteritems():
        if isinstance(v,dict):#value needs to be further parsed
            parse_dict(v,getattr(message,k))
        elif isinstance(v,list):
            parse_list(v,getattr(message,k))
        else:#value can be set
            setattr(message, k, v)
            

