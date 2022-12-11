import argparse
import subprocess


HEADER_SIZE = 28
MIN_MTU = 1
MAX_MTU = 2000

parser = argparse.ArgumentParser(description='Script finds MTU for given host')
parser.add_argument('-c', default=1, type=int, action='store', help='Retry counts for one fixed size')
parser.add_argument('host', type=str, action='store', help='Host')

def find_mtu(host: str, retry_count: int):
    l = MIN_MTU
    r = MAX_MTU
    while r > l + 1:
        mid = (l + r) // 2

        print(host, mid)

        res = subprocess.run(
            ['ping', host, '-s', str(mid), '-c', str(retry_count), '-M', 'do'],
            stdin=subprocess.DEVNULL,
            stdout=subprocess.DEVNULL,
        )

        print(res)

        if res.returncode == 0:
            l = mid
        else:
            r = mid

    return l + HEADER_SIZE


def main():
    params = parser.parse_args()
    print(find_mtu(params.host, params.c))

if __name__=='__main__':
    main()
