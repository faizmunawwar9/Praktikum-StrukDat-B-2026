class Manusia:

    def jalan(self):
        return "Berjalan"
    
    def lari(self):
        return "Berlari"
    
    def lompat(self):
        return "Melompat"

class Bulan:

    def teleport(self):
        return "SPLASHH"
    
    def berdentum(self):
        return "BUMMM"
    
    def beku(self):
        return "SPROOM"

class Matahari:

    def petir(self):
        return "CTARRR"
    
    def kinetik(self):
        return "Terbang"

class MyKisah(Manusia,Matahari,Bulan):
      def __init__(self, name, age, location,):
            self.name = name
            self.age = age
            self.location = location

      def ubahname(self,namabaru):
          self.name = namabaru  
      
      def ubahlocation(self,locationbaru):
          self.location = locationbaru

      def tampil(self):
        return f"Namaku {self.name}, Umurku {self.age}, Asalku dari {self.location}"

p1 = MyKisah("Ali", 18, "Sagaras")
p2 = MyKisah("April", 18, "Komet")
p3 = MyKisah("Seli", 19, "Matahari")

p1.ubahname("Raib")
p1.ubahlocation("Bulan")
print(p1.tampil())
print(p1.lari(), p1.lompat(), p1.teleport(), p1.beku())
print(p2.tampil())
print(p3.tampil())
print(p3.lompat(), p3.kinetik(), p3.petir())

