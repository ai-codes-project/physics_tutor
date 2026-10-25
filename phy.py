import streamlit as st

st.set_page_config(
    page_title="AI Physics Tutor",
    page_icon="⚡",
    layout="wide"
)

# -----------------------------
# Title
# -----------------------------

st.title("⚡ AI Physics Tutor")
st.subheader("An Intelligent Physics Learning Assistant")

st.markdown("""
### 🤖 Project Theme

Artificial Intelligence + Physics + Mathematics

This project demonstrates how AI technology is used in today's world for learning,
problem solving, scientific calculations, and personalized education.
""")

# -----------------------------
# Sidebar
# -----------------------------

st.sidebar.title("📚 Physics Topics")

topic = st.sidebar.selectbox(
    "Select Topic",
    [
        "Newton's Laws",
        "Motion",
        "Electricity",
        "Work and Energy"
    ]
)

# -----------------------------
# Concept Explanation
# -----------------------------

st.header("📖 Detailed Concept Explanation")

if topic == "Newton's Laws":

    st.markdown("""
# Newton's Second Law of Motion

Newton's Second Law states that the force acting on an object is directly proportional to the acceleration produced.

## Formula

F = m × a

Where:

- F = Force (Newton)
- m = Mass (kg)
- a = Acceleration (m/s²)

## Explanation

If a heavier object needs to move, more force is required.

Example:

An empty shopping trolley is easier to push than a loaded trolley.

This is because the loaded trolley has a greater mass.

## Real Life Applications

🚗 Self Driving Cars

🚀 Rockets

⚽ Sports

✈ Aircraft

## AI Connection

Artificial Intelligence systems in self-driving vehicles continuously calculate:

- Speed
- Acceleration
- Force

to make safe driving decisions.

Hence Physics and AI work together.

## Numerical Example

Mass = 5 kg

Acceleration = 4 m/s²

Force = 5 × 4

Force = 20 N
""")

elif topic == "Motion":

    st.markdown("""
# Motion

Motion occurs when the position of an object changes with time.

## Equation of Motion

s = ut + ½at²

Where:

- s = Displacement
- u = Initial Velocity
- a = Acceleration
- t = Time

## Applications

🚗 Car acceleration

🚄 Trains

🚀 Spacecraft

## AI Connection

Navigation systems use AI and motion equations to predict movement and suggest routes.
""")

elif topic == "Electricity":

    st.markdown("""
# Electricity

Electricity is the flow of electric charge.

## Ohm's Law

V = I × R

Where:

- V = Voltage
- I = Current
- R = Resistance

## Applications

💡 Lighting

📱 Smartphones

💻 Computers

## AI Connection

AI manages smart grids and predicts electricity consumption in cities.
""")

elif topic == "Work and Energy":

    st.markdown("""
# Work and Energy

Work is done when a force causes displacement.

## Formula

W = F × d

Where:

- W = Work
- F = Force
- d = Distance

## Applications

🏗 Construction

⚙ Machines

🚗 Vehicles

## AI Connection

Industrial robots calculate force and motion using AI powered systems.
""")

# -----------------------------
# AI in Today's World
# -----------------------------

st.header("🤖 AI Technology in Today's World")

st.markdown("""
Artificial Intelligence uses Physics and Mathematics to solve real-world problems.

### 🚗 Self Driving Cars
AI calculates:
- Speed
- Acceleration
- Braking distance

### 🚀 Space Exploration
AI helps rockets maintain their path.

### ⚡ Smart Energy Systems
AI predicts electricity demand.

### 🏭 Smart Factories
AI controls robots using Physics equations.

### 🏥 Healthcare
AI-powered machines use scientific calculations for diagnosis.

This project demonstrates the connection between Physics, Mathematics and Artificial Intelligence.
""")

# -----------------------------
# Physics Calculator
# -----------------------------

st.header("🧮 Physics Problem Solver")

