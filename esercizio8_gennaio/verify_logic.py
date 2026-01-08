import manager
import os
import importlib

# Clean up previous test data
if os.path.exists("supermarket_data.json"):
    os.remove("supermarket_data.json")

# Force reload of manager to ensure clean state after file deletion
importlib.reload(manager)

print("🧪 Starting Verification...")

# 1. Test Adding Product
p1 = manager.add_product("Milk", 1.50)
assert p1["name"] == "Milk"
assert len(manager.get_products()) == 1
print("✅ Product Addition Verified")

# 2. Test Adding Task
t1 = manager.add_task("Check expiration", p1["id"])
assert t1["description"] == "Check expiration"
assert t1["product_id"] == p1["id"]
print("✅ Task Addition Verified")

# 3. Test Completion
manager.complete_task(t1["id"])

# Force reload to simulate app restart and check persistence
# Note: since manager loads on import, we need to reload it to fetch from file again
importlib.reload(manager)
tasks = manager.get_tasks()
assert len(tasks) == 1
assert tasks[0]["status"] == "Completed"
print("✅ Persistence & Completion Verified")

# 4. Test Deletion
# We need to get the product ID again because the object p1 might be stale after reload
p1_id = manager.get_products()[0]["id"]
manager.remove_product(p1_id)
assert len(manager.get_products()) == 0
assert len(manager.get_tasks()) == 0
print("✅ Deletion Verified")

print("🎉 All automated checks passed!")
