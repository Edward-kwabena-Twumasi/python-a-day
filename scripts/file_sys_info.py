from pathlib import Path

def get_file_tree_info(filesys):

    path = Path(filesys)

    if path.exists() :
        
        if path.is_dir():

            dest = Path(filesys)
            children = [get_file_tree_info(entry) for entry in dest.iterdir()]  

            return {
                'name': path.name,
                'parent': path.parent.name,
                'type': 'dir',  
                'children': children
            }
        
        return {
                'name': path.name,
                'parent': path.parent.name,
                'type': 'file',
                'children': []     
            }
        
    else:
        print()
        print('The path does not exist.')
        return None

def draw_tree(tree_info):

    name = tree_info["name"]
    parent = tree_info["parent"]
    child_count =  len(tree_info["children"])
    children = [{"name":child["name"],"type":child["type"]} for child in tree_info["children"]]

    print()
    print("*****  Now ... ** Drawing your tree ... ***** ")
    print()
    print("- {}/{} , {} direct child(ren)".format(parent,name,child_count))

    for child in children:
        print("-- {} ".format(child["name"]))
    
if __name__ == '__main__' : 

    print()
    print()
    print("***** Hi, I'm ... ** getting tree info ***** ")

    tree_info = get_file_tree_info('/Users/macbook/Documents/AI-LAB/Dataset')
    if tree_info is None:
        print()
        print("Oops ... provided path seem to be incorrect")
        print()
    else :

        print()

        print("name : {}".format(tree_info["name"]))
        print()

        print("parent : {}".format(tree_info["parent"]))
        print()

        print("type : {}".format(tree_info["type"]))
        print()

        print("child count : {}".format(len(tree_info["children"])))
        print()

        print("top level children : {}".format([{"name":child["name"],"type":child["type"]} for child in tree_info["children"]]))

        draw_tree(tree_info)
        print()
        print()
        print("*********************************")