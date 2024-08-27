
import functions
import time

now = time.strftime("%A %d, %Y %H:%M:%S")
print (now)

while True:

    user_action = input("Type add, show, edit, complete, exit: ")
    user_action = user_action.strip()


    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = functions.get_todos("todos.txt")

        todos.append(todo + "\n")

        functions.write_todos(todos,"todos.txt", )

    elif user_action.startswith("show"):

        todos = functions.get_todos("todos.txt")

        for index, item in enumerate(todos):
            item= item.strip("\n")
            row = f"{index +1}- {item}"
            print (row)

    elif user_action.startswith("edit"):
        number = int(user_action[5:])
        print(number)

        number = number -1

        todos = functions.get_todos("todos.txt")

        new_todo =input("Edit a new todo: ")
        todos[number] = new_todo +"\n"

        functions.write_todos(todos,"todos.txt")



    elif user_action.startswith("complete"):

        try:
            number = int(user_action[9:])

            todos = functions.get_todos("todos.txt")
            index = number -1
            todo_to_remove = todos[index].strip("\n")
            todos.pop(index)

            functions.write_todos(todos,"todos.txt")

            message  = f"todo {todo_to_remove} has been deleted."
            print (message)

        except IndexError:
            print("Your input is not valid")
            continue

    elif user_action.startswith("exit"):
        break

    else:
        print(" Your Command is not valid")



