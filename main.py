

from app_data import Participant, calculate_expenses

if __name__=="__main__":
    p1 = Participant(name="Vadim", expense=144)
    p2 = Participant(name="Alex", expense=118)
    p3 = Participant(name="Slava", expense=0)
    party_list = [p1, p2, p3]
    print(calculate_expenses(party_list))

