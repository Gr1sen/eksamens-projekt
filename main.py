from LCA import LCA
from Tree import Tree
import debug

lca: LCA
tree = Tree()

# format messages for the help message
def help_print(command, description, indent):
    command = ' '*indent*4 + command
    print(command.ljust(70, '-')+ description)

# print help message when 'help' command is called
def help_message():
    help_print("help", "shows this help message", 0)
    help_print("exit", "exits the program", 0)


    help_print("__main()__", "{Build tree by 'list' or by 'size'?}", 0)

    help_print("list", "build tree from list", 1)
    help_print("p1, p2, p3, p4, ..., pn-1", "parent list (0 indexed) where a parent of i must be smaller than i", 2)

    help_print("size", "build random tree from size", 1)
    help_print("n", "build random tree with n nodes", 2)


    help_print("__query()__", "{waiting for query's in format: 'a b'}", 0)
    help_print("a b", "query lowest common ancestor on a and b, a and b must be nodes in the tree", 1)
    help_print("tree", "displays the tree graph", 1)

# checks whether a message contains any global commands before continuing
def smart_input(text) -> str:
    while True:
        inp = input(text)
        if inp == "help": help_message()
        elif inp == "exit": exit(0)
        else: return inp

# handles messages when for querys
@debug.debugDecorator
def querys():
    global lca
    while True:
        try: # because we dont trust the user to put in a valid input
            inp = smart_input("waiting for query's in format: 'a b'\n")
            if inp == "tree":
                lca.tree.print_tree()
                continue
            else:
                a, b = map(int, inp.split())
                if a < 0 or b < 0 or a >= lca.n or b >= lca.n: # checks user input and throw an error if its out of range
                    raise Exception(f"Invalid query, a and b must be between 0 and {lca.n-1}, {a} {b}")
                ans = lca.query(a, b) # calls the actual query to the algorithm
                print(f"Lowest common ancestor of {a} and {b} is {ans}")
                continue
        except ValueError: # handles any error where user typed a wrong type, this is the most expected error a user will get
            print("Invalid input")
            print("Use command 'help' for help")
            continue
        except Exception as e: # handles any other exceptions, including the exceptions i throw
            print("Error:", e)
            print("Use command 'help' for help")
            continue

# handles input for building the tree
@debug.debugDecorator
def main():
    global lca, tree
    match smart_input("Build tree by 'list' or by 'size'?\n"): # use match since input must be on of a few words
        case "list":
            try: # we don't trust that the user puts a valid input
                buildList = list(map(int, smart_input("waiting for parent list:\n").split(",")))
                for i in range(len(buildList)): # checks if the parent list is valid
                    if buildList[i] > i:
                        raise Exception(f"Invalid input, parent of element i must be smaller than i: {i}, {buildList[i]}")
                tree.build(buildList) # build the tree
                lca = LCA(tree) # build the algorithm
                querys() # start the query section
            except ValueError: # handle error where user didn't put in integers in the list
                print("Invalid input, list objets must be integers")
                print("Use command 'help' for help")
                return main() # restart program on error
            except Exception as e: # handles any other error, including custom errors
                print("Error: ", e)
                print("Use command 'help' for help")
                return main() # restart program on error
        case "size":
            try: # dont trust the user
                n = int(smart_input("Enter number of elements:\n"))
                if n <= 0: # there must be at least on node in the tree
                    raise Exception(f"Invalid input, number of elements must be non-negative: {n}")
                buildList = tree.build_random(n) # build the tree
                print(f"Using parent list: {buildList}") # show the parentlist to the user
                lca = LCA(tree) # build algorithm
                querys() # start the query section
            except ValueError: # handle errors where the user didnt put in integers
                print("Invalid input, size must be an integer")
                print("Use command 'help' for help")
                return main() # restart program on error
            except Exception as e: # handles other errors including custom errors
                print("Error: ", e)
                print("Use command 'help' for help")
                return main() # restart program on error
        case _: # handles any invalid input
            print("Invalid input")
            print("Use command 'help' for help")
            return main()

if __name__ == '__main__':
    main()