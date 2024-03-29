# Module and Package in Python

本文简单总结一下在 Python 中调用包和模块时的逻辑，以便处理调包和打包等问题。

## Python 的模块和包

在 Python 中，Module（模块）和Package（包）用来组织和管理代码。模块是一个包含Python代码的文件，可以包含函数、类和变量等；包是一个包含模块和子包的文件夹，它为了更好地组织和管理相关的模块而存在。二者均可用 `import` 语句导入。

包中通常包含一个特殊的 `__init__.py` 文件，用于标识该文件夹为一个包。导入包时，Python会执行 `__init__.py` 文件。

## Python 模块搜索路径

当导入模块的时候，Python 解释器会在下面的路径里搜索:

> - 内置模块
> 
> - 包含输入脚本的目录(或者未指定文件时的当前目录)
> 
> - PYTHONPATH（一个包含目录列表，它和shell变量有一样的语法）
>
> - pip安装的第三方库
>

上面所有的搜索路径会初始化在 `sys.path` 中，可以导入 `sys` 包后打印查看。

## 调用自己的 py 文件

1. 方式一

如果被调用文件和调用文件在同级目录，可以通过调用其文件名来直接调用。

2. 方式二

如果被调用文件在同级目录的子目录中，可以用`.`来索引，但注意被调用文件不能包含这种方式的调用。

> 这里涉及到当前工作目录的概念。在当前工作目录调用文件，被调用文件去调用其他文件时也是从当前工作目录开始索引的，如此索引起点就不是被调用文件的目录，从而出错。

当然也可以和 Java 项目开发一样，设计一个顶级目录名，所有包和模块的调用都从这个顶级目录名开始。

3. 方式三

最彻底的解决方式，只要将自己写的包添加在 `sys.path` 中就行了。

可以通过 `sys.path.append('path/to/directory')` 来添加。

## Reference

[python模块/包调用总结(包含跨目录)](https://blog.csdn.net/MaXumr/article/details/109640529)

