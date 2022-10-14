from flask import Flask, render_template, jsonify, request
import processor


app = Flask(__name__)

app.config['SECRET_KEY'] = 'enter-a-very-secretive-key-3479373'


@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html', **locals())



@app.route('/chatbot', methods=["GET", "POST"])
def chatbotResponse():

    if request.method == 'POST':
        the_question = request.form['question']

        response = processor.chatbot_response(the_question)

    return jsonify({"response": response })



if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8888', debug=True)





    # message = str(request.form['messageText'])

    # bot_response = bot.get_response(message)

    # while True:

    #     if bot_response.confidence > 0.1:

    #         bot_response = str(bot_response)      
    #         print(bot_response)
    #         return jsonify({'status':'OK','answer':bot_response})
 
    #     elif message == ("bye"):

    #         bot_response='Hope to see you soon'

    #         print(bot_response)
    #         return jsonify({'status':'OK','answer':bot_response})

    #         break

    #     elif message == ("contacts"):

    #         bot_response='contact us 8555034734'

    #         print(bot_response)
    #         return jsonify({'status':'OK','answer':bot_response})

    #         break

    #     else:
        
    #         try:
    #             url  = "https://en.wikipedia.org/wiki/"+ message
    #             page = get(url).text
    #             soup = BeautifulSoup(page,"html.parser")
    #             p    = soup.find_all("p")
    #             return jsonify({'status':'OK','answer':p[1].text})

    #         except IndexError as error:

    #             bot_response = 'Sorry i have no idea about that.'
            
    #             print(bot_response)
    #             return jsonify({'status':'OK','answer':bot_response})
