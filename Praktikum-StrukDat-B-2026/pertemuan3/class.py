class MyKisah:
      def __init__(self, name, age, location):
            self.name = name
            self.age = age
            self.location = location

      def ubahname(self,namabaru):
          self.name = namabaru  
      
      def ubahlocation(self,locationbaru):
          self.location = locationbaru

      def tampil(self):
        return f"Namaku {self.name}, Umurku {self.age}, Asalku dari {self.location}"

p1 = MyKisah("Ali", 18, "Bumi")
p2 = MyKisah("Amanda", 18, "Jakarta")
p3 = MyKisah("Seli", 19, "Matahari")

p1.ubahname("Raib")
p1.ubahlocation("Bulan")
print(p1.tampil())
print(p2.tampil())
print(p3.tampil())