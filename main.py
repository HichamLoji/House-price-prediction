
from sklearn.model_selection import train_test_split

data = pd.read_csv("housing.csv")

data.dropna(inplace=True)
print(data)