from category import CategoryLibrary
from tag import TagLibrary
from task import Task

def run_tests():
    print("Running verification tests...")

    # Initialize Libraries
    cat_lib = CategoryLibrary()
    tag_lib = TagLibrary()

    # 1. Create Category
    print("\n[Test 1] Create Category...")
    cat1 = cat_lib.add_category("Work", "Blue")
    assert cat1.get_name() == "Work"
    assert cat1.get_color() == "Blue"
    print(f"Category created: {cat1.get_name()} ({cat1.get_id()})")

    # 2. Create Tag via Library (Directly)
    print("\n[Test 2] Create Tag directly in Library...")
    tag1 = tag_lib.add_tag("Urgent", "Red", cat1.get_id())
    assert tag1.get_name() == "Urgent"
    assert tag1.get_category_id() == cat1.get_id()
    print(f"Tag created: {tag1.get_name()} ({tag1.get_id()})")

    # 3. Create Task and Assign Tag
    print("\n[Test 3] Task assignment interaction...")
    task = Task("Complete Project")
    
    # Assign same tag "Urgent" - should reuse existing tag from library
    task.add_tag(tag_lib, "Urgent", "Red", cat1.get_id())
    
    assert len(task.tag_list) == 1
    assert task.tag_list[0].get_id() == tag1.get_id()
    print("Tag assigned correctly (reused existing tag).")

    # 4. Assign NEW tag via Task
    print("\n[Test 4] Assign new tag via Task...")
    task.add_tag(tag_lib, "LowProp", "Green", cat1.get_id())
    
    assert len(task.tag_list) == 2
    assert len(tag_lib.get_all_tags()) == 2
    print("New tag created and assigned via Task.")

    # 5. Check Duplication Prevention (Task Level)
    print("\n[Test 5] Check Task level duplication...")
    task.add_tag(tag_lib, "Urgent", "Red", cat1.get_id())
    assert len(task.tag_list) == 2
    print("Correctly prevented duplicate tag assignment on task.")

    # 6. Update Tag in Library
    print("\n[Test 6] Update Tag in Library and check Task...")
    target_tag_id = task.tag_list[0].get_id()
    tag_lib.update_tag_name(target_tag_id, "Very Urgent")
    
    assert task.tag_list[0].get_name() == "Very Urgent"
    print("Tag name updated in library reflected in Task (passed by reference).")

    print("\nALL TESTS PASSED!")

if __name__ == "__main__":
    run_tests()
