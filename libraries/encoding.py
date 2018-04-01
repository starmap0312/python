# -*- coding: utf-8 -*-
# the above declares that this script is stored as UTF-8 format, because it contains '中文'

# unicode object is meant to handle text
# 1) text is a sequence of code points which may be bigger than a single byte
# 2) text can be encoded in a specific encoding to represent the text as raw bytes, ex. utf-8, latin-1, etc.
#    i.e. we can use encode([codec]) to convert a unicode object (text) into a str object (raw bytes)
# unicode object vs. str object:
# 1) unicode object is not encoded
#    the internal representation used by python is an implementation detail
#    we do not need to care about it as long as it can represent the code points we want
# 2) str object in Python 2 is a plain sequence of bytes, so it does not represent text
# 3) we can think of a unicode object as a general representation of some text, and
#    it can be encoded in many different ways into a sequence of binary data represented via a str object
# 4) using str object, you have a lower-level control on the single bytes of a specific encoding representation
#    whereas using unicode object, you can only control at the code-point level
# 5) in Python 3, unicode object is renamed to str object, and
#    there is a new bytes object for representing a plain sequence of bytes

print('ascii')                                     # ascii                      (a str object of ascii char)
print(repr('ascii'))                               # 'ascii'
print(type('ascii'))                               # <type 'str'>               
print
print('ascii'.decode())                            # ascii                      (a str object of ascii char)
print(repr('ascii'.decode()))                      # u'ascii'
print(type('ascii'.decode()))                      # <type 'unicode'>
print
print('中文')                                      # 中文                       (a str object of utf8 char)
print(repr('中文'))                                # '\xe4\xb8\xad\xe6\x96\x87'
print(type('中文'))                                # <type 'str'>
print
print(u'中文')                                     # 中文                       (a unicode object)
print(repr(u'中文'))                               # u'\u4e2d\u6587'
print(type(u'中文'))                               # <type 'unicode'>
print
print(u'中文'.encode('utf8'))                      # 中文 (encode() converts a unicode object into a str object)
print(repr(u'中文'.encode('utf8')))                # '\xe4\xb8\xad\xe6\x96\x87' (we encode using the right utf8 codec)
print(type(u'中文'.encode('utf8')))                # <type 'str'>
#print(u'中文'.encode())                           # we encode using the wrong codec, i.e. ascii codec 
# UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-1: ordinal not in range(128)
print
print('中文'.decode('utf8'))                       # 中文 (decode() converts a str object into a unicode object)
print(repr('中文'.decode('utf8')))                 # u'\u4e2d\u6587' (we decode using the right utf8 codec)
print(type('中文'.decode('utf8')))                 # <type 'unicode'>
print
print(u'中文'.encode('utf8').decode('utf8'))       # 中文
print(repr(u'中文'.encode('utf8').decode('utf8'))) # u'\u4e2d\u6587'
print(type(u'中文'.encode('utf8').decode('utf8'))) # <type 'unicode'>
print

# example: UnicodeDecodeError
#print('中文'.encode('utf8'))                      # 
# UnicodeDecodeError: 'ascii' codec can't decode byte 0xe4 in position 0: ordinal not in range(128)
# 1) encode() converts a "unicode" object into a "str" object
#    but here you have invoked it on a string object (because we do not have the u'')
#    so python has to convert the string to a unicode object first
#    python implicitly does the following for you:
#print('中文'.decode().encode('utf8'))             # decode the str object using the ascii codec 
#    that is why we get UnicodeDecodeError
# 2) to fix the issue, we need to decode the str object using the right codec, i.e. utf8 codec 
print('中文'.decode('utf8').encode('utf8'))        # 中文 
