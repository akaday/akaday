from todo_usecase import ToDoUseCase
from todo_repository import InMemoryToDoRepository

if __name__ == "__main__":
    repository = InMemoryToDoRepository()
    use_case = ToDoUseCase(repository)

    use_case.add_todo("Learn Clean Architecture")
    use_case.add_todo("Write a Blog Post")

    for todo in use_case.get_todos():
        print(f"{todo.id}: {todo.title} - Completed: {todo.completed}")
