def mean(L):
    total = 0
    for x in L:
        total += x #total = total +x
    mean = total / len(L)
    return mean


def median(L):
    L.sort()
    if len(L)%2 != 0:
        median = L[int(len(L)/2)]
    else:
        median = L[(int(len(L)/2)) - 1] +  L[int(len(L)/2)]
        median = median/2
    return median


def mode(L):
    counter = 0
    num = L[0]

    for i in L:
        curr_frequency = L.count(i)
        if(curr_frequency > counter):
            counter = curr_frequency
            num = i
        if len(set(L)) == len(L):
            return 'there is no mode'

    return num


number_list = []

while(True):
    ask = input('enter a number and say "stop" to end: ')

    if ask == 'stop':
        break
    number_list.append(int(ask))

mean = str(mean(number_list))
median = str(median(number_list))
mode = str(mode(number_list))

print('mean: '+ mean + '\n' + 'median: ' + median + '\n' + 'mode: ' + mode)