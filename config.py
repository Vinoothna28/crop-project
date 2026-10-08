import os
import streamlit as st
from dotenv import load_dotenv

load_dotenv()


def get_config(key, default=""):
    try:
        if key in st.secrets:
            return st.secrets[key]
    except Exception:
        pass

    return os.getenv(key, default)


HF_TOKEN = get_config("HF_TOKEN")

HF_MODEL = get_config(
    "HF_MODEL",
    "linkanjarad/mobilenet_v2_1.0_224-plant-disease-identification"
)

MONGO_URI = get_config("MONGO_URI")

MONGO_DB_NAME = get_config(
    "MONGO_DB_NAME",
    "smart_agri_ai"
)

MONGO_COLLECTION_NAME = get_config(
    "MONGO_COLLECTION_NAME",
    "diseases"
)

MONGO_HISTORY_COLLECTION = get_config(
    "MONGO_HISTORY_COLLECTION",
    "predictions"
)