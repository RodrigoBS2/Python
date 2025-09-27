from multiprocessing import Process

# Usage of Process class:

def print_function(continent = 'Asia'):
    print('The name of continent is : ', continent)

if __name__ == "__main__":  # confirms that the code is under main function
    names = ['America', 'Europe', 'Africa'] # List names
    List_proc = []  # List to store the process
    proc = Process(target=print_function)  # instantiating without any argument
    List_proc.append(proc)
    proc.start()

    # instantiating process with arguments
    for name in names:
        # print(name)
        proc = Process(target=print_function, args=(name,)) # Instantiating with argument
        List_proc.append(proc)
        proc.start()

    # complete the processes
    for proc in List_proc:
        proc.join()













