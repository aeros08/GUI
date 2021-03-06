import matplotlib.pyplot as plt
import pandas as pd

csv_file = pd.read_csv('datasheet.csv')

csv_file = csv_file.ix[41:, ['Output Voltage', 'Time']]
csv_file = csv_file.set_index(['Time'])

csv_file.plot(color='Green')
plt.title('Output Voltage')
plt.show()
