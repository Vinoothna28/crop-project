# services/localization.py

"""
Localization service for Smart Agri AI.

Supported languages:
    en -> English
    te -> Telugu
    hi -> Hindi

Usage:
    from services.localization import t

    title = t("app_title", "te")
"""


TRANSLATIONS = {

    # =====================================================
    # APPLICATION
    # =====================================================

    "app_title": {
        "en": "Smart Agri AI",
        "te": "స్మార్ట్ అగ్రి AI",
        "hi": "स्मार्ट एग्री AI"
    },

    "app_subtitle": {
        "en": "Early crop disease detection and intelligent agricultural advisory for farmers.",
        "te": "పంట వ్యాధులను ముందుగా గుర్తించి రైతులకు తెలివైన వ్యవసాయ సలహాలను అందించే వేదిక.",
        "hi": "फसल रोगों की शुरुआती पहचान और किसानों के लिए बुद्धिमान कृषि सलाह।"
    },

    "app_badge": {
        "en": "SIH26131 · Maharashtra Agritech",
        "te": "SIH26131 · మహారాష్ట్ర అగ్రిటెక్",
        "hi": "SIH26131 · महाराष्ट्र एग्रीटेक"
    },


    # =====================================================
    # LANGUAGE
    # =====================================================

    "select_language": {
        "en": "Language",
        "te": "భాష",
        "hi": "भाषा"
    },

    "english": {
        "en": "English",
        "te": "ఇంగ్లీష్",
        "hi": "अंग्रेज़ी"
    },

    "telugu": {
        "en": "Telugu",
        "te": "తెలుగు",
        "hi": "तेलुगु"
    },

    "hindi": {
        "en": "Hindi",
        "te": "హిందీ",
        "hi": "हिंदी"
    },


    # =====================================================
    # NAVIGATION
    # =====================================================

    "navigation": {
        "en": "Navigation",
        "te": "నావిగేషన్",
        "hi": "नेविगेशन"
    },

    "farmer_dashboard": {
        "en": "Farmer Dashboard",
        "te": "రైతు డ్యాష్‌బోర్డ్",
        "hi": "किसान डैशबोर्ड"
    },

    "crop_health_analysis": {
        "en": "Crop Health Analysis",
        "te": "పంట ఆరోగ్య విశ్లేషణ",
        "hi": "फसल स्वास्थ्य विश्लेषण"
    },

    "weather_advisory": {
        "en": "Weather & Advisory",
        "te": "వాతావరణం & సలహాలు",
        "hi": "मौसम और सलाह"
    },

    "my_reports": {
        "en": "My Reports",
        "te": "నా నివేదికలు",
        "hi": "मेरी रिपोर्ट"
    },

    "state_dashboard": {
        "en": "State Agritech Dashboard",
        "te": "రాష్ట్ర అగ్రిటెక్ డ్యాష్‌బోర్డ్",
        "hi": "राज्य एग्रीटेक डैशबोर्ड"
    },


    # =====================================================
    # WORKFLOW
    # =====================================================

    "step_location_crop": {
        "en": "Location & Crop",
        "te": "ప్రాంతం & పంట",
        "hi": "स्थान और फसल"
    },

    "step_weather": {
        "en": "Weather & Advisory",
        "te": "వాతావరణం & సలహాలు",
        "hi": "मौसम और सलाह"
    },

    "step_upload": {
        "en": "Upload Leaf Photo",
        "te": "ఆకు ఫోటో అప్‌లోడ్ చేయండి",
        "hi": "पत्ती की फोटो अपलोड करें"
    },

    "step_action_plan": {
        "en": "Action Plan",
        "te": "చర్యల ప్రణాళిక",
        "hi": "कार्य योजना"
    },


    "step_location_description": {
        "en": "Select your district, local area, and crop.",
        "te": "మీ జిల్లా, ప్రాంతం మరియు పంటను ఎంచుకోండి.",
        "hi": "अपना जिला, स्थानीय क्षेत्र और फसल चुनें।"
    },

    "step_weather_description": {
        "en": "Check local weather conditions and farming guidance.",
        "te": "స్థానిక వాతావరణ పరిస్థితులు మరియు వ్యవసాయ సూచనలను చూడండి.",
        "hi": "स्थानीय मौसम और कृषि सलाह देखें।"
    },

    "step_upload_description": {
        "en": "Upload a clear image of the affected plant.",
        "te": "ప్రభావిత మొక్క యొక్క స్పష్టమైన చిత్రాన్ని అప్‌లోడ్ చేయండి.",
        "hi": "प्रभावित पौधे की स्पष्ट तस्वीर अपलोड करें।"
    },

    "step_action_description": {
        "en": "Review the predicted issue and recommended next steps.",
        "te": "గుర్తించిన సమస్య మరియు సూచించిన తదుపరి చర్యలను పరిశీలించండి.",
        "hi": "पहचानी गई समस्या और सुझाए गए अगले कदम देखें।"
    },


    # =====================================================
    # LOCATION & CROP
    # =====================================================

    "select_location": {
        "en": "Select Location",
        "te": "ప్రాంతాన్ని ఎంచుకోండి",
        "hi": "स्थान चुनें"
    },

    "district": {
        "en": "District",
        "te": "జిల్లా",
        "hi": "जिला"
    },

    "taluka": {
        "en": "Taluka",
        "te": "తాలూకా",
        "hi": "तालुका"
    },

    "crop": {
        "en": "Crop",
        "te": "పంట",
        "hi": "फसल"
    },

    "select_crop": {
        "en": "Select Crop",
        "te": "పంటను ఎంచుకోండి",
        "hi": "फसल चुनें"
    },


    # =====================================================
    # WEATHER
    # =====================================================

    "weather": {
        "en": "Weather",
        "te": "వాతావరణం",
        "hi": "मौसम"
    },

    "temperature": {
        "en": "Temperature",
        "te": "ఉష్ణోగ్రత",
        "hi": "तापमान"
    },

    "humidity": {
        "en": "Humidity",
        "te": "తేమ",
        "hi": "नमी"
    },

    "rainfall": {
        "en": "Rainfall",
        "te": "వర్షపాతం",
        "hi": "वर्षा"
    },

    "weather_status": {
        "en": "Weather Status",
        "te": "వాతావరణ స్థితి",
        "hi": "मौसम की स्थिति"
    },

    "check_weather": {
        "en": "Check Weather & Advisory",
        "te": "వాతావరణం & సలహాలను చూడండి",
        "hi": "मौसम और सलाह देखें"
    },

    "weather_unavailable": {
        "en": "Weather information is currently unavailable.",
        "te": "ప్రస్తుతం వాతావరణ సమాచారం అందుబాటులో లేదు.",
        "hi": "मौसम की जानकारी अभी उपलब्ध नहीं है।"
    },


    # =====================================================
    # IMAGE ANALYSIS
    # =====================================================

    "upload_image": {
        "en": "Upload Leaf Photo",
        "te": "ఆకు ఫోటోను అప్‌లోడ్ చేయండి",
        "hi": "पत्ती की फोटो अपलोड करें"
    },

    "upload_instruction": {
        "en": "Upload a clear photo of the crop leaf.",
        "te": "పంట ఆకుకు సంబంధించిన స్పష్టమైన ఫోటోను అప్‌లోడ్ చేయండి.",
        "hi": "फसल की पत्ती की स्पष्ट फोटो अपलोड करें।"
    },

    "analyze": {
        "en": "Analyze Crop Health",
        "te": "పంట ఆరోగ్యాన్ని విశ్లేషించండి",
        "hi": "फसल स्वास्थ्य का विश्लेषण करें"
    },

    "analyzing": {
        "en": "Analyzing image...",
        "te": "చిత్రాన్ని విశ్లేషిస్తోంది...",
        "hi": "चित्र का विश्लेषण हो रहा है..."
    },

    "analysis_complete": {
        "en": "Analysis completed.",
        "te": "విశ్లేషణ పూర్తయింది.",
        "hi": "विश्लेषण पूरा हो गया।"
    },


    # =====================================================
    # PREDICTION
    # =====================================================

    "prediction": {
        "en": "Prediction",
        "te": "అంచనా",
        "hi": "अनुमान"
    },

    "detected_issue": {
        "en": "Detected Crop Issue",
        "te": "గుర్తించిన పంట సమస్య",
        "hi": "पहचानी गई फसल समस्या"
    },

    "confidence": {
        "en": "Confidence",
        "te": "నమ్మక స్థాయి",
        "hi": "विश्वास स्तर"
    },

    "confidence_high": {
        "en": "High confidence",
        "te": "అధిక నమ్మక స్థాయి",
        "hi": "उच्च विश्वास स्तर"
    },

    "confidence_medium": {
        "en": "Moderate confidence",
        "te": "మధ్యస్థ నమ్మక స్థాయి",
        "hi": "मध्यम विश्वास स्तर"
    },

    "confidence_low": {
        "en": "Low confidence",
        "te": "తక్కువ నమ్మక స్థాయి",
        "hi": "कम विश्वास स्तर"
    },

    "review_image": {
        "en": "Please capture a clearer leaf image and try again.",
        "te": "దయచేసి ఆకుకు మరింత స్పష్టమైన ఫోటో తీసి మళ్లీ ప్రయత్నించండి.",
        "hi": "कृपया पत्ती की अधिक स्पष्ट तस्वीर लेकर फिर प्रयास करें।"
    },


    # =====================================================
    # RISK
    # =====================================================

    "risk": {
        "en": "Risk",
        "te": "ప్రమాద స్థాయి",
        "hi": "जोखिम"
    },

    "risk_score": {
        "en": "Risk Score",
        "te": "ప్రమాద స్కోర్",
        "hi": "जोखिम स्कोर"
    },

    "low_risk": {
        "en": "Low Risk",
        "te": "తక్కువ ప్రమాదం",
        "hi": "कम जोखिम"
    },

    "moderate_risk": {
        "en": "Moderate Risk",
        "te": "మధ్యస్థ ప్రమాదం",
        "hi": "मध्यम जोखिम"
    },

    "high_risk": {
        "en": "High Risk",
        "te": "అధిక ప్రమాదం",
        "hi": "उच्च जोखिम"
    },


    # =====================================================
    # WARNING MESSAGES
    # =====================================================

    "warning": {
        "en": "Warning",
        "te": "హెచ్చరిక",
        "hi": "चेतावनी"
    },

    "high_risk_warning": {
        "en": "Conditions indicate a higher crop health risk. Inspect the field carefully and take appropriate action.",
        "te": "పంట ఆరోగ్యానికి అధిక ప్రమాద పరిస్థితులు కనిపిస్తున్నాయి. పొలాన్ని జాగ్రత్తగా పరిశీలించి తగిన చర్యలు తీసుకోండి.",
        "hi": "परिस्थितियां फसल स्वास्थ्य के लिए अधिक जोखिम का संकेत देती हैं। खेत का सावधानी से निरीक्षण करें और उचित कार्रवाई करें।"
    },

    "emergency_warning": {
        "en": "Emergency outbreak risk warning: the available image, confidence and environmental conditions indicate elevated risk. This is an advisory indicator, not a confirmed outbreak.",
        "te": "అత్యవసర వ్యాధి వ్యాప్తి ప్రమాద హెచ్చరిక: చిత్రం, నమ్మక స్థాయి మరియు పర్యావరణ పరిస్థితులు అధిక ప్రమాదాన్ని సూచిస్తున్నాయి. ఇది సలహా సూచిక మాత్రమే; నిర్ధారిత వ్యాధి వ్యాప్తి కాదు.",
        "hi": "आपातकालीन प्रकोप जोखिम चेतावनी: उपलब्ध तस्वीर, विश्वास स्तर और पर्यावरणीय परिस्थितियां बढ़े हुए जोखिम का संकेत देती हैं। यह केवल एक सलाहकारी संकेतक है, पुष्टि किया गया प्रकोप नहीं।"
    },

    "no_emergency": {
        "en": "No elevated emergency risk detected from the available information.",
        "te": "అందుబాటులో ఉన్న సమాచారం ఆధారంగా అధిక అత్యవసర ప్రమాదం గుర్తించబడలేదు.",
        "hi": "उपलब्ध जानकारी के आधार पर कोई बढ़ा हुआ आपातकालीन जोखिम नहीं पाया गया।"
    },


    # =====================================================
    # ADVISORY
    # =====================================================

    "advisory": {
        "en": "Agricultural Advisory",
        "te": "వ్యవసాయ సలహా",
        "hi": "कृषि सलाह"
    },

    "recommendation": {
        "en": "Recommendation",
        "te": "సిఫార్సు",
        "hi": "सिफारिश"
    },

    "organic": {
        "en": "Organic / Cultural Management",
        "te": "సేంద్రీయ / పంట నిర్వహణ",
        "hi": "जैविक / फसल प्रबंधन"
    },

    "chemical": {
        "en": "Chemical Management",
        "te": "రసాయన నిర్వహణ",
        "hi": "रासायनिक प्रबंधन"
    },

    "prevention": {
        "en": "Prevention",
        "te": "నివారణ",
        "hi": "रोकथाम"
    },

    "next_steps": {
        "en": "Recommended Next Steps",
        "te": "సూచించిన తదుపరి చర్యలు",
        "hi": "सुझाए गए अगले कदम"
    },


    # =====================================================
    # DOSAGE
    # =====================================================

    "dosage": {
        "en": "Dosage Calculator",
        "te": "మోతాదు కాలిక్యులేటర్",
        "hi": "मात्रा कैलकुलेटर"
    },

    "farm_area": {
        "en": "Farm Area",
        "te": "పొలం విస్తీర్ణం",
        "hi": "खेत का क्षेत्रफल"
    },

    "pump_capacity": {
        "en": "Pump Capacity",
        "te": "పంపు సామర్థ్యం",
        "hi": "पंप क्षमता"
    },

    "rate": {
        "en": "Label Rate",
        "te": "లేబుల్ మోతాదు",
        "hi": "लेबल मात्रा"
    },

    "calculate": {
        "en": "Calculate",
        "te": "లెక్కించండి",
        "hi": "गणना करें"
    },

    "result": {
        "en": "Result",
        "te": "ఫలితం",
        "hi": "परिणाम"
    },


    # =====================================================
    # AUDIO
    # =====================================================

    "audio": {
        "en": "Listen to Advisory",
        "te": "సలహాను వినండి",
        "hi": "सलाह सुनें"
    },

    "audio_unavailable": {
        "en": "Audio is currently unavailable. Please read the advisory on screen.",
        "te": "ప్రస్తుతం ఆడియో అందుబాటులో లేదు. దయచేసి స్క్రీన్‌పై ఉన్న సలహాను చదవండి.",
        "hi": "ऑडियो अभी उपलब्ध नहीं है। कृपया स्क्रीन पर दी गई सलाह पढ़ें।"
    },

    "generating_audio": {
        "en": "Preparing audio...",
        "te": "ఆడియో సిద్ధం చేస్తోంది...",
        "hi": "ऑडियो तैयार किया जा रहा है..."
    },


    # =====================================================
    # REPORTS
    # =====================================================

    "reports": {
        "en": "Reports",
        "te": "నివేదికలు",
        "hi": "रिपोर्ट"
    },

    "save_report": {
        "en": "Save Anonymous Report",
        "te": "అనామక నివేదికను సేవ్ చేయండి",
        "hi": "गुमनाम रिपोर्ट सहेजें"
    },

    "report_saved": {
        "en": "Anonymous report saved successfully.",
        "te": "అనామక నివేదిక విజయవంతంగా సేవ్ చేయబడింది.",
        "hi": "गुमनाम रिपोर्ट सफलतापूर्वक सहेजी गई।"
    },

    "no_reports": {
        "en": "No reports are available yet.",
        "te": "ఇంకా నివేదికలు అందుబాటులో లేవు.",
        "hi": "अभी कोई रिपोर्ट उपलब्ध नहीं है।"
    },


    # =====================================================
    # DASHBOARD
    # =====================================================

    "current_farm_overview": {
        "en": "Current Farm Overview",
        "te": "ప్రస్తుత పొలం వివరాలు",
        "hi": "वर्तमान खेत का अवलोकन"
    },

    "selected_location": {
        "en": "Selected Location",
        "te": "ఎంచుకున్న ప్రాంతం",
        "hi": "चयनित स्थान"
    },

    "selected_crop": {
        "en": "Selected Crop",
        "te": "ఎంచుకున్న పంట",
        "hi": "चयनित फसल"
    },

    "crop_health": {
        "en": "Crop Health",
        "te": "పంట ఆరోగ్యం",
        "hi": "फसल स्वास्थ्य"
    },

    "awaiting_scan": {
        "en": "Awaiting Scan",
        "te": "స్కాన్ కోసం వేచి ఉంది",
        "hi": "स्कैन की प्रतीक्षा"
    },

    "not_checked": {
        "en": "Not Checked",
        "te": "ఇంకా తనిఖీ చేయలేదు",
        "hi": "जांच नहीं की गई"
    },


    # =====================================================
    # SYSTEM STATUS
    # =====================================================

    "system_status": {
        "en": "System Status",
        "te": "సిస్టమ్ స్థితి",
        "hi": "सिस्टम स्थिति"
    },

    "service_available": {
        "en": "Service available",
        "te": "సేవ అందుబాటులో ఉంది",
        "hi": "सेवा उपलब्ध है"
    },

    "service_unavailable": {
        "en": "Service unavailable",
        "te": "సేవ అందుబాటులో లేదు",
        "hi": "सेवा उपलब्ध नहीं है"
    },

    "information": {
        "en": "Information",
        "te": "సమాచారం",
        "hi": "जानकारी"
    },


    # =====================================================
    # SAFETY / DISCLAIMER
    # =====================================================

    "disclaimer": {
        "en": "AI results are advisory indicators and should not be treated as a confirmed diagnosis. Confirm treatment decisions with approved agricultural guidance and product labels.",
        "te": "AI ఫలితాలు సలహా సూచికలు మాత్రమే; వాటిని నిర్ధారిత వ్యాధి నిర్ధారణగా పరిగణించకండి. చికిత్స నిర్ణయాలను ఆమోదించబడిన వ్యవసాయ మార్గదర్శకాలు మరియు ఉత్పత్తి లేబుళ్లతో నిర్ధారించుకోండి.",
        "hi": "AI परिणाम केवल सलाहकारी संकेतक हैं और इन्हें पुष्टि किए गए रोग निदान के रूप में नहीं माना जाना चाहिए। उपचार संबंधी निर्णयों की पुष्टि अनुमोदित कृषि सलाह और उत्पाद लेबल के अनुसार करें।"
    },

    "chemical_warning": {
        "en": "Never use a pesticide dose generated by AI. Follow the approved product label and local agricultural guidance.",
        "te": "AI సూచించిన పురుగుమందు మోతాదును స్వయంగా ఉపయోగించవద్దు. ఆమోదించబడిన ఉత్పత్తి లేబుల్ మరియు స్థానిక వ్యవసాయ మార్గదర్శకాలను అనుసరించండి.",
        "hi": "AI द्वारा सुझाई गई कीटनाशक मात्रा का स्वयं उपयोग न करें। अनुमोदित उत्पाद लेबल और स्थानीय कृषि सलाह का पालन करें।"
    },


    # =====================================================
    # COMMON ACTIONS
    # =====================================================

    "start_analysis": {
        "en": "Start Crop Health Analysis",
        "te": "పంట ఆరోగ్య విశ్లేషణ ప్రారంభించండి",
        "hi": "फसल स्वास्थ्य विश्लेषण शुरू करें"
    },

    "continue": {
        "en": "Continue",
        "te": "కొనసాగించండి",
        "hi": "जारी रखें"
    },

    "back": {
        "en": "Back",
        "te": "వెనుకకు",
        "hi": "वापस"
    },

    "retry": {
        "en": "Try Again",
        "te": "మళ్లీ ప్రయత్నించండి",
        "hi": "फिर प्रयास करें"
    },

    "close": {
        "en": "Close",
        "te": "మూసివేయండి",
        "hi": "बंद करें"
    }
}


