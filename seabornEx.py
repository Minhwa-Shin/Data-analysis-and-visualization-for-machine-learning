import matplotlib.pyplot as plt
import seaborn as sns

titanic=sns.load_dataset('titanic')
sns.countplot(x='class',data=titanic)
plt.title('titanic')
plt.show()

iris=sns.load_dataset('iris')
sns.jointplot(x='sepal_length',y='sepal_width',data=iris)
plt.show()

tips=sns.load_dataset('tips')
sns.stripplot(x='day',y='total_bill',data=tips)
plt.show()
