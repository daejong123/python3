# -*- coding: utf-8 -*-
import sys
from sys import argv

def readfile(filename):
    '给定文件名，读取文件内容'
    with open(filename) as f:
        while True:
            line = f.readline()
            if len(line) == 0:
                break
            print(line)

def test_sys_argv():
    '测试传递参数，注意这里必须传3个参数， 因为第一个默认的参数就是文件名称'
    script,first,second,third = argv
    # script 默认的参数就是该文件的名称， 所以通常都是从第一个开始取参数 sys.argv[1]
    print ("The script is called: %s"% script)
    print ("Your first variable is: %s"% first)
    print ("Your second variable is: %s"% second)
    print ("Your third variable is: %s"% third)

#script start
if __name__ == '__main__':
    if len(sys.argv) == 4:
        test_sys_argv()
        sys.exit()

    if len(sys.argv) < 2:
        print("没有行为哦")
        sys.exit()

    if sys.argv[1].startswith("--"):
        option = sys.argv[1][2:]
        if option == "version":
            print("version123456")
        elif option == "help":
            print("help asdfasdf")
        else:
            print("other unknown")
        sys.exit()
    else:
        for filename in sys.argv[1:]:
            readfile(filename)
'''
当脚本作为执行脚本时__name__的值为__main__当脚本作为模块时__name__为模块文件名。
举个例子，a.py作为执行脚本时__name__的值是__main__。
有2个脚本，a.py和b.py，a中引入b,执行a.py时，在b中模块的__name__就是b.py
这样等价于在每个模块中写上if __name__ == '__main__': 可以在该模块内做我们自己的事情。
而别的模块调用该模块时，只能调用该模块下的方法或者类，而无法执行if __name__ == '__main__':下的脚本。
'''
