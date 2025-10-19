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

# päivitetään list_tasks()-funktio
def list_tasks(tasks):
    if not tasks:
        print("Ei tehtäviä.")
        return
    for i, task in enumerate(tasks):
        status = "✔" if task["done"] else "✘"
        deadline = task.get("deadline", "ei asetettu")
        priority = task.get("priority", "ei asetettu")
        print(f"{i + 1}. [{status}] {task['title']} | Deadline: {deadline} | Prioriteetti: {priority}")


# päivitetään add_task()-funktio
def add_task(tasks, title, deadline=None, priority="medium"):
    task = {
        "title": title,
        "done": False,
        "deadline": deadline,
        "priority": priority
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"Lisätty: {title} (Deadline: {deadline}, Prioriteetti: {priority})")


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
# selkeytetty sovelluksen käyttöohjetta
def main():
    tasks = load_tasks()
    print("\n📋 Kirjoita komento ja paina enter. Komennot käytettäväksi:")
    print("  tehtävälistaus                            - Näytä kaikki tehtävät")
    print("  lisää <otsikko> | <deadline> | <prioriteetti>")
    print("                                             - Lisää uusi tehtävä")
    print("                                                 Esim: lisää Kirjoita README | 2025-10-31 | high")
    print("  poista <tehtävän numero>                   - Poista tehtävä")
    print("  merkkaa tehdyksi <tehtävän numero>         - Merkitse tehtävä tehdyksi")
    print("  lopeta                                     - Poistu sovelluksesta")

    while True:
        cmd = input("\n>> ").strip()
        if cmd == "tehtävälistaus":
            list_tasks(tasks)
        elif cmd.startswith("lisää "):
            parts = cmd[4:].split(" | ")
            title = parts[0]
            deadline = parts[1] if len(parts) > 1 else None
            priority = parts[2] if len(parts) > 2 else "medium"
            add_task(tasks, title, deadline, priority)
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
