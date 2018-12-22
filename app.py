from flask import Flask, render_template, url_for, request
import operator

app = Flask(__name__)

# home
@app.route('/')
def home():
    return render_template('home.html')

# Word Count
@app.route('/count', methods=['GET', 'POST'])
def count():
    if request.method == 'POST':
        data = request.form['fulltextarea']
        word_list = data.split()
        list_length = len(word_list)

        word_disc = {}
        for word in word_list:
            if word in word_disc:
                word_disc[word] += 1
            else:
                word_disc[word] = 1

        sort_list = sorted(word_disc.items(), key=operator.itemgetter(1), reverse=True)
        return render_template('count.html', fulltext=data, words=list_length, worddisc=sort_list)

    return render_template('home.html')


if __name__ == "__main__":
    app.secret_key = '0b579d376dc5dde856e0a0ddca6f403cc8707924ff8d6d31'
    app.run(debug=True)