# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import regex as re

def word2arr(word):
    arr=[0]*26
    for ch in word:
        arr[ord(ch)-ord('a')] = arr[ord(ch)-ord('a')] + 1
    return arr

def group_anagram(words):
    arr1 = ["".join(sorted(word)) for word in words]
    arr2 = sorted(arr1)
    last_word = ''
    last_idx = -1
    # arr4 = [[(last_idx:= idx, last_word:=word)[1] for idx, word in enumerate(arr2) if (word == last_word or last_word == '') and idx > last_idx] for w2 in arr2]
    arr3 = list()
    prev = list()
    for word in arr2:
        if not prev or word == prev[0]:
            prev.append(word)
        else:
            arr3.append(prev)
            prev = [word]
    arr3.append(prev)
    #print("inpt = ", words)
    #print("arr1 = ", arr1)
    #print("arr2 = ", arr2)
    #print("arr3 = ", arr3)
    #print("arr4 = ", arr4)
    return arr3


def string_encode(words):
    l1 = ''.join([''.join([str(len(w)),'#', w]) for w in words])
    return l1

def string_decode(word):
    words = list()
    while word != '':
        parts = word.split('#')
        word_len = int(parts[0])
        len_len = len(parts[0])
        words.append(word[len_len + 1:len_len + 1 + word_len])
        word = word[word_len + len_len + 1:]
    return words

def longestConsecutive(val_arr):
    val_arr.sort()
    longest, l_max = (0,0)
    for idx, x in enumerate(val_arr):
        if idx and x ==  val_arr[idx - 1] + 1:
            longest += 1
            if longest > l_max:
                l_max = longest
        else:
            longest = 0
    return l_max+1

def productExceptSelf_with_div(val_arr):
    mult = 1
    for x in val_arr:
        mult *= x
    prod = list()
    for x in val_arr:
        prod.append(mult / x)
    return prod

def productExceptSelf_no_div(nums):
    print(nums)
    length = len(nums)
    answer = [0] * length
    answer[0] = 1
    for i in range(1, length):
        answer[i] = nums[i - 1] * answer[i - 1]
    print(answer)
    R = 1
    for i in reversed(range(length)):
        answer[i] = answer[i] * R
        R *= nums[i]
    return answer

from contextlib import suppress
def TwoSum(arr, target):
    for i in range(1, len(arr)):
        diff = target - arr[i]
        with suppress(ValueError):
            pos = arr[0:i].index(diff)
            return [pos, i]
    return False

def topKFrequent(arr, n):
    dic = { k:0 for k in arr}
    # make histogram
    for x in arr:
        dic[x] += 1
    # sort dict. by its values
    dic2 = dict(sorted(dic.items(), key=lambda item: item[1], reverse=True))
    dic_keys = list(dic2.keys())
    l = [dic_keys[x] for x in range(0, n)]
    return l

def is9Valid(v):
    s = set()
    for c in v:
        if (c < '1' or c > '9') and c != '.':
            return 1
        if c in s and c != '.' :
            return 1
        s.add(c)
    return 0

def isValidSudoku(board):
    if (len(board) != 9 or len(board[0]) != 9):
        return False
    err = 0
    for i in range (0,9):
        err += is9Valid(board[i])
    for i in range(0, 9):
        err += is9Valid([board[c][i] for c in range(0,9)])
    for i1 in range(0, 9, 3):
        for i2 in range(0, 9, 3):
            err += is9Valid([board[i1+i3][i2+i4] for i3 in range(0, 3) for i4 in range(0, 3)])
    return err == 0

def print_hi(name):
    name = re.sub('arm', 'ARM', name)
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    #print(group_anagram(["eat","tea","tan","ate","nat","bat"]))
    #print(encoded_str:=string_encode(['hello#123456789', 'you']))
    #print(string_decode(encoded_str))
    #print(longestConsecutive([100,4,200,1,3,2]))
    #print(productExceptSelf_with_div([1, 2, 3, 4]))
    #print(productExceptSelf_no_div([1,2,3,4]))
    #print(TwoSum([2,7,11,15], 13))
    #print(topKFrequent([1, 1, 1, 2, 2, 3, 3, 3, 3, 3], 2))
    x1 = [["5", "3", ".", ".", "7", ".", ".", ".", "."]
        , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
        , [".", "9", "8", ".", ".", ".", ".", "6", "."]
        , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
        , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
        , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
        , [".", "6", ".", ".", ".", ".", "2", "8", "."]
        , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
        , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    x2 = [["8","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]
    print(isValidSudoku(x1))
    print(isValidSudoku(x2))