from django.db import models


class Payment(models.Model):
    """Base Payment model"""
    id = models.AutoField(primary_key=True)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    order = models.ForeignKey('Order', on_delete=models.CASCADE, related_name='payments')
    payment_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='pending')

    class Meta:
        app_label = 'core'
        db_table = 'core_payment'

    def __str__(self):
        return f"Payment for Order #{self.order.id}"


class CreditCardPayment(models.Model):
    """Credit Card Payment model"""
    id = models.AutoField(primary_key=True)
    card_number = models.CharField(max_length=255)
    card_holder_name = models.CharField(max_length=255)
    card_type = models.CharField(max_length=50)
    transaction_id = models.CharField(max_length=255, unique=True)

    class Meta:
        app_label = 'core'
        db_table = 'core_credit_card_payment'

    def __str__(self):
        return f"Card: {self.card_number[-4:]}"


class EWalletPayment(models.Model):
    """E-Wallet Payment model"""
    id = models.AutoField(primary_key=True)
    wallet_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    transaction_id = models.CharField(max_length=255, unique=True)
    pay_code = models.CharField(max_length=255)

    class Meta:
        app_label = 'core'
        db_table = 'core_ewallet_payment'

    def __str__(self):
        return f"E-Wallet: {self.wallet_name}"


class BankTransfer(models.Model):
    """Bank Transfer Payment model"""
    id = models.AutoField(primary_key=True)
    bank_name = models.CharField(max_length=255)
    account_number = models.CharField(max_length=255)
    account_holder = models.CharField(max_length=255)
    reference_code = models.CharField(max_length=255)

    class Meta:
        app_label = 'core'
        db_table = 'core_bank_transfer'

    def __str__(self):
        return f"Bank: {self.bank_name}"
