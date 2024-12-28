import pandas as pd

data = {
    "name": ["John", "Anna", "Peter", "Linda"],
    "age": [23, 36, 34, 21],
    "city": ["New York", "Paris", "Berlin", "London"]

}
df = pd.DataFrame(data)

df.head(2)

