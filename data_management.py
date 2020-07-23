import os
import sys


def compile_time_lapse():
    print('A')


def delete_all_images():
    confirmation = input('This function deletes all images currently saved. '
                         'Are you sure you want to continue? (y/n)\n')

    if confirmation.lower() != 'y':
        return

    print('Removing files...\n')
    directories = os.listdir('img')

    for local_dir in directories:
        local_imgs = os.listdir('img/' + local_dir)

        print(f'Removing files from img/{local_dir}/ directory...')
        for local_img in local_imgs:
            os.remove('img/' + local_dir + '/' + local_img)

        print(f'Removing img/{local_dir}/ directory...')
        os.rmdir('img/' + local_dir)

    print('\nFiles removed!\n')


commands = {
    1: compile_time_lapse,
    2: delete_all_images
}

if __name__ == "__main__":
    while True:
        print('Welcome to the data management wizard.')
        print('[1] Compile camera feed into time lapse')
        print('[2] Delete existing images')
        print('[Q] Quit')
        response = input('What would you like to do: ')

        try:
            if response.lower() == 'q':
                sys.exit()

            value = int(response)
            commands[value]()
        except (KeyError, ValueError):
            print('The specified command isn\'t valid. Please try again.\n')
