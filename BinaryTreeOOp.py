
#This full Binary search tree code in python


class bst:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right =None

    def insert(self, val):
        if self.key == val:
            return

        if self.key is None:
            self.key = val
            return
        if self.key > val:
            if self.left:
                self.left.insert(val)
            else:
                self.left=bst(val)
        else:
            if self.right:
                self.right.insert(val)
            else:
                self.right = bst(val)

    def pot(self):
          if self is None:
              return

          print(self.key, end=" " )
          if self.left:
              self.left.pot()
          if self.right:
              self.right.pot()



    def detailed(self):
        if self is None:
            return
        else:
            print(self.key,":",end="")
            if self.left is not None:
              print("L",self.left.key,end=",")

            if self.right is not  None:
                print("R",self.right.key)

            print()
            if self.left:
                self.left.detailed()
            if self.right:
                self.right.detailed()

    def delete(self,val):
          if self.key is None:
              print("bst is empty")
          if val<self.key:
              if self.left:
               self.left=self.left.delete(val)
              else:
               print("node is not found")
          elif val>self.key:
              if self.right:
                  self.right=self.right.delete(val)
              else:
                  print("node is not found right")
          else:
              if self.left is None:
                  temp=self.right
                  self=None
                  return temp
              if self.right is None:
                temp=self.left
                self=None
                return  temp

              node =self.right
              while node.left:
                  node=node.left

              self.key=node.key
              self.right=self.right.delete(node.key)

          return self


    def min(self):
      if self.key is None:
          print("tree is empty")
      current=self
      while current.left:
            current=current.left

      print(" \n min node of tree is found", current.key)

    def maxim(self):
        if self.key is None:
            print("tree is empty")
        current=self
        while current.right:
            current=current.right

        print("\n max node of tree is ", current.key)


    def inot(self):

        if self.key is None:
          return
        if self.left:
          self.left.inot()
        print( self.key , end=" ")
        if self.right:
          self.right.inot()

    def count(self):
     if self is None:
         return 0



     if self.left:
           l=self.left.count()
     else:
      l=0
     if self.right:
           r=self.right.count()
     else:
         r=0

     return 1+l+r

#number of node in tree

def count(root):
     if root is None:
        return 0

     l=count(root.left)
     r=count(root.right)
     return 1+l+r

#by help of array making bst

def lisoftree(list):
    length=len(list)
    if length==0:
        return None
    mid=length//2
    root=bst(list[mid])
    left=list[0:mid]
    right=list[mid+1:]
    le=lisoftree(left)
    ri=lisoftree(right)
    root.left=le
    root.right=ri
    return root




lid=[1,2,3,4,5,6,7]
root=lisoftree(lid)
root.detailed()
a=root.count()
print(a)


'''coun = count(root)
print(coun)
root.detailed()

"""root.pot()
root.delete(94)
print("\n")
root.pot()

print("\n")
root.delete(36)
print("\n")
root.pot()

root.min()
root.maxim()
print("\n")
root.inot()
root.maxim()"""
#root.detailed()'''
