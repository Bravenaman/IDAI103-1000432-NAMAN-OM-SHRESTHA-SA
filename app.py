import streamlit as st

# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------
st.set_page_config(page_title="CoachBot AI", page_icon="🏆", layout="wide")

st.title("🏆 Next Gen Sports Lab – Virtual Sports Performance System")
st.markdown("Elite-level personalized training for young athletes (13–18).")

# -------------------------------------------------
# SIDEBAR – ATHLETE PROFILE
# -------------------------------------------------
st.sidebar.header("Athlete Profile")

sport = st.sidebar.selectbox(
    "Select Sport",
    ["Football", "Basketball", "Cricket", "Tennis"]
)

positions_dict = {
    "Football": ["Striker", "Midfielder", "Defender", "Goalkeeper"],
    "Basketball": ["Point Guard", "Shooting Guard", "Small Forward", "Power Forward", "Center"],
    "Cricket": ["Batsman", "Bowler", "All-Rounder", "Wicket Keeper"],
    "Tennis": ["Singles Player", "Doubles Player"]
}

position = st.sidebar.selectbox("Position", positions_dict[sport])
age_group = st.sidebar.selectbox("Age Group", ["13–15", "16–18"])
fitness_level = st.sidebar.selectbox("Fitness Level", ["Beginner", "Intermediate", "Advanced"])
training_days = st.sidebar.slider("Training Days Per Week", 1, 7, 3)

# -------------------------------------------------
# SCALING LOGIC
# -------------------------------------------------
def scale_sets(base):
    if fitness_level == "Beginner":
        return base
    elif fitness_level == "Intermediate":
        return base + 1
    else:
        return base + 2

def scale_reps(base):
    if fitness_level == "Beginner":
        return base
    elif fitness_level == "Intermediate":
        return int(base * 1.2)
    else:
        return int(base * 1.4)

# -------------------------------------------------
# TABS
# -------------------------------------------------
tab1, tab2, tab3, tab4, tab5 = st.tabs(
    ["🏋️ Deep Training Plan", "⚠️ Injury Assessment", "🧘 Recovery System", "🎯 Match Strategy", "🤖 AI Assistant"]
)

# =====================================================
# TAB 1 – LONG FORM TRAINING + NUTRITION
# =====================================================
with tab1:

    st.header("Advanced Weekly Performance Plan")

    if st.button("Generate Complete Performance Plan"):

        sets = scale_sets(3)
        reps = scale_reps(8)

        st.subheader("1️⃣ Weekly Training Structure")
        st.write(f"- Training Days: {training_days} per week")
        st.write("- Day 1: Strength + Position Skills")
        st.write("- Day 2: Speed & Agility")
        st.write("- Day 3: Tactical Simulation")
        st.write("- Active Recovery included")

        st.subheader("2️⃣ Position-Specific Training Block")

        st.write(f"- Main Skill Drill: {sets} sets x {reps} reps")
        st.write(f"- Strength Compound Movement: {sets} sets x {reps} reps")
        st.write(f"- Explosive Sprint Work: {sets} x 20m")
        st.write("- Core Stability Training (Planks, Rotations)")
        st.write("- Balance & Injury Prevention Work")

        st.subheader("3️⃣ Conditioning Block")
        st.write("- Interval training based on sport demands")
        st.write("- Aerobic base building")
        st.write("- Anaerobic burst development")

        st.subheader("4️⃣ Daily Nutrition Plan")

        st.markdown("**Breakfast:**")
        st.write("- Oats / Whole grain toast")
        st.write("- Eggs or yogurt")
        st.write("- Fruit + 500ml water")

        st.markdown("**Lunch:**")
        st.write("- Lean protein (chicken, paneer, fish)")
        st.write("- Rice / Whole wheat pasta")
        st.write("- Vegetables")
        st.write("- 600ml water")

        st.markdown("**Pre-Training Snack:**")
        st.write("- Banana + peanut butter or nuts")
        st.write("- Electrolyte water")

        st.markdown("**Dinner:**")
        st.write("- Protein source")
        st.write("- Complex carbs")
        st.write("- Salad + hydration")

        st.markdown("**Hydration Target:** 2.5–3 Liters daily")

        st.success("Complete weekly training + nutrition system generated.")

with tab2:

    st.header("Injury Risk Analysis & Advisory System")

    st.markdown("Analyze risk level and receive structured training modification guidance.")

    pain_area = st.selectbox(
        "Pain Area",
        ["None", "Knee", "Ankle", "Shoulder", "Hamstring", "Groin", "Lower Back", "Wrist / Forearm", "Shin Splints", "Achilles"]
    )

    pain_level = st.slider("Pain Level (1–10)", 1, 10, 3)
    training_load = st.slider("Weekly Training Intensity (1–10)", 1, 10, 5)
    previous_injury = st.selectbox("Previous Injury?", ["No", "Yes"])

    if st.button("Assess Risk"):

        risk_score = pain_level + training_load
        if previous_injury == "Yes":
            risk_score += 3

        if risk_score < 8:
            risk_status = "Low Risk"
        elif risk_score < 14:
            risk_status = "Moderate Risk"
        else:
            risk_status = "High Risk"

        st.subheader(f"Risk Status: {risk_status}")

        if risk_status == "Low Risk":
            st.success("Continue training with slight monitoring.")
            st.write("- Maintain mobility work")
            st.write("- Avoid sudden load increases")

        elif risk_status == "Moderate Risk":
            st.warning("Training modification required.")
            st.write("- Reduce high-impact drills")
            st.write("- Add mobility + strengthening")
            st.write("- Monitor pain progression daily")

        else:
            st.error("High injury risk detected.")
            st.write("- Stop high intensity training")
            st.write("- Focus on recovery and physio guidance")
            st.write("- Gradual return-to-play protocol required")

