st.markdown("## Features")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("<div class='feature'>", unsafe_allow_html=True)
    st.write("🔍 Issue Identification")
    st.write("Automatically detects the type of workplace problem based on user input.")
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='feature'>", unsafe_allow_html=True)
    st.write("⚖️ Law Mapping")
    st.write("Matches your issue with relevant Indian labour laws and sections.")
    st.markdown("</div>", unsafe_allow_html=True)

with col3:
    st.markdown("<div class='feature'>", unsafe_allow_html=True)
    st.write("📄 Action Guidance")
    st.write("Provides legal steps, required documents, and official complaint portals.")
    st.markdown("</div>", unsafe_allow_html=True)

col4, col5, col6 = st.columns(3)

with col4:
    st.markdown("<div class='feature'>", unsafe_allow_html=True)
    st.write("✉️ Draft Email Generator")
    st.write("Creates a professional complaint email based on your problem.")
    st.markdown("</div>", unsafe_allow_html=True)

with col5:
    st.markdown("<div class='feature'>", unsafe_allow_html=True)
    st.write("📊 Confidence Score")
    st.write("Shows confidence level of detected legal issue for transparency.")
    st.markdown("</div>", unsafe_allow_html=True)

with col6:
    st.markdown("<div class='feature'>", unsafe_allow_html=True)
    st.write("🌐 Official Portals")
    st.write("Redirects you to genuine government labour complaint websites.")
    st.markdown("</div>", unsafe_allow_html=True)