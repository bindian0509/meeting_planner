temprature = int(input("What's the temprature today?\n"))
rain = input("Is it raining? (Yy/Nn)\n")

print("Rain value : "+rain)
print(rain == "Y" or rain == "y")
print(rain == "N" or rain == "n")


if temprature > 40 and (rain == "y" or rain == "Y"):
    print("Stay inside, too hot outside!\nAlert: Heatstroke chances!")
elif temprature < 10 and (rain == "y" or rain == "Y"):
    print("Stay inside, too cold outside!\nAlert: Pneumonia chances!")
else:
    print("Go outside have fun, awesome mausam!")
