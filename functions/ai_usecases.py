from flask import Flask, request, jsonify

app = Flask(__name__)

# Predefined use case logic
USE_CASES = {
    "Retail": {
        "Marketing": [
            "AI-generated personalized ad campaigns",
            "Demand forecasting with generative AI",
            "Customer sentiment analysis from reviews",
        ],
        "Operations": [
            "AI-powered inventory optimization",
            "Generative AI for supply chain simulation",
            "Chatbots for supplier communication",
        ],
    },
    "Healthcare": {
        "R&D": [
            "AI for molecule discovery",
            "Synthetic data for clinical trials",
            "Medical imaging enhancement",
        ],
        "Operations": [
            "Patient engagement via chatbots",
            "Generative AI for medical records summarization",
            "Predictive analytics for resource allocation",
        ],
    },
}

@app.route('/.netlify/functions/ai_usecases', methods=['POST'])
def get_usecases():
    data = request.json
    country = data.get("country")
    industry = data.get("industry")
    business_function = data.get("businessFunction")

    # Fetch relevant use cases
    usecases = USE_CASES.get(industry, {}).get(business_function, ["No relevant use cases found."])
    
    return jsonify({"usecases": usecases})

# For local testing
if __name__ == "__main__":
    app.run(debug=True)