with tab3:

    st.header("Structured Recovery Protocol")

    st.markdown("Generate structured post-training recovery plan.")

    if st.button("Generate Recovery Plan"):

        st.subheader("Recovery Plan Overview")

        st.write("🔹 Mobility & Soft Tissue")
        st.write("- 10–15 min foam rolling")
        st.write("- Dynamic mobility circuits")

        st.write("🔹 Hydration")
        st.write("- 2.5–3 liters water daily")
        st.write("- Electrolytes if heavy sweating")

        st.write("🔹 Nutrition Recovery")
        st.write("- Protein within 30–60 mins")
        st.write("- Balanced carbs for glycogen restoration")

        st.write("🔹 Sleep Optimization")
        st.write("- 8–10 hours sleep")
        st.write("- No screens 45 mins before bed")

        st.success("Recovery system generated based on youth safety guidelines.")

with tab4:

    st.header("Match Strategy Generator")

    st.markdown("Generate tactical approach based on opponent strength.")

    opponent_strength = st.selectbox("Opponent Strength", ["Weak", "Average", "Strong"])

    if st.button("Generate Strategy"):

        st.subheader("Game Plan")

        if opponent_strength == "Weak":
            st.success("High press & offensive dominance.")
            st.write("- Maintain possession")
            st.write("- Push defensive line higher")
            st.write("- Encourage creative plays")

        elif opponent_strength == "Average":
            st.success("Balanced tactical approach.")
            st.write("- Structured formation")
            st.write("- Quick transitions")
            st.write("- Controlled aggression")

        else:
            st.warning("Defensive compact strategy.")
            st.write("- Lower defensive block")
            st.write("- Counter-attack focus")
            st.write("- Minimize risky passes")

        st.subheader("Position-Specific Focus")

        st.write(f"As a {position} in {sport}:")
        st.write("- Improve decision timing")
        st.write("- Maintain positional discipline")
        st.write("- Communicate consistently")

        st.info("Mental cue: Focus on execution, not outcome.")

# =====================================================
# TAB 5 – WACP REQUIRED PROMPTS
# =====================================================
with tab5:

    st.header("AI Assistant")

    st.markdown("Select Required Prompt:")

    prompt_option = st.selectbox(
        "Prompt",
        [
            "Full-Body Workout Plan",
            "Safe Recovery Schedule",
            "Tactical Coaching Tips",
            "Week-Long Nutrition Guide",
            "Warm-Up & Cooldown Routine",
            "Beginner Question"
        ]
    )

    if prompt_option == "Full-Body Workout Plan":
        if st.button("Generate"):
            st.write(f"Full-body plan for a {position} in {sport}:")
            st.write("- Lower body strength")
            st.write("- Upper body stability")
            st.write("- Core rotation training")
            st.write("- Sprint conditioning")
            st.write("- Mobility & cooldown")

    elif prompt_option == "Safe Recovery Schedule":
        injury = st.text_input("Enter injury:")
        if st.button("Generate Recovery"):
            st.write(f"Recovery schedule for {injury}:")
            st.write("- Reduced intensity training")
            st.write("- Mobility exercises")
            st.write("- Ice / heat therapy guidance")
            st.write("- Gradual return-to-play protocol")

    elif prompt_option == "Tactical Coaching Tips":
        skill = st.text_input("Enter skill to improve:")
        if st.button("Generate Tactical Tips"):
            st.write(f"Tactical improvement tips for {skill} in {sport}:")
            st.write("- Improve spatial awareness")
            st.write("- Study professional examples")
            st.write("- Practice under game pressure")
            st.write("- Focus on decision speed")

    elif prompt_option == "Week-Long Nutrition Guide":
        diet_type = st.text_input("Enter diet type:")
        if st.button("Generate Nutrition"):
            st.write(f"7-Day Nutrition Guide for 15-year-old athlete ({diet_type}):")
            st.write("- Balanced macronutrients daily")
            st.write("- Hydration tracking")
            st.write("- Protein with every meal")
            st.write("- Carbohydrate timing around training")

    elif prompt_option == "Warm-Up & Cooldown Routine":
        if st.button("Generate Routine"):
            st.write(f"Warm-up and cooldown for {sport} {position}:")
            st.write("- Dynamic stretches")
            st.write("- Activation drills")
            st.write("- Gradual intensity build")
            st.write("- Static stretching cooldown")

    elif prompt_option == "Beginner Question":
        question = st.text_input("Ask your beginner sports question:")
        if st.button("Answer Question"):
            st.write("Basic guidance:")
            st.write("- Start with fundamentals")
            st.write("- Focus on technique first")
            st.write("- Avoid overtraining")
            st.write("- Consistency beats intensity")
