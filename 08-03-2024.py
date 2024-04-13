def switch_it_up(number):
    array=["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    if number == 0:
        return array[0]
    if number == 1:
        return array[1]
    if number == 2:
        return array[2]
    if number == 3:
        return array[3]
    if number == 4:
        return array[4]
    if number == 5:
        return array[5]
    if number == 6:
        return array[6]
    if number == 7:
        return array[7]
    if number == 8:
        return array[8]
    if number == 9:
        return array[9]
    



    def sum_array(arr):
        if arr == None or len(arr) < 3:
            return 0
        else:
            return sum(sorted(arr)[1:-1])
    

    def points(games):
        s = []
        for i in games:
            i = i.split(":")
            if int(i[0]) > int(i[1]):
                s.append(3)
            elif int(i[0]) == int(i[1]):
                s.append(1)
            elif int(i[0]) < int(i[1]):
                s.append(0)
        return sum(s)
