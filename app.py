import streamlit as st

# =====================================================
# PAGE CONFIG
# =====================================================
st.set_page_config(
    page_title="Legal Rights Assistant",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =====================================================
# GLOBAL STYLING (Premium Dark SaaS UI)
# =====================================================
st.markdown("""
<style>

/* Background */
body {
    background-color: #0f172a;
}

/* Remove Streamlit default padding */
.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

/* Hero Title */
.hero-title {
    font-size: 48px;
    font-weight: 700;
    color: white;
}

/* Hero Subtitle */
.hero-sub {
    font-size: 20px;
    color: #cbd5e1;
    margin-top: 20px;
    margin-bottom: 30px;
}

/* Section Spacing */
.section-space {
    padding-top: 60px;
    padding-bottom: 20px;
}

/* Cards */
.card {
    background: #1e293b;
    padding: 30px;
    border-radius: 14px;
    box-shadow: 0px 10px 25px rgba(0,0,0,0.3);
    color: white;
    height: 100%;
}

/* Section Container */
.section-box {
    background: #1e293b;
    padding: 35px;
    border-radius: 14px;
    box-shadow: 0px 10px 25px rgba(0,0,0,0.3);
    color: #e2e8f0;
}

/* Button Styling */
.stButton>button {
    background: linear-gradient(90deg, #2563eb, #1e40af);
    color: white;
    padding: 12px 28px;
    border-radius: 8px;
    font-weight: 600;
    border: none;
}

.stButton>button:hover {
    background: linear-gradient(90deg, #1e40af, #1e3a8a);
}

/* Fade In Animation */
@keyframes fadeIn {
  from {opacity: 0; transform: translateY(25px);}
  to {opacity: 1; transform: translateY(0);}
}

.hero-title, .hero-sub, .card, .section-box {
    animation: fadeIn 1s ease-in-out;
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# HERO SECTION
# =====================================================
col1, col2 = st.columns([1.2, 1])

with col1:
    st.markdown("<div class='hero-title'>AI Legal Assistant for Workplace Rights</div>", unsafe_allow_html=True)
    st.markdown(
        "<div class='hero-sub'>"
        "Structured legal clarity for employees across India. "
        "Understand your workplace rights and receive guided action steps "
        "based on relevant labour laws."
        "</div>",
        unsafe_allow_html=True
    )

    if st.button("Start Legal Consultation"):
        st.switch_page("pages/assistant.py")

with col2:
    st.image(
        "https://images.unsplash.com/photo-1589829545856-d10d557cf95f",
        use_column_width=True
    )

# =====================================================
# HOW IT WORKS SECTION
# =====================================================
st.markdown("<div class='section-space'></div>", unsafe_allow_html=True)
st.markdown("## Three Steps to Legal Clarity")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class='card'>
        <h4>Describe Your Issue</h4>
        <p>Explain your workplace concern in clear, simple language without legal terminology.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class='card'>
        <h4>Legal Identification</h4>
        <p>The system maps your query to relevant Indian labour and employment laws.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class='card'>
        <h4>Guided Action Steps</h4>
        <p>Receive structured recommendations, documentation guidance, and official resources.</p>
    </div>
    """, unsafe_allow_html=True)

# =====================================================
# FEATURES SECTION
# =====================================================
st.markdown("<div class='section-space'></div>", unsafe_allow_html=True)
st.markdown("## Core Capabilities")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class='card'>
        <h4>Multi-Category Issue Classification</h4>
        <p>Supports salary disputes, harassment, termination concerns, benefits, and overtime violations.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class='card'>
        <h4>Structured Legal Output</h4>
        <p>Provides legal reasoning, relevant provisions, and actionable next steps tailored to your issue.</p>
    </div>
    """, unsafe_allow_html=True)

# =====================================================
# CALL TO ACTION SECTION
# =====================================================
st.markdown("<div class='section-space'></div>", unsafe_allow_html=True)
st.markdown("## Begin Your Consultation")

st.markdown("<div class='section-box'>", unsafe_allow_html=True)

st.write("""
Access the Legal Assistant to describe your workplace issue and receive 
personalized legal guidance aligned with Indian labour regulations.
""")

if st.button("Proceed to Assistant"):
    st.switch_page("pages/assistant.py")

st.markdown("</div>", unsafe_allow_html=True)

# =====================================================
# DISCLAIMER
# =====================================================
st.markdown("<div class='section-space'></div>", unsafe_allow_html=True)
st.markdown("## Disclaimer")

st.markdown("<div class='section-box'>", unsafe_allow_html=True)

st.write("""
This platform provides general legal awareness related to workplace rights in India.  
It does not constitute professional legal advice and should not replace consultation 
with a qualified advocate or legal expert.

Users are encouraged to verify critical legal matters with appropriate authorities 
or licensed professionals.
""")

st.markdown("</div>", unsafe_allow_html=True)