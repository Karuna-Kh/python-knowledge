from os.path import getsize
from bisect import bisect


def convert(bytes):
    # size = [1, 1e+3, 1e+6, 1e+9, 1e+12]   ##GB
    size = [1, 2**10, 2**20, 2**30, 2**40]  ##Gib
    unit = ['B', 'K', 'M', 'G', 'T']
    idx = bisect(size, bytes) - 1
    return f'{bytes/size[idx]:.0f}{unit[idx]}'


file = 'D:\Program\Driver\driver-pack-solution-17.6.6 Offline.iso'
print(convert(getsize(file)), file)