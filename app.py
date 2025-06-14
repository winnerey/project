from flask import Flask, request, render_template
from datetime import datetime

app = Flask(__name__)

def is_valid_date(year, month, day):
    try:
        datetime(year=year, month=month, day=day)
        return True
    except ValueError:
        return False

def get_zodiac_sign(month, day):
    if (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "Aries"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "Taurus"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return "Gemini"
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return "Cancer"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "Leo"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "Virgo"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return "Libra"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return "Scorpio"
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return "Sagittarius"
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return "Capricorn"
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "Aquarius"
    else:
        return "Pisces"

@app.route('/', methods=['GET', 'POST'])
def index():
    zodiac_sign = None
    error = None
    birth_date = None
    
    if request.method == 'POST':
        try:
            birth_date = request.form['date']
            year, month, day = map(int, birth_date.split('-'))
            
            if not is_valid_date(year, month, day):
                error = "Invalid date (this date doesn't exist)"
            else:
                zodiac_sign = get_zodiac_sign(month, day)
                
        except (ValueError, TypeError):
            error = "Invalid date format (please use YYYY-MM-DD)"
    
    return render_template('index.html', 
                         zodiac_sign=zodiac_sign, 
                         error=error, 
                         birth_date=birth_date)

if __name__ == '__main__':
    app.run(debug=True)