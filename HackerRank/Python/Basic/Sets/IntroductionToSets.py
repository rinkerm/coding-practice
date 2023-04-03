def average(array):
    distinct = set(array)
    avg = sum(distinct)/len(distinct)
    return avg

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
