import json
import os

TASKS_FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(TASKS_FILE) or os.path.getsize(TASKS_FILE) == 0:
        return []
    with open(TASKS_FILE, "r") as f:
        return json.load(f)


def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=2)

def list_tasks(tasks):
    if not tasks:
        print("Ei tehtäviä.")
    for i, task in enumerate(tasks):
        status = "✔" if task["done"] else "✘"
        print(f"{i + 1}. [{status}] {task['title']}")

def add_task(tasks, title):
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)
    print(f"Lisätty: {title}")

def delete_task(tasks, index):
    try:
        removed = tasks.pop(index)
        save_tasks(tasks)
        print(f"Poistettu: {removed['title']}")
    except IndexError:
        print("Virheellinen indeksi.")

def mark_done(tasks, index):
    try:
        tasks[index]["done"] = True
        save_tasks(tasks)
        print(f"Merkitty tehdyksi: {tasks[index]['title']}")
    except IndexError:
        print("Virheellinen indeksi.")

def main():
    tasks = load_tasks()
    while True:
        print("\nKirjoita komento ja paina enter: tehtävälistaus, lisää <tehtävän kuvaus>, poista <tehtävän numero>, merkkaa tehdyksi <tehtävän numero>, lopeta")
        cmd = input(">> ").strip()
        if cmd == "tehtävälistaus":
            list_tasks(tasks)
        elif cmd.startswith("lisää "):
            add_task(tasks, cmd[4:])
        elif cmd.startswith("poista "):
            delete_task(tasks, int(cmd[4:]) - 1)
        elif cmd.startswith("merkkaa tehdyksi "):
            mark_done(tasks, int(cmd[5:]) - 1)
        elif cmd == "lopeta":
            break
        else:
            print("Tuntematon komento.")

if __name__ == "__main__":
    main()
