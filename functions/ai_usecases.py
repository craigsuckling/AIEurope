from flask import Flask, request, jsonify

app = Flask(__name__)

# Comprehensive use case dictionary
USE_CASES = {
    "Retail": {
        "Marketing": [
            "AI-generated personalized ad campaigns",
            "Demand forecasting using generative AI",
            "Customer sentiment analysis from reviews",
        ],
        "Operations": [
            "AI-powered inventory optimization",
            "Generative AI for supply chain simulation",
            "Virtual assistants for supplier communication",
        ],
        "Sales": [
            "Chatbots for customer interaction",
            "AI-powered product recommendation engines",
            "Dynamic pricing optimization using AI models",
        ],
    },
    "Healthcare": {
        "R&D": [
            "AI for molecule discovery",
            "Synthetic data for clinical trials",
            "Generative models for protein structure prediction",
        ],
        "Operations": [
            "Patient engagement via chatbots",
            "Summarizing medical records with generative AI",
            "Predictive analytics for resource allocation",
        ],
        "Clinical Practice": [
            "Automated transcription for patient consultations",
            "Medical imaging enhancement with generative AI",
            "AI-generated treatment pathway suggestions",
        ],
    },
    "Finance": {
        "Risk Management": [
            "Fraud detection using generative AI",
            "AI-generated risk scenarios for stress testing",
            "Dynamic credit scoring models",
        ],
        "Customer Service": [
            "Virtual financial assistants for clients",
            "Automated report generation for account reviews",
            "Chatbots for loan processing inquiries",
        ],
        "Product Development": [
            "Generative AI for creating personalized financial products",
            "AI-driven financial forecasting",
            "Market trend analysis using AI models",
        ],
    },
    "Manufacturing": {
        "Production": [
            "AI-generated predictive maintenance schedules",
            "Generative AI for supply chain optimization",
            "Product design prototypes using AI models",
        ],
        "Quality Control": [
            "Automated defect detection in production lines",
            "AI-powered process optimization suggestions",
            "Simulation models for testing new processes",
        ],
        "Logistics": [
            "Route optimization with AI models",
            "Generative AI for warehouse space planning",
            "Dynamic demand and supply balancing algorithms",
        ],
    },
    "Government": {
        "Public Services": [
            "Chatbots for citizen engagement",
            "Automated report summarization for policymakers",
            "Generative AI for urban planning simulations",
        ],
        "Education": [
            "AI-powered curriculum personalization",
            "Automated content creation for e-learning platforms",
            "Generative models for creating training simulations",
        ],
        "Healthcare Policy": [
            "Predictive models for disease outbreak management",
            "Generative AI for resource allocation simulations",
            "Synthesizing anonymized patient datasets for research",
        ],
    },
}

COUNTRY_SPECIFIC_INSIGHTS = {
    "Germany": [
        "Focus on manufacturing use cases due to its industrial base.",
        "Emphasis on quality control and production optimization.",
    ],
    "France": [
        "Strong focus on healthcare and finance sectors.",
        "AI-driven R&D in pharmaceuticals and risk management.",
    ],
    "United Kingdom": [
        "Advanced retail and finance applications.",
        "Generative AI for fraud detection and customer engagement.",
    ],
    "Netherlands": [
        "Logistics and transportation AI solutions.",
        "Focus on sustainable supply chain optimization.",
    ],
    "Sweden": [
        "Sustainability-focused manufacturing use cases.",
        "AI for renewable energy grid management.",
    ],
    "Italy": [
        "AI in luxury retail and fashion design.",
        "Generative AI for personalized marketing campaigns.",
    ],
    "Spain": [
        "Tourism-related AI solutions like travel assistants.",
        "Generative AI for hospitality industry optimization.",
    ],
}

@app.route('/.netlify/functions/ai_usecases', methods=['GET', 'POST'])
def ai_usecases():
    if request.method == 'GET' and request.args.get('getOptions') == 'true':
        # Return dropdown options
        countries = list(COUNTRY_SPECIFIC_INSIGHTS.keys())
        industries = list(USE_CASES.keys())
        business_functions = {industry: list(funcs.keys()) for industry, funcs in USE_CASES.items()}
        return jsonify({"countries": countries, "industries": industries, "businessFunctions": business_functions})

    elif request.method == 'POST':
        # Handle use case recommendations
        data = request.json
        country = data.get("country")
        industry = data.get("industry")
        business_function = data.get("businessFunction")

        # Fetch relevant industry and business function use cases
        usecases = USE_CASES.get(industry, {}).get(business_function, ["No relevant use cases found."])

        # Append country-specific insights if available
        country_insights = COUNTRY_SPECIFIC_INSIGHTS.get(country, [])
        if country_insights:
            usecases.append(f"Country-Specific Insights for {country}:")
            usecases.extend(country_insights)

        return jsonify({"usecases": usecases})

# For local testing
if __name__ == "__main__":
    app.run(debug=True)
