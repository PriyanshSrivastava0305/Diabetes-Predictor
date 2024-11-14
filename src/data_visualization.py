import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data():
    df = pd.read_csv(r"../dataset/diabetes.csv")
    return df

def data_visualization(df):
    plt.figure(figsize=(20, 10))
    sns.lineplot(y='Glucose', x='Age', data=df, alpha=0.7, lw=3)
    plt.title("Diabetes - Glucose vs Age")
    plt.grid()
    plt.show()

    plt.figure(figsize=(30, 20))
    sns.barplot(x='Glucose', y='Age', hue='BMI', width=1, data=df)
    plt.title("Diabetes - Glucose vs Age grouped by BMI")
    plt.show()

    sns.heatmap(df.corr(), cmap="Purples", annot=True)
    plt.title("Correlation Heatmap")
    plt.show()
