import random

class Compte(object):
   def __init__(self, customer_name):
      self.account_number = customer_name + random.choice(['AAA', 'BBB', 'CCC'])
      self._balance = 0

   def deposer(self, montant):
      if montant > 0:
         self._ajuster_balance(montant)

   def retirer(self, montant):
      if montant > 0 and montant <= self._balance:
         self._ajuster_balance(-montant)

   def get_balance(self):
      return self._balance

   def _ajuster_balance(self, montant):
      self._balance += montant
