from weather import Weather

paris = Weather("paris")
print(paris.displayWeather())

paris.setWeather(56.6, "Sunny")
print(paris.displayWeather())