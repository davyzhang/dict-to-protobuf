#A simple and pure python way to translate python dict object to protobuf message

I used this for my own project

## Example
example proto:

	message items {
		message require {
			optional bool require_sex = 1; 
			repeated int32 fate = 2 [packed = true];
		}
		message attack_type {
			optional int32 max = 1;
			optional int32 min = 2;
		}
		optional int32 sub_type = 1;
		repeated int32 levels = 2 [packed = true];
		optional require req = 3;
		repeated attack_type attack = 4;
	}

generate the python code as down_pb2.py

python code:

	>>>from down_pb2 import items
	>>>item_message = items()
	>>>item_dict = {'req':{'require_sex':1,'fate':[12,34]},'attack':[{'max':29,'min':10},{'max':2,'min':1}]}
	>>>parse_dict(item_dict,item_message)
	>>>print item_message

let me know if there's any issue

## (Un)license

This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or distribute
this software, either in source code form or as a compiled binary, for any
purpose, commercial or non-commercial, and by any means.

In jurisdictions that recognize copyright laws, the author or authors of this
software dedicate any and all copyright interest in the software to the public
domain. We make this dedication for the benefit of the public at large and to
the detriment of our heirs and successors. We intend this dedication to be an
overt act of relinquishment in perpetuity of all present and future rights to
this software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <http://unlicense.org/>