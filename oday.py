class parent():
    
    def _init_(self):
        print("This is parent class")
        
    def menu(dish):
         if dish=="buger":
             print("You can add following toppins")
             print("More cheese | Add jalapeno")
         elif dish=="iced_americano":
             print("You can add following toppin")
             print("Add chocolate flavour | Add caramel flavour")
         else:
             print("please enter valid dish")
             
    def final_amount(dish, add_ons):
      if dish=="burger" and add_ons=="cheese":
          print("you need to pay 250 USD")
      elif dish=="burger" and add_ons=="jalapeno":
          print("you need to pay 350 USD")
      elif dish=="iced_americano" and add_ons=="chocolate":
          print("you need to pay 250 USD")
      elif dish=="iced_americano" and add_ons=="caramel":
          print("you need to pay 450 USD")
          
class child1(parent):

    def _init_(self,dish):
        self.new_dish = dish
    def get_menu(self):
        parent.menu(self.new_dish)
        
class child2(parent):

    def _init_(self,dish,addons):
       self.new_dish = dish
       self.addons = addons
       
    def get_final_amount(self):
        parent.final_amount(self.new_dish,self.addons)
        
child1_object=child1("burger")
child1_object.get_menu()

child2_object=child2("burger","jalapeno")
child2_object.get_final_amount()        
        
          
             
             
"""
Created on Mon Dec 27 19:05:49 2021

@author: Admin
"""

