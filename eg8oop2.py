class student:
    # def __init__(self,name,phy,chem,maths):
    #     self.name=name
    #     self.phy_marks=phy
    #     self.chem_marks=chem
    #     self.maths_marks=maths
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def average(self):
        sum=0
        for el in self.marks:
            sum += el
        print("hi,",self.name,"your average marks is",sum/3)
s=student("kushal",[34,56,77])
s.average()
s.name="KUSHAL"
s.average()