from .Chef import Chef


from Chef import Chef
#This is how you inherit, it's basically just importing and placing what you want to inherit in parameters
class ChineseChef(Chef):
  
    def make_fried_rice(self):
        print("The chef makes fried rice")