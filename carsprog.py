class carshowroom:
    def __init__(self,cgst,sgst,insurance):
        self.cgst=cgst
        self.sgst=sgst
        self.insurance=insurance
    def company(self):
     while True:
        a=input("select the brand")
        self.a=a
        if self.a=="mahindra":
            print("welcome to mahindra family") 
            break
        elif self.a=="honda":
            print("welcome to honda family")
            break
        elif self.a=="tata":
            print("welcome to tata family")
            break
        else:
            print("enter valid company")
            
    def model(self):
     while True:
        if self.a=="mahindra":
           b=["thar","xuv"]
           print(b)
           b=input("enter the model")
           self.b=b
           break
        elif self.a=="honda":
             b==["city","civic"]
             print(b)
             b=input("enter the model")
             self.b=b
             break
        elif self.a=="tata":
             b=["nexon","altroz"]
             print(b)
             b=input("enter the model")
             self.b=b
             break
        else:
            print("enter valid model")
            
    def price(self):
     while True:
        if self.a=="mahindra" and self.b=="thar":
          price=1200000
          break
        elif self.a=="mahindra" and self.b=="xuv":
          price=1100000
          break
        elif self.a=="honda" and self.b=="city":
          price=800000
          break
        elif self.a=="honda" and self.b=="civic":
          price=700000
          break
        elif self.a=="tata" and self.b=="nexon":
          price=1000000
          break
        elif self.a=="tata" and self.b=="altroz":
          price=900000
          break
        else:
          print("enter valid")
          
     final_price=price+(self.cgst+self.sgst)/100+self.insurance
     print(final_price)
        
c=["mahindra","honda","tata"]     
print(c)
obj=carshowroom(18,15,200000)
obj.company()
obj.model()
obj.price()

            