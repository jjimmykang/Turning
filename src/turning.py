import sys
import argparse

def main():
    #argument parser
    parser = argparse.ArgumentParser(description='run a turning program.')
    parser.add_argument('file_path', help='path to the turning file.')
    args = parser.parse_args()
    
    #open file
    trng_file = open(args.file_path, 'r')
    trng_prog = trng_file.read() 
    print(trng_prog)
    print(len(trng_prog))

    #variables
    memory = [0]
    current_pointer = 0
    run = True #for the loop
    
    #main loop through characters
    for i in range(len(trng_prog)):
        character = trng_prog[i]
        ''' 
        if character == "]":
            if memory[current_pointer] == "0":
                run = True
            else:
        '''      
        if run:
            if character == "<":
                if current_pointer == 0:
                    memory.insert(0, 0)
                else:
                    current_pointer -= 1
            elif character == ">":
                if current_pointer == len(memory) - 1:
                    memory.insert(len(memory), 0)
                current_pointer += 1
            elif character == "+":
                memory[current_pointer] += 1
            elif character == "-": 
                memory[current_pointer] -= 1
            elif character == ".":
                print("data at index ", current_pointer, ": ", memory[current_pointer])
            elif character == ",":
                input_number = int(input("enter data: "))
                memory[current_pointer] = input_number
            '''
            elif character == "[":
                if memory[current_pointer] == 0:
                    run = False
            '''
    
    print("program finished.")
    print("finished memory: ", memory)

if __name__ == '__main__':
    main()
