import basic

while True:
		text = input('symox >')
		result, error = basic.run(text)

		if error: print(error.as_string())
		else: print(result)
