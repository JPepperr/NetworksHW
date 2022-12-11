import argparse
import subprocess


HEADER_SIZE = 28
MIN_MTU = 0
MAX_MTU = 2000

parser = argparse.ArgumentParser(description='Script finds MTU for given host')
parser.add_argument('-c', default=1, type=int, action='store', help='Retry counts for one fixed size')
parser.add_argument('host', type=str, action='store', help='Host')

def make_ping(host, size, retry_count_str):
    proc = subprocess.run(
        ['ping', host, '-s', str(size), '-c', retry_count_str, '-M', 'do'],
        capture_output=True
    )
    return proc.returncode, proc.stdout, proc.stderr

def find_mtu(host: str, retry_count: int):
    retry_count = str(retry_count)
    l = MIN_MTU
    r = MAX_MTU
    while r > l + 1:
        mid = (l + r) // 2
        if make_ping(host, mid, retry_count)[0] == 0:
            l = mid
        else:
            r = mid

    return l + HEADER_SIZE


def main():
    params = parser.parse_args()
    res = make_ping(params.host, 0, str(params.c))
    if res[0] != 0:
        print(f'Request failed with minimal size {HEADER_SIZE}.\nstdout:{res[1]}\nstderr:{res[2]}')
    else:
        print(find_mtu(params.host, params.c))

if __name__=='__main__':
    main()
