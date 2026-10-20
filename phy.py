import streamlit as st
import sympy as sp

st.title("Physics Tutor⚡")
st.write("Learn physics concepts, solve problems, and practice quizzes!")

# --- Section 1: Concept Notes ---
st.header("Concept Explanation")
topic = st.selectbox("Choose a topic:", ["Motion", "Electricity", "Optics", "Newton's Laws", "Work & Energy"])

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
        s = u*t + 0.5*a*(t**2)
        st.success(f"Displacement = {s} m")

elif topic == "Electricity":
    I = st.number_input("Current (A)", value=2.0)
    R = st.number_input("Resistance (Ω)", value=5.0)
    if st.button("Calculate Voltage"):
        V = I * R
        st.success(f"Voltage = {V} V")

elif topic == "Optics":
    u = st.number_input("Object distance (cm)", value=20.0)
    v = st.number_input("Image distance (cm)", value=40.0)
    if st.button("Calculate Focal Length"):
        f = 1 / (1/v - 1/u)
        st.success(f"Focal Length = {f:.2f} cm")

elif topic == "Newton's Laws":
    m = st.number_input("Mass (kg)", value=2.0)
    a = st.number_input("Acceleration (m/s²)", value=3.0)
    if st.button("Calculate Force"):
        F = m * a
        st.success(f"Force = {F} N")

elif topic == "Work & Energy":
    F = st.number_input("Force (N)", value=10.0)
    d = st.number_input("Distance (m)", value=5.0)
    if st.button("Calculate Work"):
        W = F * d
        st.success(f"Work = {W} J")

# --- Section 3: Quiz ---
st.header("Quick Quiz")
if topic == "Newton's Laws":
    st.write("A car of mass 1000 kg accelerates at 2 m/s². What is the force?")
    options = {"A": "2000 N", "B": "500 N", "C": "100 N", "D": "20 N"}
    choice = st.radio("Choose your answer:", list(options.keys()))
    if choice:
        if options[choice] == "2000 N":
            st.success("Correct! Force = 2000 N")
        else:
            st.error("Oops! Try again.")
