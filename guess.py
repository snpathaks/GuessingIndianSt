from flask import Flask, render_template, request, jsonify, session
import random
import json
from datetime import datetime
import os

app = Flask(__name__)
app.secret_key = 'incredible-india-states-game-2024'

# States data with clues and information
STATES_DATA = [
    {
        "name": "Maharashtra",
        "food": "Famous for spicy Vada Pav, often called the burger of India",
        "history": "Home to the Maratha Empire and birthplace of Chhatrapati Shivaji",
        "monument": "Ajanta and Ellora Caves showcase ancient Buddhist and Hindu art",
        "difficulty": "easy",
        "hints": ["Financial capital of India", "Bollywood is based here", "Mumbai is the capital"],
        "capital": "Mumbai"
    },
    {
        "name": "Rajasthan",
        "food": "Dal Baati Churma is the signature dish of this desert state",
        "history": "Land of Rajputs with magnificent palaces and warrior culture",
        "monument": "Hawa Mahal with its 953 small windows and pink facade",
        "difficulty": "easy",
        "hints": ["Largest state by area", "Known as Land of Kings", "Thar Desert is located here"],
        "capital": "Jaipur"
    },
    {
        "name": "Kerala",
        "food": "Appam with coconut curry is a popular breakfast here",
        "history": "Known as the spice coast, traded with Arabs and Europeans",
        "monument": "Chinese fishing nets dot the coastline of Fort Kochi",
        "difficulty": "medium",
        "hints": ["God's Own Country", "Backwaters and houseboats", "100% literacy rate"],
        "capital": "Thiruvananthapuram"
    },
    {
        "name": "Punjab",
        "food": "Makki di roti with sarson da saag is the winter staple",
        "history": "Birthplace of Sikhism and the Golden Temple",
        "monument": "Golden Temple is the holiest shrine of Sikhism",
        "difficulty": "easy",
        "hints": ["Land of Five Rivers", "Granary of India", "Bhangra dance originated here"],
        "capital": "Chandigarh"
    },
    {
        "name": "Tamil Nadu",
        "food": "Sambar rice and crispy dosas are breakfast favorites",
        "history": "Ancient Chola dynasty built magnificent temples across South India",
        "monument": "Brihadeeswarar Temple in Thanjavur is a UNESCO World Heritage site",
        "difficulty": "medium",
        "hints": ["Chennai is the capital", "Classical dance Bharatanatyam", "Tamil is the official language"],
        "capital": "Chennai"
    },
    {
        "name": "West Bengal",
        "food": "Mishti doi and rosogolla are beloved sweet treats",
        "history": "Cultural capital during British rule and Bengali Renaissance",
        "monument": "Victoria Memorial stands as a symbol of colonial architecture",
        "difficulty": "medium",
        "hints": ["Kolkata is the capital", "Durga Puja festival", "Rabindranath Tagore's birthplace"],
        "capital": "Kolkata"
    },
    {
        "name": "Gujarat",
        "food": "Dhokla and Thepla are popular steamed and flatbread snacks",
        "history": "Birthplace of Mahatma Gandhi and the Salt March",
        "monument": "Statue of Unity is the world's tallest statue",
        "difficulty": "medium",
        "hints": ["Mahatma Gandhi's birthplace", "Vibrant Navratri celebrations", "Major industrial state"],
        "capital": "Gandhinagar"
    },
    {
        "name": "Uttar Pradesh",
        "food": "Lucknowi biryani and kebabs are royal Mughal delicacies",
        "history": "Heart of Mughal Empire with cities like Agra and Lucknow",
        "monument": "Taj Mahal, one of the Seven Wonders of the World",
        "difficulty": "easy",
        "hints": ["Most populous state", "Taj Mahal is located here", "Lucknow is the capital"],
        "capital": "Lucknow"
    },
    {
        "name": "Karnataka",
        "food": "Bisi bele bath and masala dosa with coconut chutney",
        "history": "Vijayanagara Empire and Tipu Sultan's kingdom",
        "monument": "Hampi ruins showcase the grandeur of Vijayanagara Empire",
        "difficulty": "medium",
        "hints": ["Silicon Valley of India", "Bangalore is the capital", "Mysore Palace"],
        "capital": "Bangalore"
    },
    {
        "name": "Assam",
        "food": "Fish curry with bhaat (rice) and famous Assam tea",
        "history": "Ahom dynasty ruled for 600 years resisting Mughal invasions",
        "monument": "Kamakhya Temple is one of the 51 Shakti Peethas",
        "difficulty": "hard",
        "hints": ["One-horned rhinoceros", "Tea gardens", "Brahmaputra river flows through"],
        "capital": "Dispur"
    },
    {
        "name": "Himachal Pradesh",
        "food": "Sidu and dham are traditional mountain delicacies",
        "history": "Hill stations developed during British colonial period",
        "monument": "Shimla's colonial architecture and toy train are UNESCO heritage",
        "difficulty": "hard",
        "hints": ["Hill station state", "Apple orchards", "Shimla is the capital"],
        "capital": "Shimla"
    },
    {
        "name": "Odisha",
        "food": "Pakhala bhata (fermented rice) and dalma are summer staples",
        "history": "Ancient Kalinga kingdom where Ashoka's heart changed after war",
        "monument": "Konark Sun Temple shaped like a colossal chariot",
        "difficulty": "hard",
        "hints": ["Jagannath Temple", "Classical dance Odissi", "Bhubaneswar is the capital"],
        "capital": "Bhubaneswar"
    },
    {
        "name": "Goa",
        "food": "Fish curry rice and bebinca are Portuguese-influenced delicacies",
        "history": "Former Portuguese colony with unique Indo-European culture",
        "monument": "Basilica of Bom Jesus houses St. Francis Xavier's remains",
        "difficulty": "easy",
        "hints": ["Smallest state by area", "Famous beaches", "Panaji is the capital"],
        "capital": "Panaji"
    },
    {
        "name": "Madhya Pradesh",
        "food": "Poha and dal bafla are popular breakfast and main course dishes",
        "history": "Heart of India with ancient kingdoms and tribal heritage",
        "monument": "Khajuraho temples famous for intricate sculptures",
        "difficulty": "medium",
        "hints": ["Heart of India", "Tiger reserves", "Bhopal is the capital"],
        "capital": "Bhopal"
    },
    {
        "name": "Andhra Pradesh",
        "food": "Hyderabadi biryani and spicy Andhra meals with pickles",
        "history": "Ancient Satavahana dynasty and Vijayanagara Empire regions",
        "monument": "Tirumala Venkateswara Temple is one of the richest temples",
        "difficulty": "medium",
        "hints": ["Amaravati is the capital", "Spicy cuisine", "IT hub Hyderabad was here"],
        "capital": "Amaravati"
    }
]

