'''import os

def m(path):
    print(f"\nContents of {path}:")
    print("\nDirectories only:")
    for item in os.listdir(path):
        if os.path.isdir(os.path.join(path, item)):
            print(item)
    print("\nFiles only:")
    for item in os.listdir(path):
        if os.path.isfile(os.path.join(path, item)):
            print(item)
    print("\nAll contents:")
    for item in os.listdir(path):
        print(item)

path = "."  
m(path)'''


'''import os

def a(path):
    print(f"\nChecking access for {path}:")
    exists = os.path.exists(path)
    print(f"Exists: {exists}")
    
    if exists:
        readable = os.access(path, os.R_OK)
        print(f"Readable: {readable}")
        writable = os.access(path, os.W_OK)
        print(f"Writable: {writable}")
        executable = os.access(path, os.X_OK)
        print(f"Executable: {executable}")

path = "test.txt"
a(path)'''


'''import os

def a(path):
    exists = os.path.exists(path)
    print(f"Path exists: {exists}")
    
    if exists:
        abs_path = os.path.abspath(path)
        directory = os.path.dirname(abs_path)
        filename = os.path.basename(abs_path)
        
        print(f"Full path: {abs_path}")
        print(f"Directory: {directory}")
        print(f"Filename: {filename}")

path = "test.txt"
a(path)'''


'''def a(filename):
    try:
        with open(filename, 'r') as file:
            line_count = sum(1 for line in file)
        print(f"Number of lines in {filename}: {line_count}")
    except FileNotFoundError:
        print(f"Error: File {filename} not found")

a("test.txt")'''

'''def a(filename, items):
    try:
        with open(filename, 'w') as file:
            for item in items:
                file.write(str(item) + '\n')
        print(f"List written to {filename} successfully")
    except Exception as e:
        print(f"Error writing to file: {e}")

my_list = [1, 2, 3, "hello", 5]
a("output.txt", my_list)'''


'''import string

def alphabet():
    for letter in string.ascii_uppercase:
        filename = f"{letter}.txt"
        try:
            with open(filename, 'w') as file:
                file.write(f"This is file {letter}")
            print(f"Created {filename}")
        except Exception as e:
            print(f"Error creating {filename}: {e}")

alphabet()'''

'''def copy_file(source, destination):
    try:
        with open(source, 'r') as source_file:
            with open(destination, 'w') as dest_file:
                dest_file.write(source_file.read())
        print(f"Contents copied from {source} to {destination}")
    except FileNotFoundError:
        print(f"Error: Source file {source} not found")
    except Exception as e:
        print(f"Error during copy: {e}")
copy_file("source.txt", "destination.txt")'''

'''
import os

def delete_file(path):
    print(f"\nAttempting to delete {path}:")
    if not os.path.exists(path):
        print("Error: Path does not exist")
        return
    if not os.path.isfile(path):
        print("Error: Path is not a file")
        return

    if not os.access(path, os.W_OK):
        print("Error: No write permission to delete file")
        return
    try:
        os.remove(path)
        print(f"Successfully deleted {path}")
    except Exception as e:
        print(f"Error deleting file: {e}")

delete_file("test.txt")'''


