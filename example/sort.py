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


def bubbleSort(target):
    for i in range(len(target), 0, -1):
        flag = False
        for j in range(0, i - 1):
            if target[j] > target[j+1]:
                target[j], target[j+1] = target[j+1], target[j]
        if flag:
            break
    return target


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


def selectSort(target):
    for i in range(len(target)):
        lowest = i
        for j in range(i, len(target)):
            if target[j] < target[lowest]:
                lowest = j
        target[i], target[lowest] = target[lowest], target[i]
    return target


if __name__ == '__main__':
    import random
    from copy import deepcopy
    data = [random.randint(0, 100) for _ in range(20)]
    print("raw    data:", data)
    print("python sort:", sorted(deepcopy(data)))
    print("insert sort:", insertSort(deepcopy(data)))
    print("shell  sort:", shellSort(deepcopy(data)))
    print("bubble sort:", bubbleSort(deepcopy(data)))
    print("fast   sort:", fastSort(deepcopy(data)))
    print("select sort:", selectSort(deepcopy(data)))
