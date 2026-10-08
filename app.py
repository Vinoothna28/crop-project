
import streamlit as st

from ui.styles import (
    apply_global_styles,
    render_header,
    render_section_heading,
    render_workflow_card,
    render_dashboard_card
)


# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="Smart Agri AI",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ==========================================
# GLOBAL STYLES
# ==========================================

apply_global_styles()


# ==========================================
# SESSION STATE
# ==========================================

if "language" not in st.session_state:
    st.session_state.language = "English"

if "selected_district" not in st.session_state:
    st.session_state.selected_district = "Nagpur"

if "selected_crop" not in st.session_state:
    st.session_state.selected_crop = "Tomato"

if "analysis_completed" not in st.session_state:
    st.session_state.analysis_completed = False


# ==========================================
# SIDEBAR
# ==========================================

with st.sidebar:

    st.markdown("## 🌱 Smart Agri AI")

    st.caption(
        "Farmer-first crop health and advisory platform"
    )

    st.divider()

    st.markdown("### Application Settings")

    language = st.selectbox(
        "Language / भाषा / భాష",
        options=[
            "English",
            "Telugu",
            "Hindi"
        ],
        index=[
            "English",
            "Telugu",
            "Hindi"
        ].index(st.session_state.language)
    )

    st.session_state.language = language

    st.divider()

    st.markdown("### Navigation")

    selected_page = st.radio(
        "Select module",
        options=[
            "Farmer Dashboard",
            "Crop Health Analysis",
            "Weather & Advisory",
            "My Reports",
            "State Agritech Dashboard"
        ],
        index=0
    )

    st.divider()

    st.markdown("### About")

    st.caption(
        "Prototype developed for Smart India Hackathon "
        "problem statement SIH26131."
    )

    st.caption(
        "AI results are indicative and should be "
        "validated with agricultural experts."
    )


# ==========================================
# MAIN HEADER
# ==========================================

render_header()


# ==========================================
# PAGE ROUTING
# ==========================================

