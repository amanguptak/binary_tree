def mirrorbt(root):
     if root.left==None and root.right==None:
        return
    #

     mirrorbt(root.right)

     mirrorbt(root.left)
     temp = root.right
     root.right = root.left
     root.left = temp

     return
