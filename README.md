# LocalJudge

针对竞赛程序的本地测评

# 文件结构

```
dir
 ├─ localJudge.py
 ├─ main.cpp
 └─ testCase
     ├─ *.in
     └─ *.out
```
     
# 使用方法

将待评测的程序源文件和python程序放在同一目录下，将测试用例放至testCase文件夹下，执行python程序即可。

# 注意事项

在运行python程序前请确保编译参数（编译器名称）和源文件名正确。

```bash
gcc main.c -o a # 编译C语言
g++ main.cpp -o a # 编译C++
```

测试用例请保持对应的输入输出的文件名完全一致，且不包含'.'和'\'，例如：
```bash
test1.in test1.out # 合法，除后缀外完全一致且不包含'.'和'\'
test1.in test.out # 不合法，文件名不一致
test.1.in test.1.out # 不合法，包含'.'
test\1.in test\1.out # 不合法，包含'\'
```

# 原理

原理为利用Linux的输入输出重定向将*.in文件作为二进制程序的输入，将程序的输出重定向至某个文件，随后将这个文件与对应的*.out文件进行文本比对，比对成功即通过测试。
