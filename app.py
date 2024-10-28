from flask import Flask, render_template, request

from app_data import calculate_expenses, Participant

app = Flask(__name__)

participants = []


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'reset_all' in request.form:
            global participants
            participants = []
            return render_template('index.html',
                                   participants=participants,
                                   total_expense=None,
                                   fair_share=None,
                                   transactions=None)
        elif 'add_participant' in request.form:
            # Add participant with expense
            name = request.form['name']
            expense = request.form['expense']
            participants.append(Participant(name=name, expense=float(expense)))
        elif 'calculate' in request.form:
            # Calculate the total expenses
            if participants:
                total_expense, fair_share, transactions = calculate_expenses(participants)
                return render_template('index.html',
                                       participants=participants,
                                       total_expense=total_expense,
                                       fair_share=fair_share,
                                       transactions=transactions)

    return render_template('index.html',
                           participants=participants,
                           total_expense=None,
                           fair_share=None,
                           transactions=None
                           )


if __name__ == '__main__':
    app.run(debug=True)
