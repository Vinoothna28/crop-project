import streamlit as st


def apply_global_styles():

    st.html(
        """
        <style>

        /* ==============================
           GLOBAL APPLICATION
        ============================== */

        .stApp {
            background-color: #F5F7F4;
            color: #1F2933;
        }

        .main .block-container {
            max-width: 1400px;
            padding-top: 2rem;
            padding-bottom: 3rem;
            padding-left: 2rem;
            padding-right: 2rem;
        }

        #MainMenu {
            visibility: hidden;
        }

        footer {
            visibility: hidden;
        }


        /* ==============================
           TYPOGRAPHY
        ============================== */

        html,
        body,
        [class*="css"] {
            font-family: "Inter", "Segoe UI", sans-serif;
        }

        h1,
        h2,
        h3 {
            color: #173B2B;
            font-weight: 700;
        }

        p {
            color: #52615A;
            line-height: 1.6;
        }


        /* ==============================
           APPLICATION HEADER
        ============================== */

        .app-header {
            background: linear-gradient(
                135deg,
                #174A32 0%,
                #26734D 100%
            );

            border-radius: 20px;
            padding: 28px 32px;
            margin-bottom: 24px;

            color: white;

            box-shadow:
                0 8px 24px rgba(23, 74, 50, 0.12);
        }

        .app-header-title {
            color: white;
            font-size: 2rem;
            font-weight: 700;
            margin-top: 4px;
            margin-bottom: 8px;
        }

        .app-header-description {
            color: #E4F2E8;
            font-size: 1rem;
            margin: 0;
        }

        .header-badge {
            display: inline-block;

            background-color: rgba(255, 255, 255, 0.16);

            border: 1px solid rgba(255, 255, 255, 0.24);

            color: white;

            border-radius: 999px;

            padding: 6px 12px;

            font-size: 0.8rem;

            font-weight: 600;

            margin-bottom: 10px;
        }


        /* ==============================
           SECTION HEADINGS
        ============================== */

        .section-heading {
            color: #173B2B;

            font-size: 1.35rem;

            font-weight: 700;

            margin-top: 24px;

            margin-bottom: 4px;
        }

        .section-description {
            color: #68766F;

            font-size: 0.92rem;

            margin-bottom: 18px;
        }


        /* ==============================
           DASHBOARD CARDS
        ============================== */

        .dashboard-card {
            background-color: #FFFFFF;

            border: 1px solid #E1E9E2;

            border-radius: 16px;

            padding: 22px;

            min-height: 145px;

            box-shadow:
                0 4px 14px rgba(31, 41, 51, 0.04);
        }

        .dashboard-card-title {
            color: #68766F;

            font-size: 0.84rem;

            font-weight: 600;

            margin-bottom: 10px;
        }

        .dashboard-card-value {
            color: #173B2B;

            font-size: 1.5rem;

            font-weight: 750;

            margin-bottom: 6px;
        }

        .dashboard-card-description {
            color: #7B8780;

            font-size: 0.8rem;
        }


        /* ==============================
           WORKFLOW CARDS
        ============================== */

        .workflow-card {
            background-color: #FFFFFF;

            border: 1px solid #E1E9E2;

            border-radius: 16px;

            padding: 20px;

            min-height: 180px;

            box-shadow:
                0 4px 14px rgba(31, 41, 51, 0.035);
        }

        .workflow-number {
            display: inline-flex;

            align-items: center;

            justify-content: center;

            width: 34px;

            height: 34px;

            background-color: #E8F4EA;

            color: #21633F;

            border-radius: 50%;

            font-weight: 700;

            margin-bottom: 12px;
        }

        .workflow-title {
            color: #173B2B;

            font-size: 1rem;

            font-weight: 700;

            margin-bottom: 8px;
        }

        .workflow-description {
            color: #68766F;

            font-size: 0.85rem;

            line-height: 1.5;
        }


        /* ==============================
           STATUS BADGES
        ============================== */

        .status-badge {
            display: inline-block;

            border-radius: 999px;

            padding: 6px 12px;

            font-size: 0.78rem;

            font-weight: 700;
        }

        .status-healthy {
            background-color: #E2F5E8;

            color: #176534;
        }

        .status-moderate {
            background-color: #FFF3CD;

            color: #856404;
        }

        .status-high {
            background-color: #FDE7E7;

            color: #A61B1B;
        }

        .status-neutral {
            background-color: #EDF0EF;

            color: #52615A;
        }


        /* ==============================
           INFORMATION BANNERS
        ============================== */

        .info-banner {
            background-color: #EAF3FF;

            border-left: 4px solid #367BC4;

            border-radius: 10px;

            padding: 14px 16px;

            color: #244B70;

            font-size: 0.88rem;

            margin: 12px 0;
        }

        .warning-banner {
            background-color: #FFF3CD;

            border-left: 4px solid #D99A00;

            border-radius: 10px;

            padding: 14px 16px;

            color: #765400;

            font-size: 0.88rem;

            margin: 12px 0;
        }

        .emergency-banner {
            background-color: #FDE7E7;

            border-left: 4px solid #C62828;

            border-radius: 10px;

            padding: 16px;

            color: #8D1717;

            font-size: 0.9rem;

            font-weight: 600;

            margin: 12px 0;
        }


        /* ==============================
           BUTTONS
        ============================== */

        .stButton > button {
            width: 100%;

            min-height: 46px;

            border-radius: 10px;

            border: 1px solid #2E7D4F;

            background-color: #287A4E;

            color: white;

            font-weight: 650;

            font-size: 0.92rem;

            transition: all 0.2s ease;
        }

        .stButton > button:hover {
            background-color: #1F603D;

            border-color: #1F603D;

            color: white;
        }


        /* ==============================
           FORM CONTROLS
        ============================== */

        .stSelectbox label,
        .stTextInput label,
        .stFileUploader label,
        .stTextArea label {
            color: #34463B !important;

            font-weight: 600 !important;
        }

        .stTextInput input,
        .stTextArea textarea {
            border-radius: 10px !important;
        }


        /* ==============================
           SIDEBAR
        ============================== */

        section[data-testid="stSidebar"] {
            background-color: #FFFFFF;

            border-right: 1px solid #E1E9E2;
        }

        section[data-testid="stSidebar"] h2 {
            color: #173B2B;
        }


        /* ==============================
           AUDIO CARD
        ============================== */

        .audio-card {
            background-color: #F0F7F1;

            border: 1px solid #D7E9DA;

            border-radius: 14px;

            padding: 18px;

            margin-top: 12px;
        }


        /* ==============================
           FOOTER
        ============================== */

        .app-footer {
            text-align: center;

            color: #87938B;

            font-size: 0.78rem;

            padding-top: 32px;

            padding-bottom: 12px;
        }


        /* ==============================
           MOBILE RESPONSIVENESS
        ============================== */

        @media (max-width: 768px) {

            .main .block-container {
                padding-left: 1rem;
                padding-right: 1rem;
                padding-top: 1rem;
            }

            .app-header {
                padding: 22px;

                border-radius: 14px;
            }

            .app-header-title {
                font-size: 1.55rem;
            }

            .dashboard-card {
                padding: 18px;
            }

            .workflow-card {
                padding: 18px;
            }
        }

        </style>
        """
    )


def render_header():

    st.html(
        """
        <div class="app-header">

            <div class="header-badge">
                SIH26131 · Maharashtra Agritech
            </div>

            <div class="app-header-title">
                🌱 Smart Agri AI
            </div>

            <div class="app-header-description">
                Early crop disease detection and intelligent
                agricultural advisory for farmers.
            </div>

        </div>
        """
    )


def render_section_heading(title, description=""):

    st.html(
        f"""
        <div class="section-heading">
            {title}
        </div>

        <div class="section-description">
            {description}
        </div>
        """
    )


def render_workflow_card(number, title, description):

    st.html(
        f"""
        <div class="workflow-card">

            <div class="workflow-number">
                {number}
            </div>

            <div class="workflow-title">
                {title}
            </div>

            <div class="workflow-description">
                {description}
            </div>

        </div>
        """
    )


def render_dashboard_card(title, value, description):

    st.html(
        f"""
        <div class="dashboard-card">

            <div class="dashboard-card-title">
                {title}
            </div>

            <div class="dashboard-card-value">
                {value}
            </div>

            <div class="dashboard-card-description">
                {description}
            </div>

        </div>
        """
    )