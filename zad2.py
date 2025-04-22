def taskimos_manager(taskimoss):

    for taskimos in taskimoss:
        if taskimos["priority"] >= 3:
            yield f"Висок приоритет: {taskimos['name']}"

if __name__ == "__main__":
    taskimoss = [
        {"name": "Имейли", "priority": 2},
        {"name": "Среща", "priority": 4},
        {"name": "Целене с балони", "priority": 5}
    ]
    high_priority_taskimoss = taskimos_manager(taskimoss)
    
    for taskimos in high_priority_taskimoss:
        print(taskimos)
