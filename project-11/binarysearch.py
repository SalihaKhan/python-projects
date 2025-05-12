def binary_search(arr, target):
    """
    Perform binary search on a sorted array.
    
    Parameters:
        arr (list): Sorted list to search
        target: Element to search for
    
    Returns:
        int: Index of target if found, -1 otherwise
    """
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]
        
        if guess == target:
            return mid
        if guess > target:
            high = mid - 1
        else:
            low = mid + 1
    return -1

def binary_search_visual(arr, target):
    """
    Binary search with visualization of search process.
    """
    low = 0
    high = len(arr) - 1
    steps = 0
    
    print("\nSearch Process:")
    print("Indexes:", ' '.join(f'{i:2}' for i in range(len(arr))))
    print("Values: ", ' '.join(f'{x:2}' for x in arr))
    print("-" * 40)
    
    while low <= high:
        steps += 1
        mid = (low + high) // 2
        current_range = arr[low:high+1]
        
        # Visualize current search range
        visual = ['  '] * len(arr)
        for i in range(low, high+1):
            visual[i] = f'{arr[i]:2}'
        visual[mid] = f'[{arr[mid]}]'
        print(f"Step {steps}:", ' '.join(visual))
        
        if arr[mid] == target:
            print(f"\nFound {target} at index {mid} in {steps} steps")
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    print(f"\n{target} not found in the list (searched in {steps} steps)")
    return -1

def generate_sorted_list(length=20, max_value=100):
    """Generate a sorted list of random integers."""
    import random
    return sorted(random.sample(range(max_value), k=length))

def run_tests():
    """Run test cases for binary search."""
    test_cases = [
        ([1, 2, 3, 4, 5], 3, 2),    # Target in middle
        ([1, 2, 3, 4, 5], 1, 0),    # Target at start
        ([1, 2, 3, 4, 5], 5, 4),    # Target at end
        ([1, 2, 3, 4, 5], 6, -1),   # Target not present
        ([], 1, -1),                # Empty list
        ([1, 3, 5, 7], 0, -1),     # Target smaller than all
        ([1, 3, 5, 7], 8, -1)      # Target larger than all
    ]
    
    print("\nRunning Tests:")
    for arr, target, expected in test_cases:
        result = binary_search(arr, target)
        status = "PASSED" if result == expected else "FAILED"
        print(f"Search {target} in {arr}: Result {result} (Expected {expected}) - {status}")

def main_menu():
    """Interactive main menu."""
    while True:
        print("\nBinary Search Project")
        print("1. Run binary search (simple)")
        print("2. Run binary search with visualization")
        print("3. Generate random list and search")
        print("4. Run test cases")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            arr = list(map(int, input("Enter sorted numbers separated by spaces: ").split()))
            target = int(input("Enter number to search for: "))
            result = binary_search(arr, target)
            print(f"Result: {'Found at index ' + str(result) if result != -1 else 'Not found'}")
        
        elif choice == "2":
            arr = list(map(int, input("Enter sorted numbers separated by spaces: ").split()))
            target = int(input("Enter number to search for: "))
            binary_search_visual(arr, target)
        
        elif choice == "3":
            length = int(input("Enter length of random list (default 20): ") or 20)
            max_val = int(input("Enter maximum value (default 100): ") or 100)
            arr = generate_sorted_list(length, max_val)
            print("\nGenerated sorted list:", arr)
            target = int(input("Enter number to search for: "))
            binary_search_visual(arr, target)
        
        elif choice == "4":
            run_tests()
        
        elif choice == "5":
            print("Exiting program.")
            break
        
        else:
            print("Invalid choice. Please enter 1-5.")

if __name__ == "__main__":
    main_menu()