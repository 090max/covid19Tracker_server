from flask import Flask
from information_fetch import  info_fetch
from flask_cors import CORS
from flask import request

app = Flask(__name__)
cors = CORS(app)


@app.route('/')
def main_page():
   return("The API is UP !!")

#This route Gives the information of today's case report in India
@app.route('/getgeneral')
def get_general():
   try:
      info_fetcher=info_fetch()
      return(info_fetcher.get_general())
   except Exception as ex:
      print(ex)

#This returns a JSON all the case report of india
@app.route('/getanalytics')
def get_general_list():
   try:
      info_fetcher=info_fetch()
      return(info_fetcher.get_entire_general())
   except Exception as ex:
      print(ex)

#This returns the Json of the case report of a particular state or all the states
@app.route('/getstate', methods=['GET'])
def get_state():
   try:
      state = str(request.args.get('state'))

      info_fetcher = info_fetch()
      if(state=="all"):
         return(info_fetcher.get_states())
      else:
         return(info_fetcher.get_particular_state(state))
   except Exception as ex:
      print(ex)


if __name__ == '__main__':
   app.run()