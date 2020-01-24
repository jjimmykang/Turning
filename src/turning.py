import sys
import argparse

def main():
    parser = argparse.ArgumentParser(description='run a turning program.')
    parser.add_argument('file_path', help='path to the turning file.')
    args = parser.parse_args()
    print(args.file_path)

if __name__ == '__main__':
    main()
