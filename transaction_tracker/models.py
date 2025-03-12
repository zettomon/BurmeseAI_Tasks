from django.db import models

class Transaction(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=4)
    date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=10, choices=[('food', 'Food'), ('salary', 'Salary'), ('car_oil', 'Car Oil'), ('groom', 'Gromming')], default='food')
    transaction_type = models.CharField(max_length=10, choices=[('income', 'Income'), ('expense', 'Expense')])


