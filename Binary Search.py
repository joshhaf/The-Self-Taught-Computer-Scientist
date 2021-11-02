#This is a code example of the use of a binary search in Python
org_list = ['apple', 'banana', 'coconut', 'grape', 'kiwi', 'lemon', 'orange']

def binary_search(a_list, target):
    first = 0
    last = len(a_list) - 1
    while last >= first:
        mid = (first + last) // 2
        if a_list[mid] == target:
            return True
        else:
            if target < a_list[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return False


print(binary_search(org_list, 'pineapple'))