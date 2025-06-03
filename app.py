from flask import Flask, request, jsonify

app = Flask(__name__)

def get_project(month, day):
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

@app.route('/')
def index():
    return "Welcome to the Zodiac Sign Finder!"

@app.route('/project', methods=['GET'])
def project():
    try:
        birth_date = request.args.get('date')
        month, day, year = map(int, birth_date.split('-'))
        zodiac_sign = get_project(month, day)
        return jsonify({"zodiac": zodiac_sign})
    except (ValueError, TypeError):
        return jsonify({"error": "Invalid date format"}), 400

if __name__ == '__main__':
    app.run(debug=True)