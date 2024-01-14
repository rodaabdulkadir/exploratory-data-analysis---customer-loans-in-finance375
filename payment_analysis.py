import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load your dataset
df = pd.read_csv('loan_payments_data.csv')

# Summarize currently what percentage of the loans are recovered against the investor funding and the total amount funded
df['recovery_percentage'] = (df['recoveries'] / df['funded_amount_inv']) * 100
df['total_percentage'] = (df['total_payment'] / df['funded_amount_inv']) * 100

# Set a consistent color palette
sns.set_palette("viridis")

# Create subplots for better visualization
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(15, 6))

# Plot 1: Percentage of Loans Recovered Against Investor Funding
sns.barplot(x='loan_status', y='recovery_percentage', data=df, ax=axes[0])
axes[0].set_title('Percentage of Loans Recovered Against Investor Funding')
axes[0].set_xlabel('Loan Status')
axes[0].set_ylabel('Recovery Percentage')
axes[0].tick_params(axis='x', rotation=45)  # Rotate x-axis labels

# Plot 2: Percentage of Total Amount Funded Received
sns.barplot(x='loan_status', y='total_percentage', data=df, ax=axes[1])
axes[1].set_title('Percentage of Total Amount Funded Received')
axes[1].set_xlabel('Loan Status')
axes[1].set_ylabel('Total Percentage')
axes[1].tick_params(axis='x', rotation=45)  # Rotate x-axis labels

# Adjust layout to prevent overlapping
plt.tight_layout()
plt.show()

# Calculate the percentage of charged-off loans historically and the total amount paid towards these loans before being charged off
charged_off_loans = df[df['loan_status'] == 'Charged Off']
charged_off_percentage = (charged_off_loans.shape[0] / df.shape[0]) * 100
total_paid_charged_off = charged_off_loans['total_payment'].sum()

# Display results
print(f"Percentage of Charged Off Loans: {charged_off_percentage:.2f}%")
print(f"Total Amount Paid towards Charged Off Loans: ${total_paid_charged_off:,.2f}")

# Calculate the projected loss of Charged Off loans
projected_loss = charged_off_loans['funded_amount_inv'] - charged_off_loans['recoveries']

# Calculate the loss in revenue these loans would have generated if they had finished their term
remaining_term_loss = projected_loss * (charged_off_loans['total_percentage'] / 100)

# Plot the projected loss over the remaining term
plt.figure(figsize=(10, 6))
sns.barplot(x=charged_off_loans['term'], y=remaining_term_loss)
plt.title('Projected Loss of Charged Off Loans Over Remaining Term')
plt.xlabel('Remaining Term (Months)')
plt.ylabel('Projected Loss')
plt.show()

# Identify customers currently behind on payments
late_payments = df[df['loan_status'].isin(['Late', 'Default'])]

# Calculate the percentage of customers currently behind on payments
late_payments_percentage = (late_payments['id'].count() / df['id'].count()) * 100

# Calculate the total amount of customers currently behind on payments
late_payments_total = late_payments['id'].count()

# Check if there are late payments before calculating potential and projected loss
if late_payments_total > 0:
    # Calculate the potential loss if customers in this bracket were charged off
    late_payments_loss = late_payments['funded_amount_inv'].sum()

    # Calculate the projected loss if customers in this bracket were to finish the full loan term
    late_payments_projected_loss = late_payments_loss * (late_payments['total_percentage'].mean() / 100)

    # Display results
    print(f"Percentage of Customers Currently Behind on Payments: {late_payments_percentage:.2f}%")
    print(f"Total Amount of Customers Currently Behind on Payments: {late_payments_total}")
    print(f"Potential Loss if Status Changed to Charged Off: ${late_payments_loss:,.2f}")
    print(f"Projected Loss if Customers Finish Full Loan Term: ${late_payments_projected_loss:,.2f}")
else:
    print("No customers currently behind on payments.")
