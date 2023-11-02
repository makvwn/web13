def find_max(arr, max_=None):
    if max_ is None:
        max_ = arr.pop()
    current = arr.pop()
    if current > max_:
        max_ = current
    if arr:
        return find_max(arr, max_)
    return max_


list1=[1,8,9,4,8]
result = find_max(list1)
print(result)
