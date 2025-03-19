from LCA import LCA
from Tree import Tree
import debug

lca: LCA
tree = Tree()

def help_print(command, description, indent):
    command = ' '*indent*4 + command
    print(command.ljust(70, '-')+ description)

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


def smart_input(text) -> str:
    while True:
        inp = input(text)
        if inp == "help": help_message()
        elif inp == "exit": exit(0)
        else: return inp

@debug.debugDecorator
def querys():
    global lca
    while True:
        try:
            inp = smart_input("waiting for query's in format: 'a b'\n")
            if inp == "tree":
                pass
            else:
                a, b = map(int, inp.split())
                if a < 0 or b < 0 or a >= lca.n or b >= lca.n:
                    raise Exception(f"Invalid query, a and b must be between 0 and {lca.n-1}, {a} {b}")
                ans = lca.query(a, b)
                print(f"Lowest common ancestor of {a} and {b} is {ans}")
                continue
        except ValueError:
            print("Invalid input")
            print("Use command 'help' for help")
            continue
        except Exception as e:
            print("Error:", e)
            print("Use command 'help' for help")
            continue

@debug.debugDecorator
def main():
    global lca, tree
    match smart_input("Build tree by 'list' or by 'size'?\n"):
        case "list":
            try:
                buildList = list(map(int, smart_input("waiting for parent list:\n").split(",")))
                for i in range(len(buildList)):
                    if buildList[i] > i:
                        raise Exception(f"Invalid input, parent of element i must be smaller than i: {i}, {buildList[i]}")
                tree.build(buildList)
                lca = LCA(tree)
                querys()
            except ValueError:
                print("Invalid input, list objets must be integers")
                print("Use command 'help' for help")
                return main() # restart program on error
            except Exception as e:
                print("Error: ", e)
                print("Use command 'help' for help")
                return main() # restart program on error
        case "size":
            try:
                n = int(smart_input("Enter number of elements:\n"))
                if n <= 0:
                    raise Exception(f"Invalid input, number of elements must be non-negative: {n}")
                buildList = tree.build_random(n)
                print(f"Using parent list: {buildList}")
                lca = LCA(tree)
                querys()
            except ValueError:
                print("Invalid input, size must be an integer")
                print("Use command 'help' for help")
                return main() # restart program on error
            except Exception as e:
                print("Error: ", e)
                print("Use command 'help' for help")
                return main() # restart program on error
        case _:
            print("Invalid input")
            print("Use command 'help' for help")
            return main()

if __name__ == '__main__':
    main()