from django.db import models

# Create your models here.

# My Testmodel

class simulation(models.Model):

     windgeschwindigkeit = models.FloatField()
     rollwiderstandskoeffizient = models.FloatField()
     masseFahrzeug = models.FloatField()
     masseInsassen = models.FloatField()
     stirnflaechefahrzeug = models.FloatField()
     gas = models.FloatField()
     bremse = models.FloatField()
     lenkwinkel = models.FloatField()

 # methods
    def get_id(self):
        return self.id

    def get_windgeschwindigkeit(self):
        return self.windgeschwindigkeit

    def get_rollwiderstandskoeffizient(self):
            return self.rollwiderstandskoeffizient

    def get_masseFahrzeug(self):
        return self.masseFahrzeug

    def get_masseInsassen(self):
        return self.masseInsassen

    def get_stirnflaechefahrzeug(self):
        return self.stirnflaechefahrzeug

    def get_gas(self):
            return self.gas

    def get_bremse(self):
                return self.bremse

    def get_lenkwinkel(self):
                return self.lenkwinkel
