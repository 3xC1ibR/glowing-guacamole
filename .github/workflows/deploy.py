import argparse

import os
import uuid

def save_endpoint(e):
    print(os.getcwd())
    with open('somefile', 'w') as f:
        f.write(str(e))

def main(env):
    endpoint = uuid.uuid4()
    print(env)
    print(endpoint)
    save_endpoint(endpoint)
    return endpoint

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--env")

    args = parser.parse_args()
    main(**vars(args))