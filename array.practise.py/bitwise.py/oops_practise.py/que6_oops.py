class PARENT:
    def parent_class(self):
        print("This is parent class")
class CHILD(PARENT):
    def child_class(self):
        print("This is child class")
p=PARENT()
p.parent_class()
c=CHILD()
c.child_class()
c.parent_class()