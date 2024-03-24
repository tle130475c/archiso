# author: Le Anh Tai
# email: leanhtai01@gmail.com
# GitHub: https://github.com/leanhtai01
import os
import subprocess


def build_archiso():
    subprocess.run(
        ['sudo', 'pacman', '-Syu', '--needed', '--noconfirm', 'archiso']
    )
    subprocess.run(['sudo', 'mkarchiso', '-v', '../releng'])


if __name__ == '__main__':
    username = subprocess.check_output('whoami', shell=True).decode().strip()

    # clean old stuffs
    if os.path.isdir('work'):
        subprocess.run(['sudo', 'rm', '-r', 'work'])
    if os.path.isdir('out'):
        subprocess.run(['sudo', 'rm', '-r', 'out'])

    build_archiso()

    # delete unnecessary work directory
    subprocess.run([
        'sudo', 'rm', '-r', 'work'
    ])

    # change ISO's owner to user
    subprocess.run([
        'sudo', 'chown', '-R', f'{username}:{username}', 'out'
    ])
