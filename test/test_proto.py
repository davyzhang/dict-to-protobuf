#coding=utf-8
'''
Created on Jul 2, 2012

@author: davyzhang
'''
import unittest
from protobuf.message_pb2 import CityAoi
from dict_to_protobuf import dict_to_protobuf


class Test(unittest.TestCase):

    def test_parse_dict(self):
        obj = {'player':[{'role_id':1,'target_x':23},{'role_id':2,'target_x':24}]}
        proto_obj = CityAoi()
        dict_to_protobuf(obj, proto_obj)
        self.assertEqual(proto_obj.player[0].role_id, 1)
        self.assertEqual(proto_obj.player[1].target_x, 24)
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()