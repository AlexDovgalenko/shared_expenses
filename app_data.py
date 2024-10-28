from dataclasses import dataclass
from typing import List


@dataclass
class Participant:
    """Class represents participants to share common expenses."""
    name: str
    expense: float = 0.0
    balance: float = 0.0


def calculate_expenses(participants: List["Participant"]):
    """Calculates total expenses by all participants."""
    number_of_participants = len(participants)
    total_expense = sum([participant.expense for participant in participants])
    fair_share = total_expense / number_of_participants

    # Calculate each person's balance
    list(map(lambda participant: setattr(participant, 'balance', participant.expense - fair_share), participants))

    # Determine who owes whom
    transactions = []
    for participant in participants:
        if participant.balance > 0:  # person has overpaid
            for other_participant in participants:
                if other_participant.balance < 0:  # other person has underpaid
                    amount_to_transfer = min(participant.balance, -other_participant.balance)
                    transactions.append(f"{other_participant.name} --> {participant.name} ${amount_to_transfer:.2f}")
                    participant.balance -= amount_to_transfer
                    other_participant.balance += amount_to_transfer

    return total_expense, fair_share, transactions
