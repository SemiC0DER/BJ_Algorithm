while True:
    try:
        N = int(input())
        array = ['-']
        while len(array) < 3 ** N:
            tmp1 = [' '] * (len(array))
            tmp2 = array[:]
            array.extend(tmp1)
            array.extend(tmp2)
        print(''.join(array[:3**N]))
    except:
        break