'''consider telephone book data base of n clents. make use of ht implemention to quickly look up clients telephone no. make use of 2 collision handling technique & compare them using no. of comparisons a set of telephone no.'''

class hashing:
	def inpt(self):
		lst=[]
		self.telh=[]
		self.n=int(input("enter total no. of entries: "))
		for i in range (self.n):
			sublist=[]
			tele=str(input("enter the telephone no.: "))
			tel=int(tele)
			self.telh.append(tel)
			sublist.append(tele)			
			name=str(input("enter the name: "))
			
			sublist.append(name)
			lst.append(sublist)
		return (lst)
								
	def display(self,l):
		print("array is :")
		lst=l
		for i in range (len(lst)):
			print(lst[i])
        
	def linear(self,list1):
		list3 = []
		f1 = int(input("enter the size of hashing table"))
		for i in range(f1):
			list3.append(0)
		print("hashtable is", list3)
		for j in range(len(self.telh)):
			g1=self.telh[j]%f1
			if (g1!=0):
				while(list3[g1]!=0):
					g1=(g1+1)
				list3[g1] = list1[j]
			else:
				list3[g1] = list1[j]
		return (list3)
	
	
h=hashing()
a=h.inpt()
h.display(a)
l=h.linear(a)
h.display(l)

		
'''class imp:
  
    def func1(self):
        self.list1=[]
        self.a=int(input("enter the size of array"))
        for i in range(self.a):
            m=int(input("enter the nos"))
            self.list1.append(m)
            print("array is ",self.list1)
            
    def withoutcollision(self):
        self.list2=[]
        f=int(input("enter the size of hashing table"))
        for i in range(f):
            self.list2.append(0)
        print("hashtable is",self.list2)
        for j in range(len(self.list1)):
            g=self.list1[j]%f
            self.list2[g]=self.list1[j]
        print("output is",self.list2)
        
    def withcollision(self):
        self.list3 = []
        f1 = int(input("enter the size of hashing table"))
        for i in range(f1):
            self.list3.append(0)
        print("hashtable is", self.list3)
        for j in range(len(self.list1)):
            g1=self.list1[j]%f1
            while(self.list3[g1]!=0):
                g1=(g1+1)
            self.list3[g1] = self.list1[j]
        print("hashtable is", self.list3)

r=imp()
r.func1()
r.withoutcollision()
r.withcollision()
'''
