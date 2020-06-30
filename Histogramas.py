from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')


ages = [18, 19, 21, 25, 26, 26, 30, 32, 38, 45, 55]
NumBins = int(len(ages)**0.5)
Amplitud = round(((ages[len(ages)-1]-ages[0])/NumBins))
bins = [ages[0]]
Suma = ages[0]
for i in range(NumBins):
    Suma += Amplitud
    bins.append(Suma)
print(bins)
plt.hist(ages, bins=bins, edgecolor='black')

median_age = 29
color = '#fc4f30'

plt.axvline(median_age, color=color, label='Age Median', linewidth=2)

plt.legend()

plt.title('Ages of Respondents')
plt.xlabel('Ages')
plt.ylabel('Total Respondents')

plt.tight_layout()

plt.show()

