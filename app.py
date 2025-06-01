import streamlit as st
from google import genai

# Set page config
st.set_page_config(
    page_title="Predictive Maintenance Analysis",
    page_icon="🔧",
    layout="wide"
)

# Initialize Gemini API
GEMINI_API_KEY = "AIzaSyBDuT94T7WXfoa3mkKn_lijDQMu0_JWDlo"
client = genai.Client(api_key=GEMINI_API_KEY)

# Function to get Gemini prediction and analysis
def get_gemini_prediction(machine_data):
    try:
        prompt = f"""
        As a predictive maintenance expert, provide a precise numerical analysis based on these parameters:

        Machine Parameters:
        - Cycle: {machine_data['cycle']}
        - Machine ID: {machine_data['machine_id']}
        - Temperature: {machine_data['temperature']}°C
        - Vibration: {machine_data['vibration']} mm/s
        - Pressure: {machine_data['pressure']} bar
        - Speed: {machine_data['speed']} RPM
        - Sector: {machine_data['sector']}

        Provide your analysis in this exact format:

        RUL: [Provide a specific number of cycles]
        Condition: [Good/Fair/Poor] - [Brief reason]
        Actions: [List 2-3 specific maintenance tasks]
        Risks: [List 2-3 specific risks with probabilities]

        Keep each section brief and specific. Focus on numbers and actionable insights.
        """
        
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )
        return response.text
    except Exception as e:
        return f"Error getting prediction: {str(e)}"

# Main app
def main():
    st.title("🔧 Predictive Maintenance Analysis")
    st.write("Enter machine parameters to get AI-powered maintenance predictions and recommendations.")

    # Create two columns for input
    col1, col2 = st.columns(2)

    # Initialize input values in session state if they don't exist
    if 'cycle' not in st.session_state:
        st.session_state.cycle = 1
    if 'machine_id' not in st.session_state:
        st.session_state.machine_id = 1
    if 'temperature' not in st.session_state:
        st.session_state.temperature = 25.0
    if 'vibration' not in st.session_state:
        st.session_state.vibration = 1.0
    if 'pressure' not in st.session_state:
        st.session_state.pressure = 1.0
    if 'speed' not in st.session_state:
        st.session_state.speed = 1000.0
    if 'sector' not in st.session_state:
        st.session_state.sector = "Automotive"

    with col1:
        st.subheader("Machine Parameters")
        st.session_state.cycle = st.number_input("Cycle", value=st.session_state.cycle, min_value=1)
        st.session_state.machine_id = st.number_input("Machine ID", value=st.session_state.machine_id, min_value=1)
        st.session_state.temperature = st.number_input("Temperature (°C)", value=st.session_state.temperature)
        st.session_state.vibration = st.number_input("Vibration (mm/s)", value=st.session_state.vibration)
        st.session_state.pressure = st.number_input("Pressure (bar)", value=st.session_state.pressure)
        st.session_state.speed = st.number_input("Speed (RPM)", value=st.session_state.speed)
        
        st.session_state.sector = st.selectbox(
            "Sector",
            ["Automotive", "Energy", "Food Processing", "Manufacturing", "Healthcare", "Transportation"]
        )

    # Create a button for prediction
    if st.button("Get AI Analysis"):
        try:
            # Prepare input data
            machine_data = {
                'cycle': st.session_state.cycle,
                'machine_id': st.session_state.machine_id,
                'temperature': st.session_state.temperature,
                'vibration': st.session_state.vibration,
                'pressure': st.session_state.pressure,
                'speed': st.session_state.speed,
                'sector': st.session_state.sector
            }
            
            # Get prediction and analysis from Gemini
            with st.spinner("Analyzing machine condition..."):
                analysis = get_gemini_prediction(machine_data)
                
                # Display results in a structured format
                st.subheader("AI Analysis Results")
                
                # Split the response into sections and display
                sections = analysis.split('\n')
                for section in sections:
                    if section.strip():
                        if section.startswith('RUL:'):
                            st.metric("Estimated Remaining Useful Life", section.replace('RUL:', '').strip())
                        elif section.startswith('Condition:'):
                            st.info(section.replace('Condition:', '').strip())
                        elif section.startswith('Actions:'):
                            st.success(section.replace('Actions:', '').strip())
                        elif section.startswith('Risks:'):
                            st.warning(section.replace('Risks:', '').strip())
            
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
            st.error("Please try again or check your internet connection.")

if __name__ == "__main__":
    main() 