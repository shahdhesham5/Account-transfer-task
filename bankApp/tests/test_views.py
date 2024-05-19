# bankApp/tests/test_views.py
import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from bankApp.models import Account

@pytest.mark.django_db
def test_transaction_same_account(client):
    # Create two accounts
    account1 = Account.objects.create(Identifier='123', name='Account1', balance=1000)
    account2 = Account.objects.create(Identifier='456', name='Account2', balance=1000)

    # Simulate a POST request to transfer between the same account
    response = client.post(reverse('transaction'), {
        'from_account': account1.id,
        'to_account': account1.id,
        'amount': 100
    })

    assert response.status_code == 302  # Redirects back to the transaction page

@pytest.mark.django_db
def test_transaction_insufficient_balance(client):
    # Create two accounts
    account1 = Account.objects.create(Identifier='123', name='Account1', balance=100)
    account2 = Account.objects.create(Identifier='456', name='Account2', balance=1000)

    # Simulate a POST request with insufficient balance
    response = client.post(reverse('transaction'), {
        'from_account': account1.id,
        'to_account': account2.id,
        'amount': 200
    })
   
    assert response.status_code == 302  # Redirects back to the transaction page

@pytest.mark.django_db
def test_transaction_success(client):
    # Create two accounts
    account1 = Account.objects.create(Identifier='123', name='Account1', balance=1000)
    account2 = Account.objects.create(Identifier='456', name='Account2', balance=1000)

    # Simulate a successful POST request
    response = client.post(reverse('transaction'), {
        'from_account': account1.id,
        'to_account': account2.id,
        'amount': 200
    })

    assert response.status_code == 302  # Redirects back to the transaction page

    # Refresh accounts from the database to check updated balances
    account1.refresh_from_db()
    account2.refresh_from_db()

    assert account1.balance == 800
    assert account2.balance == 1200
