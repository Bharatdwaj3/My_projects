dict = {"Program": "A non running process",
        "Computer": "A device for doing calculatiions",
        "Input": "Commmands given to the computer",
        "Output": "Results by the computer",
        "Process": "A non runing program",
        "Threads": "The smalest unit of execution",
        "Operating System": "A program that procee interface b/w user and machine",
        "Processor": "A device for processing commands",
        "Cathe": "Most recent commands",
        "RAM": "Temporary Memory",
        "ROM": "Secondary Memory",
        }
key: str = input('Enter the word to be searched : ')
if key not in dict:
    print('Not avaliable in Dictonary ')
else:

    print(key, " : ", dict[key])