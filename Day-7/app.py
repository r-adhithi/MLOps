import streamlit as st
import joblib
import pandas as pd

model = joblib.load("sportsmodel.pkl")
scaler = joblib.load("scaler.pkl")

st.set_page_config(
    page_title="SportifyAI",
    page_icon="🏅",
    layout="wide"
)

st.title("🏅 SportifyAI")
st.subheader("AI-Based Cross-Sport Scout Score Prediction System")

st.markdown("---")

st.header("📥 Athlete Performance Input")

col1, col2 = st.columns(2)

with col1:

    VO2_max = st.number_input(
        "VO2 Max",
        min_value=0.0,
        max_value=100.0,
        value=50.0
    )

    training_hours_per_week = st.number_input(
        "Training Hours Per Week",
        min_value=0,
        max_value=40,
        value=10
    )

    agility_score = st.slider(
        "Agility Score",
        0,
        100,
        50
    )

    strength_score = st.slider(
        "Strength Score",
        0,
        100,
        50
    )

    endurance_score = st.slider(
        "Endurance Score",
        0,
        100,
        50
    )

    speed_index = st.slider(
        "Speed Index",
        0,
        100,
        50
    )

    fatigue_score = st.slider(
        "Fatigue Score",
        0,
        100,
        30
    )

    fitness_score = st.slider(
        "Fitness Score",
        0,
        100,
        50
    )

with col2:

    training_load_au = st.number_input(
        "Training Load",
        min_value=0.0,
        max_value=5000.0,
        value=1000.0
    )

    recovery_time_hr = st.number_input(
        "Recovery Time (Hours)",
        min_value=0.0,
        max_value=72.0,
        value=24.0
    )

    biomechanical_efficiency = st.slider(
        "Biomechanical Efficiency",
        0,
        100,
        50
    )

    participation_ratio_pct = st.slider(
        "Participation Ratio %",
        0,
        100,
        50
    )

    long_term_training_effect_pct = st.slider(
        "Long Term Training Effect %",
        0,
        100,
        50
    )

    adaptation_pct = st.slider(
        "Adaptation %",
        0,
        100,
        50
    )

    training_session_count = st.number_input(
        "Training Session Count",
        min_value=0,
        max_value=30,
        value=5
    )

power_score = (
    strength_score * speed_index
) / 100

recovery_efficiency = (
    endurance_score /
    (recovery_time_hr + 1)
)

training_intensity = (
    training_load_au /
    (training_hours_per_week + 1)
)

endurance_fitness_ratio = (
    endurance_score /
    (fitness_score + 1)
) * 100

st.markdown("---")

if st.button("🔍 Predict Scout Score"):

    input_data = pd.DataFrame([{

        'VO2_max': VO2_max,
        'training_hours_per_week': training_hours_per_week,
        'agility_score': agility_score,
        'strength_score': strength_score,
        'endurance_score': endurance_score,
        'training_load_au': training_load_au,
        'speed_index': speed_index,
        'fatigue_score': fatigue_score,
        'recovery_time_hr': recovery_time_hr,
        'biomechanical_efficiency': biomechanical_efficiency,
        'participation_ratio_pct': participation_ratio_pct,
        'long_term_training_effect_pct': long_term_training_effect_pct,
        'adaptation_pct': adaptation_pct,
        'training_session_count': training_session_count,
        'fitness_score': fitness_score,
        'power_score': power_score,
        'recovery_efficiency': recovery_efficiency,
        'training_intensity': training_intensity,
        'endurance_fitness_ratio': endurance_fitness_ratio

    }])

    input_scaled = scaler.transform(input_data)

    prediction = model.predict(input_scaled)

    scout_score = prediction[0]

    st.success(f"🏅 Predicted Scout Score: {scout_score:.2f}")

    st.progress(min(int(scout_score), 100))

    if scout_score >= 80:
        st.balloons()
        st.success("🔥 Elite Athlete Performance")

    elif scout_score >= 60:
        st.info("💪 Strong Athletic Performance")

    elif scout_score >= 40:
        st.warning("⚡ Average Athletic Performance")

    else:
        st.error("📉 Needs Improvement")

    st.markdown("---")

    st.subheader("🏆 Suggested Sports")

    if speed_index > 80 and agility_score > 80:
        st.write("⚽ Football")
        st.write("🏸 Badminton")
        st.write("🏃 Sprint Running")

    elif strength_score > 80 and endurance_score > 70:
        st.write("🏋 Weightlifting")
        st.write("🤼 Wrestling")
        st.write("🏉 Rugby")

    elif endurance_score > 85:
        st.write("🚴 Cycling")
        st.write("🏃 Marathon")
        st.write("🏊 Swimming")

    else:
        st.write("🏏 Cricket")
        st.write("🏐 Volleyball")
        st.write("🏀 Basketball")