if topic == "Newton's Laws":

    mass = st.number_input("Mass (kg)", 0.0)

    acceleration = st.number_input(
        "Acceleration (m/s²)",
        0.0
    )

    if st.button("Calculate Force"):

        force = mass * acceleration

        st.success(
            f"Force = {force:.2f} N"
        )

        st.write("### Step-by-Step")

        st.write(f"""
F = m × a

F = {mass} × {acceleration}

F = {force:.2f} N
""")

elif topic == "Motion":

    u = st.number_input("Initial Velocity", 0.0)

    a = st.number_input("Acceleration", 0.0)

    t = st.number_input("Time", 0.0)

    if st.button("Calculate Displacement"):

        s = u*t + 0.5*a*t*t

        st.success(
            f"Displacement = {s:.2f} m"
        )

elif topic == "Electricity":

    current = st.number_input("Current (A)", 0.0)

    resistance = st.number_input("Resistance (Ω)", 0.0)

    if st.button("Calculate Voltage"):

        voltage = current * resistance

        st.success(
            f"Voltage = {voltage:.2f} V"
        )

elif topic == "Work and Energy":

    force = st.number_input("Force (N)", 0.0)

    distance = st.number_input("Distance (m)", 0.0)

    if st.button("Calculate Work"):

        work = force * distance

        st.success(
            f"Work Done = {work:.2f} J"
        )

# -----------------------------
# Quiz Section
# -----------------------------

st.header("🧠 AI Physics Quiz")

questions = [
{
"question":"Newton's Second Law Formula?",
"options":["F = m × a","V = IR","P = VI","W = Fd"],
"answer":"F = m × a"
},
{
"question":"SI unit of Force?",
"options":["Newton","Joule","Watt","Ampere"],
"answer":"Newton"
},
{
"question":"A 5kg body accelerates at 4m/s². Force?",
"options":["20 N","40 N","10 N","5 N"],
"answer":"20 N"
},
{
"question":"Formula for Work Done?",
"options":["W = Fd","V = IR","P = VI","F = ma"],
"answer":"W = Fd"
},
{
"question":"SI unit of Work?",
"options":["Joule","Newton","Watt","Volt"],
"answer":"Joule"
},
{
"question":"Ohm's Law?",
"options":["V = IR","F = ma","W = Fd","P = VI"],
"answer":"V = IR"
},
{
"question":"Unit of Current?",
"options":["Ampere","Volt","Newton","Joule"],
"answer":"Ampere"
},
{
"question":"Who discovered Newton's Laws?",
"options":["Isaac Newton","Einstein","Tesla","Faraday"],
"answer":"Isaac Newton"
},
{
"question":"What is AI used in?",
"options":["Self Driving Cars","Books","Pens","Paper"],
"answer":"Self Driving Cars"
},
{
"question":"Physics is important for?",
"options":["AI Systems","Nothing","Only Sports","Only Art"],
"answer":"AI Systems"
}
]

score = 0

for i, q in enumerate(questions):

    answer = st.radio(
        q["question"],
        q["options"],
        key=i
    )

    if answer == q["answer"]:
        score += 1

if st.button("Submit Quiz"):

    st.success(
        f"Your Score = {score}/10"
    )

    st.progress(score/10)

    # AI Analysis

    st.header("🤖 AI Performance Analysis")

    if score >= 8:

        st.balloons()

        st.success("""
Excellent Performance!

AI Recommendation:

✅ Advanced Mechanics

✅ Robotics

✅ Space Physics

✅ Artificial Intelligence
""")

    elif score >= 5:

        st.warning("""
Good Performance

AI Recommendation:

✅ Revise Newton's Laws

✅ Practice Numerical Problems

✅ Learn Energy Concepts
""")

    else:

        st.error("""
Needs Improvement

AI Recommendation:

✅ Review Basic Physics

✅ Learn Formulas

✅ Practice Daily
""")

# -----------------------------
# Dashboard
# -----------------------------

st.header("📊 Learning Dashboard")

data = pd.DataFrame(
{
"Topic":
[
"Newton",
"Motion",
"Electricity",
"Energy"
],

"Progress":
[
90,
75,
80,
70
]
}
)

st.bar_chart(
data.set_index("Topic")
)

st.success("🎉 Thank you for using AI Physics Tutor!")
.
