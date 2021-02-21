import sys
import shutil


def compile_time_lapse():
    print('A')


# This function is used to maintenance purposes only - it removes all files present in any 
# of the storage folders
def delete_all_images():
    response = input('This function deletes all images currently saved. ' 
                     'Are you sure you want to continue? (y/n)')
    
    if (response != 'y'):
        return
    
    print('Removing files...')    
    shutil.rmtree(save_folder)


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
                
            # Get the response and cast as an int
            value = int(response)
            
            # Invoke the function from the command
            commands[value]()
            
        except (KeyError, ValueError):
            # Print an error if the select
            print('The specified command isn\'t valid. Please try again.\n')