if selected_page == "Farmer Dashboard":

    render_section_heading(
        "Farmer Dashboard",
        "Check your crop health and access local agricultural guidance."
    )

    # --------------------------------------
    # LOCATION AND CROP SELECTION
    # --------------------------------------

    st.markdown(
        '<div class="section-heading">Step 1 · Select Location & Crop</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-description">'
        'Choose your farming location and crop before checking crop health.'
        '</div>',
        unsafe_allow_html=True
    )

    left_column, right_column = st.columns(2)

    with left_column:

        districts = [
            "Nagpur",
            "Pune",
            "Nashik",
            "Jalna",
            "Amravati",
            "Akola",
            "Aurangabad",
            "Kolhapur",
            "Solapur",
            "Other"
        ]

        selected_district = st.selectbox(
            "District",
            districts,
            index=districts.index(
                st.session_state.selected_district
            )
            if st.session_state.selected_district in districts
            else 0
        )

        st.session_state.selected_district = selected_district

    with right_column:

        crops = [
            "Tomato",
            "Cotton",
            "Soybean",
            "Rice",
            "Wheat",
            "Chilli",
            "Onion",
            "Other"
        ]

        selected_crop = st.selectbox(
            "Crop",
            crops,
            index=crops.index(
                st.session_state.selected_crop
            )
            if st.session_state.selected_crop in crops
            else 0
        )

        st.session_state.selected_crop = selected_crop

    st.divider()

    # --------------------------------------
    # WORKFLOW
    # --------------------------------------

    render_section_heading(
        "Your Crop Health Journey",
        "Follow four simple steps to receive an AI-assisted crop advisory."
    )

    workflow_columns = st.columns(4)

    workflow_data = [
        (
            "1",
            "Location & Crop",
            "Select your district, local area, and crop."
        ),
        (
            "2",
            "Weather & Advisory",
            "Check local weather conditions and farming guidance."
        ),
        (
            "3",
            "Upload Leaf Photo",
            "Upload a clear image of the affected plant."
        ),
        (
            "4",
            "Action Plan",
            "Review the predicted issue and recommended next steps."
        )
    ]

    for column, workflow in zip(
        workflow_columns,
        workflow_data
    ):

        with column:

            render_workflow_card(
                workflow[0],
                workflow[1],
                workflow[2]
            )

    st.divider()

    # --------------------------------------
    # SUMMARY CARDS
    # --------------------------------------

    render_section_heading(
        "Current Farm Overview",
        "Live values will be connected in the next service modules."
    )

    summary_columns = st.columns(4)

    with summary_columns[0]:

        render_dashboard_card(
            "Selected Location",
            st.session_state.selected_district,
            "District selected for your session"
        )

    with summary_columns[1]:

        render_dashboard_card(
            "Selected Crop",
            st.session_state.selected_crop,
            "Crop selected for analysis"
        )

    with summary_columns[2]:

        render_dashboard_card(
            "Weather Status",
            "Not checked",
            "Open weather module to fetch data"
        )

    with summary_columns[3]:

        render_dashboard_card(
            "Crop Health",
            "Awaiting scan",
            "Upload a leaf image to begin"
        )

    st.divider()

    # --------------------------------------
    # PRIMARY ACTIONS
    # --------------------------------------

    render_section_heading(
        "Start Crop Health Check",
        "Begin with a weather check or upload a crop image."
    )

    action_left, action_right = st.columns(2)

    with action_left:

        if st.button(
            "🌤️ Check Weather & Advisory",
            key="weather_action"
        ):

            st.info(
                "Weather service integration will be added in Phase 2."
            )

    with action_right:

        if st.button(
            "📷 Start Crop Health Analysis",
            key="analysis_action"
        ):

            st.info(
                "AI image analysis will be added in a later module."
            )

    st.divider()

    # --------------------------------------
    # STATUS AND ACCESSIBILITY
    # --------------------------------------

    render_section_heading(
        "System Status",
        "Service availability will be connected as backend modules are implemented."
    )

    status_left, status_right = st.columns(2)

    with status_left:

        st.markdown(
            """
            <div class="info-banner">
                <strong>Information:</strong>
                This is the initial application interface.
                Weather, AI inference, and database services
                are not connected yet.
            </div>
            """,
            unsafe_allow_html=True
        )

    with status_right:

        st.markdown(
            """
            <div class="warning-banner">
                <strong>Farmer Safety:</strong>
                AI predictions are advisory indicators.
                Confirm treatment decisions using approved
                agricultural guidance and product labels.
            </div>
            """,
            unsafe_allow_html=True
        )


elif selected_page == "Crop Health Analysis":

    render_section_heading(
        "Crop Health Analysis",
        "Upload and review crop images in the next development phase."
    )

    st.info(
        "The image analysis module will be implemented after Phase 1."
    )


elif selected_page == "Weather & Advisory":

    render_section_heading(
        "Weather & Local Advisory",
        "Weather integration and location-based recommendations."
    )

    st.info(
        "The weather service module will be implemented after Phase 1."
    )


elif selected_page == "My Reports":

    render_section_heading(
        "My Reports",
        "Review anonymous crop health reports from this application."
    )

    st.info(
        "Report storage and retrieval will be connected to MongoDB."
    )


elif selected_page == "State Agritech Dashboard":

    render_section_heading(
        "State Agritech Dashboard",
        "District-level anonymous crop health signals and risk summaries."
    )

    st.info(
        "The dashboard will be connected after the reporting service is implemented."
    )


# ==========================================
# FOOTER
# ==========================================

st.markdown(
    """
    <div class="app-footer">
        Smart Agri AI · SIH26131 · Maharashtra
        <br>
        Designed for accessible, farmer-first agricultural support
    </div>
    """,
    unsafe_allow_html=True
)