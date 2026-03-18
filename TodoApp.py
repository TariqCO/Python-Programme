todos = []
todosTime = []

completedTodos = []
completedTodosTime = []


def allTodos(todos,todosTime):
    print("")
    print("-" * 65)
    if len(todos) < 1:
        print("There is no task added yet.")
    else:  
        for i in range(len(todos)):
            if todos[i] in completedTodos:
                print(f"{i + 1}. (Task: {todos[i]} , Time: {todosTime[i]} ✅)")
            else:
                print(f"{i + 1}. (Task: {todos[i]} , Time: {todosTime[i]} ⌛)")
        print("-" * 65)    
        return True    
    print("-" * 65)

def addTodo():
    allTodos(todos,todosTime)
    
    task = input("Enter Task: ")
    time = input("Enter time: ")
    
    todos.append(task)
    todosTime.append(time)
    

def updateTodo():
    isTasksAdded = allTodos(todos,todosTime)
    
    if isTasksAdded:
        taskIndex = int(input("select task to update: "))
        
        if taskIndex > 1 and taskIndex <= len(todos):

            task = input("Enter Task: ")
            time = input("Enter time: ")
            
            todos[taskIndex - 1] = task
            todosTime[taskIndex - 1] = time

            print(f"\nThis task --> (Task: {task} , Time: {time}) updated to the todo.")
        else:
            print("Invalid Task index..")

def deleteTodo():
    isTasksAdded = allTodos(todos,todosTime)
    
    if isTasksAdded:
        taskIndex = int(input("select task to delete: "))
        
        if taskIndex > 1 and taskIndex <= len(todos):
            
            deletedTask = todos.pop(taskIndex - 1)
            deletedTaskTime = todosTime.pop(taskIndex - 1)

            print(f"\nThis task --> (Task: {deletedTask} , Time: {deletedTaskTime})  removed from the todo.")
        else:
            print("Invalid Task index..")


def completeTodo():
    isTasksAdded = allTodos(todos,todosTime)
    if isTasksAdded:
        taskIndex = int(input("select task to move to completed list: "))
    
        completedTask = todos[taskIndex - 1]
        completedTaskTime = todosTime[taskIndex - 1]
    
        completedTodos.append(completedTask)
        completedTodosTime.append(completedTaskTime)
    
        print(f"\nThis task --> (Task: {completedTask} , Time: {completedTaskTime})  moved to completed the todo.")



def allCompletedTodos(completedTodos,completedTodoTime):
    print("")
    print("-" * 65)
    print("======= All Completed Tasks =======\n")
    for i in range(len(completedTodos)):
            print(f"{i + 1}. (Task: {completedTodos[i]} , Time: {completedTodoTime[i]} ✅)")
    print("-" * 65)


def main():
    while True:
        print("")
        print("1.List all Tasks ")
        print("2.Add new Task ")
        print("3.Update the Task ")
        print("4.Delete the Task ")
        print("5.Complete the Task")
        print("6.List completed Tasks")
        print("7.Exit ")

        choice = input("\nChoose what you want to do: ")

        if choice == "1":
            allTodos(todos,todosTime)
        elif choice == "2":
            addTodo()
        elif choice == "3":
            updateTodo()
        elif choice == "4":
            deleteTodo()
        elif choice == "5":
            completeTodo()
        elif choice == "6":
            allCompletedTodos(completedTodos,completedTodosTime)
        elif choice == "7": 
            print("Thank you for using our app. Exiting...")
            break
        else:
            print("Invalid choice selected..!")
            
    
main()
