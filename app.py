from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        # Extracting the the form data
        income_details = {
            'income_from_salary': request.form.get('income_from_salary'),
            'income_from_interest': request.form.get('income_from_interest'),
            'rental_income_received': request.form.get('rental_income_received'),
            'income_from_digital_assets': request.form.get('income_from_digital_assets'),
            'other_income': request.form.get('other_income'),
            'exempt_allowances': request.form.get('exempt_allowances'),
            'interest_home_loan_self_occupied': request.form.get('interest_home_loan_self_occupied'),
            'interest_home_loan_let_out': request.form.get('interest_home_loan_let_out')
        }
        
        # Save the form data to a file
        with open('income_details.txt', 'a') as file:
            for key, value in income_details.items():
                file.write(f'{key}: {value}\n')
            file.write('\n')  # Add a newline to separate entries
        
        return "Data submitted successfully!"
    return render_template('income_details.html')

if __name__ == "__main__":
    app.run(debug=True)
