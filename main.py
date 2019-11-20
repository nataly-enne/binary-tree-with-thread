from threading import Thread
from time import sleep, time

from node import Node, insert, search


PATHNAME = 'dictionary_partial.txt'


def insert_data(root, pathname):
    start_time = time()

    with open(pathname) as fp:
        line = fp.readline()
        while line:
            word = line.strip()
            insert(root, Node(word))
            # sleep(0.1)
            line = fp.readline()

    end_time = time()
    print(f"--- {(end_time - start_time)} seconds ---")


def main(root):
    thread = Thread(target=insert_data, args=(root, PATHNAME))
    thread.start()


def menu(root):
    while True:
        try:
            value = str(input(""))
            if not search(root, value) is None:
                print("find.")
            else:
                print("not found!")
        except KeyboardInterrupt:
            break


if __name__ == '__main__':
    root = Node('__init__')
    main(root)
    menu(root)
