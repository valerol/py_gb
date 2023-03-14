numbers = list(map(int, input("Your ticket number: ")))

print("You win!" if sum(numbers[:3]) == sum(numbers[3:]) else "Sorry, you don't win")
