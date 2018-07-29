#!/bin/python3
import os

compiler = 'g++'  # 编译器名
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
        testCaseName = fileName.split('.')[0]  # 获取测试文件名，因能力问题，所以文件名中不得包含'.'和'\'
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
        print('Wrong Answer %d/%d' % (cntAll - cntWa, cntAll))
    else:
        print('Accept')
    os.system('rm a')  # 删除可执行文件
