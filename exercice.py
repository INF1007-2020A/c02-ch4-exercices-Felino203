#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def is_even_len(string):
	return len(string) % 2 == 0


def get_num_char(string, char):
	num = 0
	for letter in string:
		if letter == char :
			num += 1
	return num


def get_first_part_of_name(name):
	prenommin = name.split("-")[0]
	prenommaj = prenommin[0].upper() + prenommin[1:].lower()
	return "Bonjour, " + prenommaj


def get_random_sentence(animals, adjectives, fruits):
	Sentence = "Aujourd’hui, j’ai vu un %s s’emparer d’un panier %s plein de %s"
	animal = animals[random.randrange(0, (len(animals)))]
	adjective = adjectives[random.randrange(0, (len(adjectives)))]
	fruit = fruits[random.randrange(0, (len(fruits)))]
	return Sentence % (animal, adjective, fruit)


if __name__ == "__main__":
	spam = "Bonjour!"
	parity = "pair" if is_even_len(spam) else "impair"
	print(f"Le nombre de caractère dans la chaine '{spam}' est {parity}.")

	eggs = "Hello, world!"
	print(f"Le nombre d'occurrence de l dans '{eggs}' est : {get_num_char(eggs, 'l')}.")

	parrot = "jean-marc"
	print(f"Pour {parrot}, on a '{get_first_part_of_name(parrot)}'.")

	animals = ("chevreuil", "chien", "pigeon")
	adjectives = ("rouge", "laid et puant", "lourd")
	fruits = ("pommes", "kiwis", "bananes")
	print(get_random_sentence(animals, adjectives, fruits))
