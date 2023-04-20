from flask import Flask, render_template
from Score import get_score
from Utils import BAD_RETURN_CODE

app = Flask(__name__)


@app.route('/')
def score_server():
    score = get_score()
    if score > 0:
        return render_template('Score.html', score=score)
    else:
        return render_template('Error.html', error=BAD_RETURN_CODE)


if __name__ == '__main__':
    app.run()
