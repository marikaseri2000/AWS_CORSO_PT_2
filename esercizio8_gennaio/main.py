import manager
import sys

def print_menu():
    print("\n--- 🛒 Supermarket Manager ---")
    print("1. Add Product")
    print("2. View Products")
    print("3. Delete Product")
    print("4. Add Task to Product")
    print("5. View Tasks")
    print("6. Complete Task")
    print("7. Exit")
    print("------------------------------")

def main():
    while True:
        print_menu()
        choice = input("Select an option: ")

        try:
            if choice == "1":
                name = input("Enter product name: ")
                price = float(input("Enter product price: "))
                prod = manager.add_product(name, price)
                print(f"✅ Product '{prod['name']}' added with ID {prod['id']}")

            elif choice == "2":
                products = manager.get_products()
                if not products:
                    print("📭 No products found.")
                else:
                    print("\n📦 Products:")
                    for p in products:
                        print(f"  [{p['id']}] {p['name']} - ${p['price']:.2f}")

            elif choice == "3":
                pid = int(input("Enter Product ID to delete: "))
                manager.remove_product(pid)
                print(f"🗑️ Product {pid} and its tasks deleted.")

            elif choice == "4":
                pid = int(input("Enter Product ID for the task: "))
                desc = input("Enter task description: ")
                try:
                    task = manager.add_task(desc, pid)
                    print(f"✅ Task added to Product {pid}: {task['description']}")
                except ValueError as e:
                    print(f"❌ Error: {e}")

            elif choice == "5":
                pid_input = input("Enter Product ID to filter (or press Enter for all): ")
                pid = int(pid_input) if pid_input else None
                tasks = manager.get_tasks(pid)
                if not tasks:
                    print("📭 No tasks found.")
                else:
                     print("\n📋 Tasks:")
                     for t in tasks:
                         status_icon = "✅" if t['status'] == "Completed" else "⏳"
                         print(f"  [{t['id']}] {status_icon} {t['description']} (Prod ID: {t['product_id']})")

            elif choice == "6":
                tid = int(input("Enter Task ID to complete: "))
                try:
                    manager.complete_task(tid)
                    print(f"🎉 Task {tid} marked as completed!")
                except ValueError as e:
                    print(f"❌ Error: {e}")

            elif choice == "7":
                print("👋 Goodbye!")
                break
            
            else:
                print("❌ Invalid option, please try again.")

        except ValueError:
            print("❌ Invalid input. Please enter numbers for IDs/Prices.")
        except Exception as e:
            print(f"❌ Unexpected Error: {e}")

if __name__ == "__main__":
    main()