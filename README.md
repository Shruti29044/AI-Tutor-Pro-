# README for AI Tutor Pro (Hugging Face Inference API Version)

## Project Overview
AI Tutor Pro is an intelligent learning platform that uses advanced AI models to generate personalized educational explanations for students. This version is fully compatible with Google Colab, uses free open-source models hosted on Hugging Face, and requires no GPU resources locally.

## Features
- ✅ Interactive Gradio-based web interface
- ✅ Hugging Face hosted model (`Mistral-7B-Instruct-v0.2`) for high-quality explanations
- ✅ No OpenAI API key required
- ✅ 100% Colab friendly
- ✅ Simple database integration using SQLite (in-memory)

## Requirements
- Google Colab account (or local machine with Python)
- Hugging Face account (free-tier available)
- Hugging Face Inference API Key

## Setup Instructions

### 1️⃣ Clone or copy the code into a Google Colab notebook.

### 2️⃣ Install dependencies (already included in the Colab code):
```bash
!pip install sqlalchemy pydantic gradio requests
```

### 3️⃣ Get a Hugging Face Inference API Key:
- Go to: https://huggingface.co/settings/tokens
- Create a new token.
- Free-tier quotas are available for small-scale usage.

### 4️⃣ Replace API Key in Code:
Replace the placeholder in this line with your actual key:
```python
huggingface_api_key = "hf_REPLACE_WITH_YOUR_HUGGING_FACE_API_KEY"
```

### 5️⃣ Run the notebook.
- The Gradio UI will launch.
- Enter any topic and difficulty level.
- The AI will generate custom explanations using the hosted model.

---

## Model Used
- **Model:** `mistralai/Mistral-7B-Instruct-v0.2`
- **Provider:** Hugging Face Inference API
- **License:** Open source, commercial-use friendly.

---

## Limitations
- This version depends on Hugging Face Inference API quotas.
- Response speed may vary based on server load.
- No webcam or real-time emotion detection included (can be extended).

---

## Future Improvements (Optional Extensions)
- Add user authentication
- Track student progress and profile data
- Add Reinforcement Learning agent for adaptive difficulty adjustment
- Add realtime CV (engagement detection)
- Deployment-ready Dockerfile

---

## Contact & Credits
- Project: **AI Tutor Pro (Colab Edition)**
- AI Model Credits: Hugging Face & Mistral AI

---

## License
This project is provided for educational and prototyping purposes only.

---

# End of README
