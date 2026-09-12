import unittest

from src.models import Status
from src.store import TaskStore


class TestTaskStore(unittest.TestCase):
    def test_add_defaults_to_todo(self):
        store = TaskStore()
        task = store.add("Write the report")
        self.assertEqual(task.status, Status.TODO)

    def test_list_returns_all_tasks_by_default(self):
        store = TaskStore()
        store.add("First")
        store.add("Second")
        self.assertEqual(len(store.list()), 2)

    def test_list_filters_by_exact_status(self):
        store = TaskStore()
        first = store.add("First")
        store.add("Second")
        store.mark_done(first.id)

        self.assertEqual([t.title for t in store.list(status=Status.DONE)], ["First"])
        self.assertEqual([t.title for t in store.list(status=Status.TODO)], ["Second"])


if __name__ == "__main__":
    unittest.main()
