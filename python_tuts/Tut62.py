# class Dad:
#     basketball = 1

# class Son(Dad):
#     dance = 1
#     basketball = 9
#     def isdance(self):
#         return f"Yes I dance {self.dance} no of times"


# class Grandson(Son):
#     dance = 6

#     def isdance(self):
#         return f" Jackson Yeah!! Yes I dance awesomely {self.dance} no of times"


# darry = Dad()
# larry = Son()
# harry = Grandson()

# print(larry.isdance())
# print(harry.isdance())
# print(harry.basketball)

# Exercise Create 3 classes:
# ElectronicDevice
# PocketGadget
# Phone

# Exercise solution

class ElectronicDevice:
    operates_on_electricity = True
    electric_supply = True

    def turnOff(self):
        if self.electric_supply:
            self.electric_supply = False
            print("Successfully turned off device")
        else:
            print("the Device is currently turned off")


class PocketGadget(ElectronicDevice):
    is_portable = True
    in_pocket = False

    def putInPocket(self):
        if self.is_portable and not self.in_pocket:
            self.in_pocket = True
            print("Successfully put device in pocket")
        else:
            print("Device is already in pocket")



class Phone(PocketGadget ):
    can_call = True
    reception_level = 4

    def call(self,phone_num):
        if self.can_call and self.reception_level > 0:
            print(f"Calling {phone_num}... ")
        else:
            print("No Cellular Reception currently, Please try again later")
        

pocket_device = PocketGadget()
phone = Phone()

pocket_device.putInPocket()
phone.putInPocket()
phone.turnOff()
phone.call('1010101010')
