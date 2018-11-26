import matplotlib.pyplot as plt

years = [1950, 1955, 1960, 1965, 1970, 1975, 1980, 1985, 1990, 1995, 2000, 2005,  2010]

pops = [2.5, 2.7, 3, 3.3, 3.6, 4, 4.4, 4.8, 5.3, 5.7, 6.1, 6.5, 6.9]

deaths = [0.5, 0.6, 0.7, 0.8, 1, 1.1, 1.3, 1.4, 1.5, 1.5, 1.6, 1.7, 1.7]

plt.plot(years, pops, marker="X", color=(255/255, 100/255, 100/255))
plt.plot(years, deaths, "--", color=(100/255, 255/255, 100/255))

plt.title("Human population")
plt.ylabel("Population in billions")
plt.xlabel("Population growth by year")


plt.grid(True)
plt.show()
