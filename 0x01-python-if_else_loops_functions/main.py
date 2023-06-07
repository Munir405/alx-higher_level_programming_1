#!/usr/bin/env python3
pow = __import__('11-pow').pow
fizzbuzz = __import__('12-fizzbuzz').fizzbuzz
remove_char_at = __import__('101-remove_char_at').remove_char_at


print(pow(2, 2))
print(pow(98, 2))
print(pow(98, 0))
print(pow(100, -2))
print(pow(-4, 5))

fizzbuzz()
print("")

print(remove_char_at("Holberton School", 3))
print(remove_char_at("Chicago", 2))
print(remove_char_at("C is fun!", 0))
print(remove_char_at("School", 10))
print(remove_char_at("Python", -2))
