def check_ascending(array):
    status = True
    if not array:
        status = False
    elif len(array)==1:
        status = True
    else:
        for i in range(1,len(array)):
            if (array[i-1] > array [i]):
                status = False
    return status