# zpy-script

#### 一、介绍
中文编程zpy-script，解析中文的Python关键字，[在线尝试 - Zpy Online IDE](https://service-jbqv5vwm-1302874749.gz.apigw.tencentcs.com/release/)

#### 二、基本功能

- 执行中文zpy脚本文件
- 完全兼容python语法，完全兼容python官方库与第三方库
- 将中文编程的zpy后缀文件，转化为py文件后执行
- 将py文件转化为中文编程zpy文件
- TODO 完善pyTozpy
- TDDO 添加对全角符号的支持

#### 三、软件架构
- 基于Python3实现
- 纯原生实现，未使用第三方库
- 支持中英关键字混合编程，完全兼容python3
- 轻量级177行代码
- 大小仅4KB


#### 四、安装教程

1.  确保本地已安装[Python3](https://www.python.org/downloads/)，且终端有python3环境

> 本教程基于Linux/Unix/MacOS环境
>
> Windows环境请视情况调整

1.  拉取仓库代码

``` shell
git clone https://gitee.com/louisyoungx/zpy-script.git
```

3. 进入文件夹

```shell
cd zpy-script
```

#### 五、使用说明

1.  给予zpy权限

```shell
# 确保当前在zpy-script目录下
sudo chmod 777 zpy
```

2. 运行demo

```shell
# 确保当前在zpy-script目录下
sudo ./zpy example/pokemon.zpy
```

3. 如果运行成功，你将会在example目录下找到转化后的pokemon.py文件

```shell
简单顺序查找 开始计时
  id : 448
  name :
    english : Lucario
    japanese : ルカリオ
    chinese : 路卡利欧
    french : Lucario
  type : ['Fighting', 'Steel']
  base :
    HP : 70
    Attack : 110
    Defense : 70
    Sp. Attack : 115
    Sp. Defense : 70
    Speed : 90
简单顺序查找 完成  0.0001308918s
```

4. 全局执行zpy命令

```shell
sudo chmod 777 zpy
sudo mv zpy /usr/local/bin

zpy example/pokemon.zpy # 此时可以在任意目录执行zpy命令，不用加./
```

1. 卸载zpy命令

```shell
sudo rm /usr/local/bin/zpy
```



#### 六、zpy与python3的语法对应关系

```python
关键字 = {
    "类": "class",
    "函数": "def",
    "删除": "del",
    "跳过": "pass",
    "终止": "break",
    "继续": "continue",
    "返回": "return",
    "从": "from",
    "抛出": "raise",
    "生成": "yield",
    "导入": "import",
    "全局": "global",
    "非局部": "nonlocal",
    "断言": "assert",
    "如果": "if",
    "或如": "elif",
    "否则": "else",
    "当": "while",
    "对于": "for",
    "在": "in",
    "尝试": "try",
    "捕获": "except",
    "最后": "finally",
    "作为": "as",
    "随着": "with",
    "匿名": "lambda",
    "或": "or",
    "与": "and",
    "不": "not",
    "在": "in",
    "空": "None",
    "对": "True",
    "错": "False",
  	"自己": "self",
    "类": "class",
    "异步": "async",
    "等待": "await"
}

内部方法 = {
    "符": "chr",
    "二进制": "bin",
    "串": "str",
    "八进制": "oct",
    "符值": "ord",
    "十六进制": "hex",
    "元组": "tuple",
    "长": "len",
    "集合": "set",
    "全为真": "all",
    "字典": "dict",
    "任一为真": "any",
    "列表": "list",
    "迭代": "iter",
    "冻结集合": "frozenset",
    "超类": "super",
    "切片": "slice",
    "乘方": "pow",
    "字节": "bytes",
    "全局字典": "globals",
    "字节数组": "bytearray",
    "局部字典": "locals",
    "属性": "property",
    "对象": "object",
    "删属性": "delattr",
    "变量字典": "vars",
    "取属性": "getattr",
    "可调用": "callable",
    "有属性": "hasattr",
    "内存视图": "memoryview",
    "设属性": "setattr",
    "哈希": "hash",
    "复数": "complex",
    "商余": "divmod",
    "整数": "int",
    "评估": "eval",
    "浮点数": "float",
    "范围": "range",
    "布尔": "bool",
    "表示": "repr",
    "输入": "input",
    "打包": "zip",
    "打印": "print",
    "打开": "open",
    "执行": "exec",
    "排序": "sorted",
    "编译": "compile",
    "反转": "reversed",
    "映射": "map",
    "和": "sum",
    "是实例": "isinstance",
    "枚举": "enumerate",
    "最大值": "max",
    "断点": "breakpoint",
    "最小值": "min",
    "是子类": "issubclass",
    "绝对值": "abs",
    "下一个": "next",
    "类型": "type",
    "筛选": "filter",
    "格式化": "format",
    "静态方法": "staticmethod",
    "舍入": "round",
    "类方法": "classmethod",
    "退出": "exit",
    "帮助": "help",
    "ascii": "ascii",
    "id": "id",
    "dir": "dir"
}

```



#### 七、示例代码

更多例子：[排序（zpy与python对照）](sort.md)

```python
导入 os
导入 json
导入 time
从 copy 导入 deepcopy


函数 初始化():

    随着 打开("./example/pokemon.json") 作为 宝可梦:
        宝可梦数据 = 宝可梦.read()
        数据集 = json.loads(宝可梦数据)

    数据集.sort(key=匿名 此项: 此项["id"])

    返回 数据集


数据集 = 初始化()


函数 前样式_1(单词):
    返回 f'\033[31m{单词}\033[0m'


函数 前样式_2(单词):
    返回 f'\033[32m{单词}\033[0m'


函数 前样式_3(单词):
    返回 f'\033[33m{单词}\033[0m'


函数 前样式_4(单词):
    返回 f'\033[34m{单词}\033[0m'


函数 前样式_6(单词):
    返回 f'\033[36m{单词}\033[0m'


函数 后样式_1(单词):
    返回 f'\033[41m{单词}\033[0m'


函数 混合样式(单词):
    返回 f'\033[5;34;46m{单词}\033[0m'


类 计时(对象):
    名字 = 空
    开始时间 = 空
    结束时间 = 空

    函数 __在it__(自己, 名字="计时"):
        自己.名字 = 名字
        自己.开始()

    函数 开始(自己):
        自己.打印开始()
        自己.开始时间 = time.time()

    函数 结束(自己):
        自己.使用时间 = time.time() - 自己.开始时间
        自己.打印结束()
        自己 = 空

    函数 打印开始(自己):
        打印(前样式_4("{} 开始计时").格式化(自己.名字))

    函数 打印结束(自己):

        打印(前样式_6('{} 完成 ').格式化(自己.名字) +
              前样式_2(' {:.10f}s'.格式化(自己.使用时间)))


函数 分割线(名字):
    打印(f'\n{混合样式(f"===== {名字} =====")}\n')


函数 显示(目标字典, 样式列表=[], 深度=0):

    对于 关键字 在 目标字典:
        如果 样式列表 == [] 或 关键字 在 样式列表 或 深度 != 0:
            如果 类型(目标字典[关键字]) == 字典:
                打印(
                    f'{" "*2*深度}{后样式_1(" ")} {前样式_4(关键字)} {前样式_1(":")}')
                显示(目标字典[关键字], 样式列表, 深度 + 1)
            否则:
                打印(
                    f'{" "*2*深度}{后样式_1(" ")} {前样式_4(关键字)} {前样式_1(":")} {前样式_3(目标字典[关键字])}')
    返回


函数 未找到(单词="没有找到"):
    打印("")
    打印(f'{后样式_1(" ")} {前样式_4(单词)}')
    打印("")


分割线("简单顺序查找")


函数 简单顺序查找(目标):
    查找计时 = 计时("简单顺序查找")
    对于 此项 在 数据集:
        如果 目标 == 此项["name"]["chinese"]:
            显示(此项)
            查找计时.结束()
            返回 此项
    否则:
        查找计时.结束()
        未找到()
        返回 错


简单顺序查找("路卡利欧")

```

