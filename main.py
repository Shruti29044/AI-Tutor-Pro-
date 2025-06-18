# 100% COLAB FRIENDLY AI Tutor Pro (Hugging Face version - No OpenAI API key needed)

# Install dependencies (only for Colab cells)
!pip install sqlalchemy pydantic gradio transformers accelerate

# Load environment variables securely (OPTIONAL)
import os

# DATABASE SETUP (SQLite in-memory for Colab)
from sqlalchemy import create_engine, Column, Integer, String, DateTime, JSON
from sqlalchemy.orm import declarative_base, sessionmaker
import datetime

SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

Base.metadata.create_all(bind=engine)

# Pydantic Schemas
from pydantic import BaseModel
class UserCreate(BaseModel):
    username: str
    email: str

# CRUD Example (for demo purpose)
from sqlalchemy.orm import Session

def create_user(db: Session, user: UserCreate):
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# NLP SERVICE using Hugging Face Transformers (No OpenAI Key required)
from transformers import pipeline

# Use small open-source model for educational explanation generation
# You can replace this with more powerful models on Hugging Face if desired
model_name = "google/flan-t5-large"  # Small enough to run on Colab

# Initialize pipeline
generator = pipeline("text2text-generation", model=model_name, device_map="auto")

def generate_explanation(prompt: str):
    try:
        response = generator(prompt, max_new_tokens=300, temperature=0.7)
        return response[0]['generated_text']
    except Exception as e:
        return f"Error: {str(e)}"

# GRADIO UI (fully Colab-friendly)
import gradio as gr

def gradio_explain(topic, difficulty):
    full_prompt = f"Explain {topic} to a {difficulty} level student."
    return generate_explanation(full_prompt)

gr.Interface(
    fn=gradio_explain,
    inputs=[gr.Textbox(label="Topic"), gr.Dropdown(choices=["beginner", "intermediate", "advanced"], label="Difficulty")],
    outputs="text",
    title="AI Tutor Pro - 100% Colab Version (Hugging Face Model)"
).launch(share=True)

# COMPLETELY REMOVED:
# - OpenAI API dependencies (No key needed)
# - OpenAI Key tester (no longer necessary)
# This version works fully for free using open-source models directly on Colab!
