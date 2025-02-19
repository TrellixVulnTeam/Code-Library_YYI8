import requests
import hashlib
import sys


def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + str(query_char)
    res = requests.get(url)
    print(res)
    if res.status != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}, check the api and try again.')
    return res


def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0


def pwned_api_check(password):
    sha1password = (hashlib.sha1(password.encode('utf-8')).digest().upper())
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)
    return get_password_leaks_count(response, tail)


def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f'{password} was found {count} times, you should change your password.')
        else:
            print(f'{password} was not found.  You are good!')
    return 'done'


if __name__ == '__main__':
    main(sys.argv[1:])
