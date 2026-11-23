# Name_Program : Todo_lixy
# version : 1.0v

import json

tasks = []

def load_tasks():
    try:
        with open("tasks.json", "r", encoding="utf-8") as file:
            return json.load(file)

    except FileNotFoundError:
        return []

def list_show(tasks):
    if not tasks:
        print("No tasks available.")
        return

    for task in tasks:
        status = "[x]" if task["completed"] else "[ ]"

        print(
            f'{task["id"]}- {status}.{task["task"]} '
        )

def save_tasks(tasks):
    with open("tasks.json", "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=4, ensure_ascii=False)

def task_add(tasks):
    while True :
        task = input("Enter the task (Enter `00` for exit) : ")
        if task == "00" :
            print("Bye")
            break
        else :
            new_task = {
                "id" : max([task["id"] for task in tasks], default=0) + 1,
                "task" : task,
                "completed" : False
            }
            #tasks.append({"task" : f"{task}" , "completed" : False})
            tasks.append(new_task)
            save_tasks(tasks)
            

def completed(tasks):
    task = int(input("Enter the number task"))
    if task>=1 and task <= len(tasks) :
        task-=1
        tasks[task]["completed"] = not tasks[task]["completed"]
        save_tasks(tasks)
    else :
        print("the Task is not found !!!")

def remove_task(tasks) :
    task = int(input("Enter Number task that you want remove it : "))
    if task >= 1 and task <=len(tasks):
        
        tasks.pop(task - 1)
        save_tasks(tasks)
        list_show(tasks)
    else : 
        print("This task is not found !")


def choose():
    
    print("---------LIST CHOOSE---------")
    print("1- For SHOW LIST")
    print("2- For ADD TASK")
    print("3- For Remove TASK")
    print("4- For Completed or not Competed Tasks")
    print("99- Exit")
    user = int(input("Enter Number : "))
    return user
    


def main():
    tasks = load_tasks()
    while True :
        try :
            check_choose = choose()
            match check_choose :
                case 1:
                    list_show(tasks)
                case 2:
                    task_add(tasks)
                case 3:
                    remove_task(tasks)
                case 4:
                    completed(tasks)
                case 99:
                    print("GoodBye")
                    break
                case _ :
                    print("Please Enter valid choose ")
        except ValueError :
            print("Please Enter valid choose !!!")
        
main()