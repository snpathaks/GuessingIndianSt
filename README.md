# Incredible India - States Knowledge Challenge:

An interactive educational web game that tests your knowledge of Indian states through food, history, and monuments. Built with Flask and modern web technologies.

![Game Preview](https://img.shields.io/badge/Game-Interactive%20Learning-orange?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.7+-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-2.3.3-green?style=for-the-badge&logo=flask)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)

## 🎯 Features

### 🎮 Game Mechanics
- **Three Difficulty Levels**: Easy, Medium, and Hard
- **Timed Challenges**: 60-second rounds with time bonuses
- **Progressive Hints**: Food, History, and Monument clues
- **Smart Scoring System**: Points based on difficulty, hints used, and time remaining
- **High Score Tracking**: Persistent score tracking across sessions

### 📚 Educational Content
- **15 Indian States** with authentic information
- **Cultural Food Items**: Traditional dishes and regional specialties
- **Historical Context**: Ancient dynasties, empires, and cultural heritage
- **Architectural Wonders**: Famous monuments and UNESCO World Heritage sites
- **Additional Hints**: Capital cities, nicknames, and unique features

### 🎨 User Experience
- **Responsive Design**: Works seamlessly on desktop and mobile devices
- **Beautiful UI**: Indian flag-inspired color scheme with smooth animations
- **Interactive Elements**: Hover effects, transitions, and visual feedback
- **Accessibility**: Clear typography and intuitive navigation

## 🚀 Quick Start

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd incredible-india-game
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python app.py
   ```

4. **Open your browser**
   Navigate to `http://localhost:5000`

## 🏗️ Project Structure

```
incredible-india-game/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── templates/
│   └── index.html        # Main game interface
└── README.md             # Project documentation
```

## 🎲 How to Play

### Getting Started
1. **Choose Difficulty**: Select Easy (10 pts), Medium (20 pts), or Hard (30 pts)
2. **Read Clues**: Reveal Food, History, and Monument clues as needed
3. **Make Your Guess**: Type the state name and submit your answer
4. **Beat the Clock**: Answer within 60 seconds for time bonuses

### Scoring System
- **Base Points**: 10 (Easy), 20 (Medium), 30 (Hard)
- **Hint Penalty**: -2 points per hint used
- **Time Bonus**: +1 point per 10 seconds remaining
- **Minimum Score**: 1 point (never goes below)

### States Included

#### Easy Level (4 states)
- Maharashtra - Financial capital, Bollywood
- Rajasthan - Land of Kings, largest state
- Punjab - Land of Five Rivers, Golden Temple
- Uttar Pradesh - Most populous, Taj Mahal
- Goa - Smallest state, beautiful beaches

#### Medium Level (7 states)
- Kerala - God's Own Country, backwaters
- Tamil Nadu - Classical dance, ancient temples
- West Bengal - Cultural capital, Durga Puja
- Gujarat - Mahatma Gandhi's birthplace
- Karnataka - Silicon Valley of India
- Madhya Pradesh - Heart of India
- Andhra Pradesh - Spicy cuisine, IT hub

#### Hard Level (3 states)
- Assam - One-horned rhinoceros, tea gardens
- Himachal Pradesh - Hill stations, apple orchards
- Odisha - Jagannath Temple, classical dance

## 🛠️ Technical Details

### Backend (Flask)
- **Session Management**: Secure game state tracking
- **RESTful API**: JSON-based communication
- **Error Handling**: Comprehensive exception management
- **Smart Answer Checking**: Handles abbreviations and partial matches

### Frontend (HTML/CSS/JavaScript)
- **Responsive Design**: Mobile-first approach with Tailwind CSS
- **Modern JavaScript**: ES6+ features with async/await
- **Smooth Animations**: CSS transitions and keyframe animations
- **Interactive UI**: Real-time feedback and visual cues

### Key API Endpoints
- `POST /start_game` - Initialize new game session
- `POST /submit_guess` - Process user's answer
- `POST /use_hint` - Track hint usage
- `POST /new_round` - Start next challenge
- `POST /reset_game` - Reset game state
- `GET /get_stats` - Retrieve game statistics

## 🎨 Design Philosophy

### Visual Design
- **Indian Heritage**: Saffron, white, and green color palette
- **Modern Aesthetics**: Clean layouts with subtle shadows
- **Accessibility**: High contrast ratios and readable fonts
- **Responsive**: Seamless experience across all devices

### User Experience
- **Progressive Disclosure**: Information revealed as needed
- **Immediate Feedback**: Real-time responses to user actions
- **Gamification**: Points, levels, and achievements
- **Educational Value**: Learning through interactive gameplay

## 🔧 Configuration

### Environment Variables
```python
# app.py
app.secret_key = 'incredible-india-states-game-2024'  # Change in production
```

### Customization Options
- **Add New States**: Extend `STATES_DATA` array in `app.py`
- **Modify Scoring**: Adjust `calculate_score()` function
- **Change Timer**: Update timer duration in JavaScript
- **Styling**: Customize CSS classes in `templates/index.html`

## 🚀 Deployment

### Local Development
```bash
python app.py
# Runs on http://localhost:5000
```

### Production Deployment
1. **Set Production Secret Key**
2. **Configure WSGI Server** (Gunicorn, uWSGI)
3. **Set Up Reverse Proxy** (Nginx, Apache)
4. **Enable HTTPS** for secure sessions

### Docker Deployment
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]
```

## 🤝 Contributing

We welcome contributions! Here's how you can help:

### Adding New States
1. Add state data to `STATES_DATA` in `app.py`
2. Include food, history, monument, and hints
3. Assign appropriate difficulty level
4. Test thoroughly

### Improving Features
- Enhanced scoring algorithms
- Additional hint types
- Multiplayer functionality
- Achievement system
- Sound effects and music

### Bug Reports
Please include:
- Browser and version
- Steps to reproduce
- Expected vs actual behavior
- Screenshots if applicable

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- **Cultural Content**: Sourced from authentic Indian heritage resources
- **Design Inspiration**: Traditional Indian art and modern web design
- **Educational Value**: Promoting knowledge of India's rich diversity
- **Community**: Thanks to all contributors and players

## 📞 Support

- **Issues**: Report bugs via GitHub Issues
- **Questions**: Contact the development team
- **Suggestions**: We'd love to hear your ideas!

---

**Made with ❤️ for promoting Indian cultural heritage through interactive learning**

*Incredible India - Unity in Diversity* 🇮🇳












