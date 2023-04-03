phrases = input("Стишок Винни: ").split()

vowels = "аяуюоеёэиы"

vowels_counts = []

# ку-да и-дем мы с-пя-тач-ком боль-шой боль-шой сек-рет
# ку-да и-дем мы-спя тач-ком боль-шой боль-шой сек-рет

for phrase in phrases:
    vowels_counts.append(len(list(filter(lambda letter: letter in vowels, phrase))))

print(("Пам парам") if max(vowels_counts) != min(vowels_counts) else ("Парам пам-пам"))
