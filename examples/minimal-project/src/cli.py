import argparse

from .models import Status
from .store import TaskStore


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="tasks")
    subparsers = parser.add_subparsers(dest="command", required=True)

    add_parser = subparsers.add_parser("add", help="Create a task")
    add_parser.add_argument("title")

    list_parser = subparsers.add_parser("list", help="List tasks")
    list_parser.add_argument("--status", choices=[s.value for s in Status], default=None)

    done_parser = subparsers.add_parser("done", help="Mark a task as done")
    done_parser.add_argument("id", type=int)

    return parser


def main(argv: list[str] | None = None) -> None:
    parser = build_parser()
    args = parser.parse_args(argv)
    store = TaskStore()

    if args.command == "add":
        task = store.add(args.title)
        print(f"Created task {task.id}: {task.title} [{task.status.value}]")
    elif args.command == "list":
        status = Status(args.status) if args.status else None
        for task in store.list(status=status):
            print(f"{task.id}: {task.title} [{task.status.value}]")
    elif args.command == "done":
        task = store.mark_done(args.id)
        print(f"Marked task {task.id} as done")


if __name__ == "__main__":
    main()