# =========================================================
# TRANSLATION HELPER
# =========================================================

SUPPORTED_LANGUAGES = {
    "English": "en",
    "Telugu": "te",
    "Hindi": "hi"
}


def get_language_code(language):
    """
    Convert a language name or language code into the
    internal language code.

    Examples:
        English -> en
        Telugu  -> te
        Hindi   -> hi
        en      -> en
    """

    if not language:
        return "en"

    language = str(language).strip()

    if language in SUPPORTED_LANGUAGES:
        return SUPPORTED_LANGUAGES[language]

    language_code = language.lower()

    if language_code in ("en", "te", "hi"):
        return language_code

    return "en"


def t(key, language="en"):
    """
    Return a translated string.

    If:
        - the key does not exist, or
        - the requested language is unavailable

    the function safely falls back to English.

    Example:
        t("analyze", "te")
    """

    language_code = get_language_code(language)

    translation = TRANSLATIONS.get(key)

    if not translation:
        return key

    return translation.get(
        language_code,
        translation.get("en", key)
    )


def get_all_translations(key):
    """
    Return all available translations for a specific key.

    Example:
        {
            "en": "...",
            "te": "...",
            "hi": "..."
        }
    """

    translation = TRANSLATIONS.get(key)

    if not translation:
        return {}

    return translation.copy()


def is_supported_language(language):
    """
    Check whether a language is supported.
    """

    if not language:
        return False

    language_code = get_language_code(language)

    return language_code in {
        "en",
        "te",
        "hi"
    }