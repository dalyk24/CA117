#!/usr/bin/env python3

class BankAccount(object):
	def set_attributes(self, name, number, balance):
		self.name = name
		self.number = number
		self.balance = balance

	def print_attributes(self):
		print(f"Name: {self.name}")
		print(f"Account number: {self.number}")
		print("Balance: " + str(self.balance) + ".00")

	def deposit(self, amount):
		self.balance += amount
