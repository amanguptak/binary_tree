
def height(root):
    if root==None:
        return 0
    left=height(root.left)
    right=height(root.right)
    if (left==right):
        return 1+left
    else:
        return 1+max(left,right)

def bltree(root):
    if root==None:
        return True
    if height(root.left)-height(root.right)>1 or height(root.right)-height(root.left)>1:
        return False
    left_sub=bltree(root.left)
    right_sub=bltree(root.right)
    if left_sub and right_sub:
        return True
    else:
     return False
