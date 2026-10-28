# Código Inicial para a Tarefa do Jogo da Forca

import random

# Lista de palavras possíveis
words = ['python', 'hangman', 'challenge', 'programming', 'computer']

def play_game():
	secret_word = random.choice(words)
	guessed_letters = set()
	incorrect_guesses = 0
	max_incorrect = 6

	while incorrect_guesses < max_incorrect:
		progress = ' '.join(
			letter if letter in guessed_letters else '_'
			for letter in secret_word
		)
		print(f'Palavra: {progress}')
		print(f'Tentativas restantes: {max_incorrect - incorrect_guesses}')

		if all(letter in guessed_letters for letter in secret_word):
			print('Parabéns! Você venceu!')
			return

		guess = input('Digite uma letra: ').strip().lower()
		if len(guess) != 1 or not guess.isalpha():
			print('Digite apenas uma letra válida.')
			continue
		if guess in guessed_letters:
			print('Você já tentou essa letra.')
			continue

		guessed_letters.add(guess)
		if guess not in secret_word:
			incorrect_guesses += 1
			print('Letra incorreta.')
		else:
			print('Acertou!')

	print(f'Você perdeu! A palavra era: {secret_word}')


if __name__ == '__main__':
	play_game()
