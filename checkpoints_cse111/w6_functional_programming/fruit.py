def main():
    # Create and print a list named fruit.
    fruit_list = ["pear", "banana", "apple", "mango"]
    print(f"original: {fruit_list}")
    fruit_list.reverse()
    print(f"reverse: {fruit_list}")
    fruit_list.append("orange")
    print(f"append orange: {fruit_list}")
    fruit_list.insert(1, "cherry")
    print(f"insert cherry: {fruit_list}")
    fruit_list.remove("banana")
    print(f"removed banana: {fruit_list}")
    pop_item = fruit_list.pop()
    print(f"Popped {pop_item}: {fruit_list}")
    fruit_list.sort()
    print(f"sorted list: {fruit_list}")
    fruit_list.clear()
    print(f"cleared list: {fruit_list}")





if __name__ == '__main__':
    main()