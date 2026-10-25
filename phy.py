import streamlit as st

st.set_page_config(page_title="Physics Tutor", page_icon="⚡")
st.title("Physics Tutor⚡")
st.write("Learn physics concepts, solve problems, and practice quizzes!")

# --- Section 1: Concept Notes ---
st.header("Concept Explanation")
topics = ["Motion", "Electricity", "Optics", "Newton's Laws", "Work & Energy"]
topic = st.selectbox("Choose a topic:", topics)

if topic == "Motion":
    st.info("Equation of motion: s = ut + 0.5at²")
elif topic == "Electricity":
    st.info("Ohm's Law: V = I × R")
elif topic == "Optics":
    st.info("Lens Formula: 1/f = 1/v - 1/u")
elif topic == "Newton's Laws":
    st.info("Force = mass × acceleration")
elif topic == "Work & Energy":
    st.info("Work = Force × Distance")

# --- Section 2: Problem Solver ---
st.header("Problem Solver")

if topic == "Motion":
    u = st.number_input("Initial velocity (m/s)", value=10.0)
    a = st.number_input("Acceleration (m/s²)", value=2.0)
    t = st.number_input("Time (s)", value=5.0)
    if st.button("Calculate Displacement"):
        s = u * t + 0.5 * a * (t ** 2)
        st.success(f"Displacement = {s} m")

elif topic == "Electricity":
    current = st.number_input("Current (A)", value=2.0)
    resistance = st.number_input("Resistance (Ω)", value=5.0)
    if st.button("Calculate Voltage"):
        voltage = current * resistance
        st.success(f"Voltage = {voltage} V")

elif topic == "Optics":
    object_distance = st.number_input("Object distance (cm)", value=20.0)
    image_distance = st.number_input("Image distance (cm)", value=40.0)
    if st.button("Calculate Focal Length"):
        if object_distance == 0 or image_distance == 0:
            st.error("Object distance and image distance must be non-zero.")
        else:
            focal_length = 1 / ((1 / image_distance) - (1 / object_distance))
            st.success(f"Focal Length = {focal_length:.2f} cm")

elif topic == "Newton's Laws":
    mass = st.number_input("Mass (kg)", value=2.0)
    acceleration = st.number_input("Acceleration (m/s²)", value=3.0)
    if st.button("Calculate Force"):
        force = mass * acceleration
        st.success(f"Force = {force} N")

elif topic == "Work & Energy":
    force = st.number_input("Force (N)", value=10.0)
    distance = st.number_input("Distance (m)", value=5.0)
    if st.button("Calculate Work"):
        work = force * distance
        st.success(f"Work = {work} J")

# --- Section 3: Quiz ---
st.header("Quick Quiz")
quiz_questions = {
    "Motion": {
        "prompt": "A car travels at 10 m/s for 5 s. What is the distance covered if acceleration is 0?",
        "options": {"A": "50 m", "B": "25 m", "C": "10 m", "D": "5 m"},
        "answer": "50 m",
    },
    "Electricity": {
        "prompt": "A circuit has 3 A current and 4 Ω resistance. What is the voltage?",
        "options": {"A": "7 V", "B": "12 V", "C": "1.33 V", "D": "0.75 V"},
        "answer": "12 V",
    },
    "Optics": {
        "prompt": "Using the lens formula, if an object is placed at 20 cm and the image is at 40 cm, the focal length is:",
        "options": {"A": "13.33 cm", "B": "60 cm", "C": "40 cm", "D": "20 cm"},
        "answer": "13.33 cm",
    },
    "Newton's Laws": {
        "prompt": "A car of mass 1000 kg accelerates at 2 m/s². What is the force?",
        "options": {"A": "2000 N", "B": "500 N", "C": "100 N", "D": "20 N"},
        "answer": "2000 N",
    },
    "Work & Energy": {
        "prompt": "A force of 20 N moves an object 3 m. How much work is done?",
        "options": {"A": "60 J", "B": "23 J", "C": "17 J", "D": "6 J"},
        "answer": "60 J",
    },
}

if topic in quiz_questions:
    question = quiz_questions[topic]
    st.write(question["prompt"])
    choice = st.radio("Choose your answer:", list(question["options"].keys()))
    if choice:
        if question["options"][choice] == question["answer"]:
            st.success(f"Correct! {question['answer']}")
        else:
            st.error("Oops! Try again.")
