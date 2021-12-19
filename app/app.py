from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # if request.method == 'POST':
    #     # user inputs
    #     first = request.form.get('first')
    #     second = request.form.get('second')
    #     # api call
    #     url = "https://api.github.com/search/users?q=location:{0} \
    #         +language:{1}".format(first, second)
    #     now = time.ctime(int(time.time()))
    #     response = requests.get(url)
    #     print("Time: {0} / Used Cache: \
    #         {1}".format(now, response.from_cache))
    #     # return json
    #     return jsonify(response.json())
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=True)
