from storage import load_tasks, save_tasks


def add_task(task_name):
    tasks = load_tasks()
    tasks.append({"task": task_name, "completed": False})
    save_tasks(tasks)
    print("✅ Task added successfully!")


def view_tasks():
    tasks = load_tasks()

    if not tasks:
        print("No tasks available.")
        return

    for index, task in enumerate(tasks, start=1):
        status = "✔" if task["completed"] else "✘"
        print(f"{index}. {task['task']} [{status}]")


def complete_task(task_number):
    tasks = load_tasks()

    if 0 < task_number <= len(tasks):
        tasks[task_number - 1]["completed"] = True
        save_tasks(tasks)
        print("✅ Task marked as completed!")
    else:
        print("Invalid task number.")


def delete_task(task_number):
    tasks = load_tasks()

    if 0 < task_number <= len(tasks):
        removed = tasks.pop(task_number - 1)
        save_tasks(tasks)
        print(f"🗑 Deleted task: {removed['task']}")
    else:
        print("Invalid task number.")
