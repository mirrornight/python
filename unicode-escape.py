# coding=utf-8
'''在将unicode存储到文本的过程中，还有一种存储方式，不需要将unicode转换为实际的文本存储字符集，
而是将unicode的内存编码值进行存储，读取文件的时候再反向转换回来，是采用：unicode-escape的转换方式。'''

s = u'中文'
print s
a = s.encode('unicode-escape')
print a
print s.encode('unicode-escape').decode('unicode-escape')

f = open('unicode_escape.txt', 'w')
f.write(a)
f.close()