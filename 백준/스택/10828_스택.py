stack_list = [];
cmd = [];

def init():
    line = int(input())
    for i in range(0, line, 1):
        cmd.append(list(input().split()));

def run():
     for i in range(0, len(cmd), 1):
        command = cmd[i][0];

        if(command == 'push'):
            push(cmd[i][1]);

        elif(command == 'top'):
            top();

        elif(command == 'size'):
            print(size());

        elif(command == 'empty'):
            empty();

        elif(command == 'pop'):
            pop();

def push(X):
    stack_list.append(int(X));

def pop():
    if(check_empty()):
        print(-1)
    else:
        print(stack_list.pop());

def size():
    return len(stack_list);

def empty():
    if(check_empty()):
        print(1)
    else:
        print(0)

def check_empty():
    if(size() == 0):
        return True;
    else:
        return False;

def top():
    if(check_empty()):
        print(-1)
    else:
        print(stack_list[size()-1]);

init();
run();