def get_states_by_difficulty(difficulty):
    """Get states filtered by difficulty level"""
    return [state for state in STATES_DATA if state['difficulty'] == difficulty]

def calculate_score(difficulty, hints_used, time_bonus=0):
    """Calculate score based on difficulty, hints used, and time bonus"""
    base_scores = {'easy': 10, 'medium': 20, 'hard': 30}
    base_score = base_scores.get(difficulty, 10)
    hint_penalty = hints_used * 2
    return max(base_score - hint_penalty + time_bonus, 1)

def normalize_string(text):
    """Normalize string for comparison"""
    return text.lower().strip().replace(' ', '')

def check_answer(user_answer, correct_answer):
    """Check if user answer matches the correct answer"""
    user_normalized = normalize_string(user_answer)
    correct_normalized = normalize_string(correct_answer)
    
    # Exact match
    if user_normalized == correct_normalized:
        return True
    
    # Partial match for longer names
    if len(correct_answer) > 6:
        if user_normalized in correct_normalized or correct_normalized in user_normalized:
            return True
    
    # Check for common abbreviations
    abbreviations = {
        'up': 'uttarpradesh',
        'mp': 'madhyapradesh',
        'hp': 'himachalpradesh',
        'ap': 'andhrapradesh',
        'wb': 'westbengal',
        'tn': 'tamilnadu'
    }
    
    if user_normalized in abbreviations and abbreviations[user_normalized] == correct_normalized:
        return True
    
    return False

