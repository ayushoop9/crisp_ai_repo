Python 3.13.4 (tags/v3.13.4:8a526ec, Jun  3 2025, 17:46:04) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
import streamlit as st
import random
from datetime import datetime

# --- Initialization ---
if 'user' not in st.session_state:
    st.session_state.user = None
    st.session_state.users = {}
    st.session_state.leaderboard = {}

modules = [
    "Product Knowledge",
    "Scientific Detailing",
    "Stockist Management",
    "Competitive Intelligence",
    "Digital Literacy",
    "Strategic Planning"
]

# --- Helper Functions ---
def simulate_feedback():
    score = random.randint(65, 100)
    strengths = random.choice(["terminology", "structure", "engagement"])
    improvement = random.choice(["objection handling", "time management", "follow-up"])
    return {
        "score": score,
        "strength": strengths,
        "improvement": improvement,
        "next_steps": f"Practice {improvement.replace(' ', '_')} scenarios"
    }

def update_competency(user):
    xp = user['xp']
    if xp >= 1000:
        user['level'] = "Expert"
    elif xp >= 500:
        user['level'] = "Advanced"
    elif xp >= 250:
        user['level'] = "Intermediate"
    else:
        user['level'] = "Beginner"

# --- Pages ---
st.title("CRISP AI Platform: Learning Dashboard")

if st.session_state.user is None:
    username = st.text_input("Enter your name to begin")
    if st.button("Start Learning") and username:
        st.session_state.user = username
        st.session_state.users[username] = {
            "progress": 0,
            "xp": 0,
            "level": "Beginner",
            "performance": {},
            "badges": [],
            "last_active": datetime.now()
        }
        st.success(f"Welcome {username}!")
        st.experimental_rerun()
else:
    user = st.session_state.users[st.session_state.user]
    st.sidebar.title(f"👤 {st.session_state.user}")
    choice = st.sidebar.radio("Navigation", ["Dashboard", "Modules", "Analytics", "Leaderboard"])

    if choice == "Dashboard":
...         st.subheader("📊 Your Progress")
...         st.progress(user['progress'] / len(modules))
...         st.write(f"**XP:** {user['xp']} | **Level:** {user['level']}")
...         st.write(f"**Modules Completed:** {user['progress']} / {len(modules)}")
... 
...     elif choice == "Modules":
...         st.subheader("📚 Learning Modules")
...         for mod in modules:
...             if st.button(f"Start {mod}"):
...                 feedback = simulate_feedback()
...                 user['progress'] += 1
...                 user['xp'] += feedback['score']
...                 user['performance'][mod] = feedback
...                 user['last_active'] = datetime.now()
...                 if feedback['score'] > 85:
...                     user['badges'].append(f"{mod} Expert")
...                 st.session_state.leaderboard[st.session_state.user] = st.session_state.leaderboard.get(st.session_state.user, 0) + feedback['score']
...                 update_competency(user)
...                 with st.expander(f"Feedback for {mod}", expanded=True):
...                     st.metric("Score", feedback['score'])
...                     st.success(f"Strength: {feedback['strength']}")
...                     st.warning(f"Improvement: {feedback['improvement']}")
...                     st.info(f"Next Step: {feedback['next_steps']}")
... 
...     elif choice == "Analytics":
...         st.subheader("📈 Your Analytics")
...         scores = [v['score'] for v in user['performance'].values()]
...         avg_score = sum(scores) / len(scores) if scores else 0
...         st.write(f"Average Score: {avg_score:.2f}")
...         st.write(f"Modules Attempted: {len(scores)}")
...         st.write("Badges:", ", ".join(user['badges']) or "None yet")
... 
...     elif choice == "Leaderboard":
...         st.subheader("🏆 Leaderboard")
...         sorted_lb = sorted(st.session_state.leaderboard.items(), key=lambda x: -x[1])
...         for i, (name, score) in enumerate(sorted_lb, 1):
...             st.write(f"{i}. {name} - {score} points")
