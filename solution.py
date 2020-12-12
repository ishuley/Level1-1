def solution(data, n):
    if complaint_check(data, n):
        for task in complaint_check(data, n):
            data = remove_task(data, task)
    return data

def remove_task(data, task):
    return [item for item in data if item != task]

def complaint_check(data, n):
    complaint_list = []
    for x in data:
        if data.count(x) > n:
            complaint_list.append(x)
    return complaint_list if complaint_list != [] else False