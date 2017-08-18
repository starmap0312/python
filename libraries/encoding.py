# -*- coding: utf-8 -*-
# the above declares that this script is stored as UTF-8 format, because it contains '中文'

# 1) Ольга
print(u'\u041e\u043b\u044c\u0433\u0430')                                     # Ольга 
# 1.1) u'...':
#      if you wanted a Unicode value, then using a Unicode literal (u'...') is all you needed to do
#      no further decoding is necessary.
print(repr(u'\u041e\u043b\u044c\u0433\u0430'))                               # u'\u041e\u043b\u044c\u0433\u0430'
# 1.2) encode():
#      the above string is a Unicode string, so it only makes sense to encode it to utf8 
#      you cannot decode Unicode data, it is already decoded
print(repr(u'\u041e\u043b\u044c\u0433\u0430'.encode('utf8')))                # '\xd0\x9e\xd0\xbb\xd1\x8c\xd0\xb3\xd0\xb0'
# 1.3) decode():
print(repr(u'\u041e\u043b\u044c\u0433\u0430'.encode('utf8').decode('utf8'))) # u'\u041e\u043b\u044c\u0433\u0430'

# 2) 中文
print(u'中文')                                     # 中文
print(repr(u'中文'))                               # u'\u4e2d\u6587' 
print(repr(u'中文'.encode('utf8')))                # '\xe4\xb8\xad\xe6\x96\x87' 
print(repr(u'中文'.encode('utf8').decode('utf8'))) # u'\u4e2d\u6587'
