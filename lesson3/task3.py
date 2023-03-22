rates = {
    'point1': {'A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R', 'А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т'},
    'point2': {'D', 'G', 'Д', 'К', 'Л', 'М', 'П', 'У'},
    'point3': {'B', 'C', 'M', 'P', 'Б', 'Г', 'Ё', 'Ь', 'Я'},
    'point4': {'F', 'H', 'V', 'W', 'Y', 'Й', 'Ы'},
    'point5': {'K', 'Ж', 'З', 'Х', 'Ц', 'Ч'},
    'point8': {'J', 'X', 'Ш', 'Э', 'Ю'},
    'point10': {'Q', 'Z', 'Ф', 'Щ', 'Ъ'}
}

myWord = input("Your word: ")

countPoints = 0

for letter in myWord:
    for key, val in rates.items():
        if letter.upper() in val:
            countPoints += int(key.replace('point', ''))

print(f"There is {countPoints} points in \"{myWord}\" word")

