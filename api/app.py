from flask import Flask, request, jsonify
from cocomo import OrganicCocomo, SemiDetachedCocomo, EmbeddedCocomo
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Welcome to the COCOMO Estimation API!"


@app.route('/estimate', methods=['POST'])
def estimate():
    data = request.json
    model_type = data.get('model_type')
    kloc = data.get('kloc')
    a=data.get('a')
    b=data.get('b')
    c=data.get('c')
    d=data.get('d')
    cost_drivers = data.get('cost_drivers', {})

    if model_type == 'organic':
        model = OrganicCocomo()
    elif model_type == 'semi-detached':
        model = SemiDetachedCocomo()
        if 'cost_driver' in cost_drivers:
            model.set_cost_driver(cost_drivers['cost_driver'])
    elif model_type == 'embedded':
        model = EmbeddedCocomo()
        model.set_cost_drivers(cost_drivers)
    else:
        return jsonify({"error": "Invalid model type"}), 400

    if a: model.a = a
    if b: model.b = b
    if c: model.c = c
    if d: model.d = d
    
    effort = model.effort(kloc)
    time = model.time(kloc)

    return jsonify({
        "effort_person_months": effort,
        "development_time_months": time
    })



if __name__ == '__main__':
    app.run
