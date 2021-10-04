def Binary_Tree(root):
    return [root,[],[]]  #returns a list that contain [root, left part of the root, right part of the root]

def insert_left(root, new_branch):

    t = root.pop(1)                                       #popping out the left side of the root element

    if len(t) > 1:                                       #checking the left side element has more left side 
        root.insert(1,[new_branch, t,[]])                  #if it had more element we are placing the new_branch and all other below
    else:
        root.insert(1,[new_branch,[],[]])               #in case no element at left we insert the new_branch in left

    return root


def insert_right(root, new_branch):

    t = root.pop(2)                             #pop(2) because of right element

    if len(t) > 1:
        root.insert(2,[new_branch, [], t])      #(new_branch, left_side, right_side )
    else:
        root.insert(2,[new_branch,[],[]])

    return root


def get_root_value(root):
    return root[0]

def set_root_value(root, new_value):
    root[0] = new_value

def get_left_child(root):
    return root[1]

def get_right_child(root):
    return root[2]

r = Binary_Tree(3)

print(insert_left(r, 4))
print(insert_left(r, 5))
print(insert_right(r, 7))   
print(insert_right(r, 6))

l = get_left_child(r)
print(l)