@app.route('/')
def index():
    """Main game page"""
    # Initialize session variables
    if 'high_score' not in session:
        session['high_score'] = 0
    if 'games_played' not in session:
        session['games_played'] = 0
    
    return render_template('index.html', high_score=session['high_score'])

@app.route('/start_game', methods=['POST'])
def start_game():
    """Start a new game with selected difficulty"""
    try:
        data = request.get_json()
        difficulty = data.get('difficulty', 'easy')
        
        # Get states for selected difficulty
        available_states = get_states_by_difficulty(difficulty)
        if not available_states:
            return jsonify({'success': False, 'message': 'No states available for this difficulty'})
        
        current_state = random.choice(available_states)
        
        # Initialize game session
        session['current_state'] = current_state
        session['difficulty'] = difficulty
        session['current_score'] = 0
        session['hints_used'] = 0
        session['game_start_time'] = datetime.now().timestamp()
        session['games_played'] = session.get('games_played', 0) + 1
        
        return jsonify({
            'success': True,
            'state': current_state,
            'games_played': session['games_played']
        })
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})

@app.route('/submit_guess', methods=['POST'])
def submit_guess():
    """Process user's guess"""
    try:
        data = request.get_json()
        user_guess = data.get('guess', '').strip()
        
        if 'current_state' not in session:
            return jsonify({'success': False, 'message': 'No active game'})
        
        current_state = session['current_state']
        correct = check_answer(user_guess, current_state['name'])
        
        # Calculate time bonus
        game_duration = datetime.now().timestamp() - session.get('game_start_time', 0)
        time_bonus = max(0, int((60 - game_duration) / 10)) if game_duration < 60 else 0
        
        # Calculate score
        score = 0
        if correct:
            score = calculate_score(
                session.get('difficulty', 'easy'),
                session.get('hints_used', 0),
                time_bonus
            )
            session['current_score'] = session.get('current_score', 0) + score
            
            # Update high score
            if session['current_score'] > session.get('high_score', 0):
                session['high_score'] = session['current_score']
        
        return jsonify({
            'success': True,
            'correct': correct,
            'score': score,
            'current_score': session.get('current_score', 0),
            'correct_answer': current_state['name'],
            'time_bonus': time_bonus,
            'high_score': session.get('high_score', 0)
        })
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})

@app.route('/use_hint', methods=['POST'])
def use_hint():
    """Use a hint (increment hint counter)"""
    try:
        session['hints_used'] = session.get('hints_used', 0) + 1
        return jsonify({
            'success': True,
            'hints_used': session['hints_used']
        })
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})

@app.route('/new_round', methods=['POST'])
def new_round():
    """Start a new round with same difficulty"""
    try:
        if 'difficulty' not in session:
            return jsonify({'success': False, 'message': 'No active game'})
        
        difficulty = session['difficulty']
        available_states = get_states_by_difficulty(difficulty)
        current_state = random.choice(available_states)
        
        # Reset round-specific variables
        session['current_state'] = current_state
        session['hints_used'] = 0
        session['game_start_time'] = datetime.now().timestamp()
        session['games_played'] = session.get('games_played', 0) + 1
        
        return jsonify({
            'success': True,
            'state': current_state,
            'games_played': session['games_played']
        })
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})

@app.route('/reset_game', methods=['POST'])
def reset_game():
    """Reset the entire game"""
    try:
        # Keep high score but reset everything else
        high_score = session.get('high_score', 0)
        session.clear()
        session['high_score'] = high_score
        session['games_played'] = 0
        
        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})

@app.route('/get_stats', methods=['GET'])
def get_stats():
    """Get current game statistics"""
    try:
        return jsonify({
            'success': True,
            'high_score': session.get('high_score', 0),
            'current_score': session.get('current_score', 0),
            'games_played': session.get('games_played', 0),
            'hints_used': session.get('hints_used', 0)
        })
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)