from django.apps import AppConfig


class TransactionTrackerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'transaction_tracker'
    verbose_name= "Transaction Tracker"
