import regex as re

def meeting_rooms(v):
    v.sort(key = lambda x: x[0]) # sort by staring time
    for i in range(1,len(v)):
        if v[i][0] < v[i-1][1]: # if 2nd starts before 1st finishes
            return False
    return True

def meeting_rooms_2(v):
    v.sort(key=lambda x: x[0])  # sort by staring time
    room_max = 1
    for i in range(1,len(v)):
        max1 = 1
        for j in range(0,i):
            if v[i][0] < v[j][1]: # if 2nd starts before 1st finishes
                max1 += 1
        room_max = max(max1, room_max)
    return room_max

def merge_intervals(v):
    r = list()
    v.sort(key=lambda x: x[0])  # sort by staring time
    i=0
    while i < len(v):
        r.append(v[i])
        i += 1
        while i < len(v) and v[i][0] <= r[-1][1]: # while start[i] <= end[last]
            r[-1][1] = max(r[-1][1], v[i][1])
            i += 1
    return r

def make_not_overlapping(v):
    v.sort(key=lambda x: x[0])  # sort by staring time
    i=1
    while i < len(v):
        if v[i][0] < v[i-1][1]:
            print("removing ", v[i])
            v.pop(i)
        else:
            i += 1
    return v


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #print_hi('PyCharm')
    #print(meeting_rooms([[0,30], [5,10], [15,20]]))
    #print(meeting_rooms([[7, 10], [2, 4], [15, 20]]))
    #print(meeting_rooms_2([[0,30], [5,10], [15,20]]))
    #print(meeting_rooms_2([[7, 10], [2, 4], [15, 20]]))
    #print(merge_intervals([[1,3], [2,6], [8,10], [15,18]]))
    print(make_not_overlapping([[1,2], [2,3], [3,4], [1,3]]))