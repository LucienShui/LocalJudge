#!/bin/python3
# coding=utf-8
import os
import platform

system = platform.system()

compiler = 'g++'
if system == 'Darwin':
    for i in range(5, 9):
        if os.path.isfile('/usr/local/bin/' + compiler + '-' + str(i)):
            compiler = 'g++' + '-' + str(i)
            break
    if compiler == 'g++' and not os.path.isfile('/usr/local/bin/' + compiler):
        print('Please run\nbrew install gcc\nto install compiler')
        quit(0)

elif system == 'Linux':
    if not os.path.isfile('/usr/bin/' + compiler):
        print('please install gcc before using it')
        quit(0)

elif system == 'Windows':
    print('Please input your compiler dir like: C:\\gcc\\bin\\g++.exe')
    compiler = input()
    if not os.path.isfile(compiler):
        print('Invalid compiler')
        quit(0)
print('System:' + system + ' Compiler:' + compiler)

sourceFile = 'main.cpp'  # 源文件名
vis = []  # 被访问过的文件列表
cntAll = cntWa = 0
if __name__ == '__main__':
    path = os.path.split(os.path.realpath(__file__))[0]  # 获取当前绝对路径
    os.system('%s %s -o a' % (compiler, sourceFile))  # 生成可执行文件
    if not os.path.exists('userOutput'):  # 将程序的输出保存至此，如果不存在则创建
        os.makedirs('userOutput')
    for fileName in os.listdir('testCase'):  # 遍历每一组测试用例
        if fileName[0] == '.':  # 如果是隐藏文件则跳过
            continue
        splitedName = fileName.split('.')
        if splitedName[-1] != 'in' and splitedName[-1] != 'out':  # 不是测试用例则跳过
            continue
        testCaseName = ''
        if splitedName[-1] == 'in':
            testCaseName =  fileName[:-3] # 获取测试文件名，因能力问题，所以文件名中不得包含'\'
        else:
            testCaseName = fileName[:-4]
        if testCaseName not in vis:  # 如果这个测试用例没有用过
            cntAll += 1  # 测试用例总数量加一
            vis.append(testCaseName)  # 标记测试用例
            # 调用程序
            os.system('%s/a <%s/testCase/%s.in >%s/userOutput/%s.out' % (path, path, testCaseName, path, testCaseName))
            stdOut = open(path + '/testCase/' + testCaseName + '.out').read()  # 获取答案的输出
            userOut = open(path + '/userOutput/' + testCaseName + '.out').read()  # 用户程序的输出
            if stdOut != userOut:
                cntWa += 1  # Wrong Answer数量加一
                # 输出错误信息
                print('-----------\n%s:\nExpect:\n%sUser output:\n%s' % (testCaseName, stdOut, userOut))

    if cntWa != 0:
        print('%d/%d Passed' % (cntAll - cntWa, cntAll))
    else:
        print('All correct')
    os.system('rm a')  # 删除可执行文件
    os.system('rm -rf userOutput')  # 删除输出文件

