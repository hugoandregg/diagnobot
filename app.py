from flask import Flask, request, Response, render_template
import json

app = Flask(__name__, static_url_path = "", static_folder = "templates")

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/salvar_json')
def salvar():
	params = sorted(request.args.items())
	data = {}
	data_list = []
	for param, value in params:
		data_aux = {}
		if "introducao" in param:
			data_aux['type'] = "intro"
			data_aux['text'] = value
		elif "historia" in param:
			data_aux['type'] = "story"
			data_aux['text'] = value
		elif "questao" in param:
			data_aux['type'] = "question"
			data_aux['text'] = value
		data_list.append(data_aux)
	data['actions'] = data_list
	json_data = json.dumps(data)
	return Response(json_data, mimetype='application/json', headers={'Content-Disposition':'attachment;filename=roteiro.json'})


if __name__ == '__main__':
	app.run(debug=True)