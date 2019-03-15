from Naked.toolshed.shell import execute_js
import os

def remove_magnetlink(path):
    magnetlinks = []
    with open(path, 'r') as f:
        content = f.read()
        magnetlinks = content.split(',')
        magnetlinks.pop(0)

    with open(path, 'w') as f:
        f.write(''.join(magnetlinks))

    print('Successfully updated list.')


def download_file(magnetlink):
    path = "C:\\Users\\Magnus\\Documents\\plex-torrent-server\\instance\\magnetlinks.txt"
    with open(path, "a+") as f:
        f.write(magnetlink + ',')

    success = execute_js('C:\\Users\\Magnus\\Documents\\plex-torrent-server\\src\\util\\torrentHandler.js')
    remove_magnetlink(path)
