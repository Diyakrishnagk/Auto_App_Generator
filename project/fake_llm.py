import google.generativeai as genai
import json

#  Put your key here (later move to .env)
API_KEY = "YOUR_API_KEY"


# -------------------------------
#  GEMINI CALL (WITH RETRY)
# -------------------------------
def call_gemini(prompt, retries=2):
    for attempt in range(retries):
        try:
            genai.configure(api_key=AQ.Ab8RN6KaYxnx1Flnfkn3FSYP2-jEILt1jKA7dl30cD2zIkGHGw)

            model = genai.GenerativeModel("gemini-1.5-flash")

            # 🔥 Force structured output
            full_prompt = f"""
            Convert the following app description into JSON format with keys:
            entities, features, roles.

            Prompt: {prompt}

            Example:
            {{
                "entities": ["students"],
                "features": ["login", "dashboard"],
                "roles": ["admin", "user"]
            }}
            """

            response = model.generate_content(full_prompt)

            return {
                "source": "gemini",
                "text": response.text
            }

        except Exception as e:
            print(f"[Gemini Attempt {attempt+1}] Failed:", str(e))

    return None


# -------------------------------
#  PARSE RESPONSE SAFELY
# -------------------------------
def parse_response(text):
    try:
        return json.loads(text)
    except Exception:
        print("⚠️ Failed to parse Gemini JSON, using fallback structure")
        return None


# -------------------------------
#  FALLBACK FAKE LLM
# -------------------------------
def fake_response(prompt):
    return {
        "source": "fake_llm",
        "entities": ["students"],
        "features": ["login", "dashboard"],
        "roles": ["admin", "user"]
    }


# -------------------------------
#  MAIN GENERATE FUNCTION
# -------------------------------
def generate(prompt):
    gemini_result = call_gemini(prompt)

    if gemini_result:
        structured = parse_response(gemini_result["text"])

        if structured:
            structured["source"] = "gemini"
            return structured

    #  fallback if anything fails
    return fake_response(prompt)