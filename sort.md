## 排序（zpy与python对照）

- [zpy排序程序源码](example/排序.zpy)
- [python排序程序源码](example/sort.py)

#### 一、简单插入排序

1. zpy 简单插入排序

```python
函数 简单插入排序(目标数组):
    对于 索引一 在 范围(0, 长(目标数组) - 1):
        这个 = 目标数组[索引一]
        之后 = 目标数组[索引一 + 1]
        如果 这个 > 之后:
            替换 = 之后
            对于 索引二 在 范围(索引一, -1, -1):
                目标数组[索引二+1] = 目标数组[索引二]
                如果 目标数组[索引二] < 替换:
                    终止
            目标数组[索引二+1] = 替换
            当 索引二 >= 0 与 目标数组[索引二] >= 替换:
                目标数组[索引二+1] = 目标数组[索引二]
                索引二 -= 1
            目标数组[索引二+1] = 替换
    返回 目标数组
```

2. python简单插入排序

```python
def insertSort(target):
    for i in range(0, len(target) - 1):
        this = target[i]
        after = target[i + 1]
        if this > after:
            temp = after
            for j in range(i, -1, -1):
                target[j+1] = target[j]
                if target[j] < temp:
                    break
            target[j+1] = temp
            while j >= 0 and target[j] >= temp:
                target[j+1] = target[j]
                j -= 1
            target[j+1] = temp
    return target
```





#### 二、希尔排序

1. zpy 希尔排序

```python
函数 希尔排序(目标数组):
    步长 = 长(目标数组)
    当 步长 > 0:
        步长 //= 2
        对于 索引一 在 范围(步长, 长(目标数组)):
            替换 = 目标数组[索引一]
            索引二 = 索引一
            当 索引二 >= 步长 与 替换 < 目标数组[索引二-步长]:
                目标数组[索引二] = 目标数组[索引二-步长]
                索引二 -= 步长
            目标数组[索引二] = 替换
    返回 目标数组
```

1. python 希尔排序

```python
def shellSort(target):
    step = len(target)
    while step > 0:
        step //= 2
        for i in range(step, len(target)):
            temp = target[i]
            j = i
            while j >= step and temp < target[j-step]:
                target[j] = target[j-step]
                j -= step
            target[j] = temp
    return target
```



#### 三、冒泡排序

1. zpy 冒泡排序

```python
函数 冒泡排序(目标数组):
    对于 索引一 在 范围(长(目标数组), 0, -1):
        标记 = 错
        对于 索引二 在 范围(0, 索引一 - 1):
            如果 目标数组[索引二] > 目标数组[索引二+1]:
                目标数组[索引二], 目标数组[索引二+1] = 目标数组[索引二+1], 目标数组[索引二]
        如果 标记:
            终止
    返回 目标数组
```

1. python 冒泡排序

```python
def bubbleSort(target):
    for i in range(len(target), 0, -1):
        flag = False
        for j in range(0, i - 1):
            if target[j] > target[j+1]:
                target[j], target[j+1] = target[j+1], target[j]
        if flag:
            break
    return target
```



#### 四、快速排序

1. zpy 快速排序

```python
函数 快速排序(目标数组):
    函数 _快速排序(目标数组, 左指针, 右指针):
        枢轴 = 目标数组[左指针]
        原左指针 = 左指针
        原右指针 = 右指针
        左指针空标记 = 0  # 左指针为空
        当 左指针 != 右指针:
            如果 左指针空标记:
                如果 (目标数组[左指针] >= 枢轴):
                    目标数组[右指针] = 目标数组[左指针]
                    左指针空标记 = 0
                否则:
                    左指针 += 1
            否则:
                如果 (目标数组[右指针] < 枢轴):
                    目标数组[左指针] = 目标数组[右指针]
                    左指针空标记 = 1
                否则:
                    右指针 -= 1
        中指针 = 左指针
        目标数组[中指针] = 枢轴
        如果 原左指针 < 中指针 - 1:
            _快速排序(目标数组, 原左指针, 中指针 - 1)
        如果 中指针+1 < 原右指针:
            _快速排序(目标数组, 中指针+1, 原右指针)
    左指针 = 0
    右指针 = 长(目标数组) - 1
    _快速排序(目标数组, 左指针, 右指针)
    返回 目标数组
```

1. python 快速排序

```python
def fastSort(target):
    def _fastSort(target, left, right):
        pivot = target[left]
        rawLeft = left
        rawRight = right
        leftTag = 0  # left pointer null
        while left != right:
            if leftTag:
                if (target[left] >= pivot):
                    target[right] = target[left]
                    leftTag = 0
                else:
                    left += 1
            else:
                if (target[right] < pivot):
                    target[left] = target[right]
                    leftTag = 1
                else:
                    right -= 1
        mid = left
        target[mid] = pivot
        if rawLeft < mid - 1:
            _fastSort(target, rawLeft, mid - 1)
        if mid+1 < rawRight:
            _fastSort(target, mid+1, rawRight)
    left = 0
    right = len(target) - 1
    _fastSort(target, left, right)
    return target
```



#### 五、选择排序

1. zpy 选择排序

```python
函数 选择排序(目标数组):
    对于 索引一 在 范围(长(目标数组)):
        最小数值 = 索引一
        对于 索引二 在 范围(索引一, 长(目标数组)):
            如果 目标数组[索引二] < 目标数组[最小数值]:
                最小数值 = 索引二
        目标数组[索引一], 目标数组[最小数值] = 目标数组[最小数值], 目标数组[索引一]
    返回 目标数组
```

1. python 选择排序

```python
def selectSort(target):
    for i in range(len(target)):
        lowest = i
        for j in range(i, len(target)):
            if target[j] < target[lowest]:
                lowest = j
        target[i], target[lowest] = target[lowest], target[i]
    return target
```



