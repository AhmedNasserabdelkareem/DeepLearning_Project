from flask import Flask, json,request,render_template
import predict

api = Flask(__name__,template_folder='template')

@api.route('/players', methods=['GET'])
def get_table():
  team_id = request.args.get('id', default = 1, type = int)
  gw = request.args.get('gw', default = 29, type = int)
  players = {"data": []}
  data = predict.run(team_id,gw)

  for row in data:
    players['data'].append(row)
  return json.dumps(players)

@api.route("/") 
def home_view(): 
        return "<h1>Ahmed Nasser abdelkareem (9) </h1><h1>Abdelrahman Ahmed Mohamed Omran (36)</h1>"

if __name__ == '__main__':
    api.run()
