import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load your dataset
df = pd.read_csv('loan_payments_data.csv')

# Create a subset of users who have already stopped paying (Charged Off) and users who are currently behind on payments (Late)
charged_off_users = df[df['loan_status'] == 'Charged Off']
late_users = df[df['loan_status'] == 'Late']

# Define columns of interest
columns_of_interest = ['grade', 'purpose', 'home_ownership']

# Visualize the impact of loan grade on customers not paying
plt.figure(figsize=(12, 6))
sns.countplot(x='grade', hue='loan_status', data=df, order=sorted(df['grade'].unique()))
plt.title('Impact of Loan Grade on Loan Status')
plt.xlabel('Loan Grade')
plt.ylabel('Count')
plt.show()

# Visualize the impact of loan purpose on customers not paying
plt.figure(figsize=(14, 6))
sns.countplot(x='purpose', hue='loan_status', data=df, order=sorted(df['purpose'].unique()))
plt.title('Impact of Loan Purpose on Loan Status')
plt.xlabel('Loan Purpose')
plt.ylabel('Count')
plt.xticks(rotation=45, ha='right')
plt.show()

# Visualize the impact of home ownership on customers not paying
plt.figure(figsize=(10, 6))
sns.countplot(x='home_ownership', hue='loan_status', data=df, order=sorted(df['home_ownership'].unique()))
plt.title('Impact of Home Ownership on Loan Status')
plt.xlabel('Home Ownership')
plt.ylabel('Count')
plt.show()
