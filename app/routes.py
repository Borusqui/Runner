from app import app
from flask import render_template, request

game_scenes = {
    1: {
        'description': 'You are at a crossroads. Do you go to the forest or the village?',
        'options': [{'id': 2, 'text': 'Go to the forest'}, {'id': 3, 'text': 'Go to the village'}]
    },
    2: {
        'description': 'You are in the forest. Do you fight the monster or run away?',
        'options': [{'id': 4, 'text': 'Fight the monster'}, {'id': 5, 'text': 'Run away'}]
    },
    3: {
        'description': 'You are in the village. Do you talk to the elder or explore the market?',
        'options': [{'id': 6, 'text': 'Talk to the elder'}, {'id': 7, 'text': 'Explore the market'}]
    },
    4: {
        'description': 'You fought the monster. Did you win or lose?',
        'options': [{'id': 8, 'text': 'Win'}, {'id': 9, 'text': 'Lose'}]
    },
    5: {
        'description': 'You ran away. Game Over.',
        'options': []
    }
}

@app.route('/')
def index():
    return render_template('index.html', title ='Home')

@app.route('/start_game')
def start_game():
    return render_template('game_scene.html', scene_id=1, scene_description=game_scenes[1]['description'], options=game_scenes[1]['options'])

@app.route('/choose_option/<int:scene_id>', methods=['POST'])
def choose_option(scene_id):
    option_id = int(request.form['option_id'])
    next_scene = game_scenes.get(option_id, None)
    
    if next_scene is None:
        return render_template('game_over.html')
    
    return render_template('game_scene.html', scene_id=option_id, scene_description=next_scene['description'], options=next_scene['options'])
