import re
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")  # expects environment variable OPENAI_API_KEY


def score_resume(resume_text, job_description=None):
    """
    Uses an LLM to evaluate resume quality and job match.
    Returns structured evaluation text.
    """

    prompt = f"""
You are an expert ATS resume evaluator for recruiters.

Evaluate the following resume. If a job description is provided,
compare the resume to it and score relevance.

Resume:
{resume_text}

Job Description (if any):
{job_description}

Respond ONLY in this JSON format:

{{
  "overall_score": 0-100,
  "ats_score": 0-100,
  "keyword_match": 0-100,
  "missing_keywords": [],
  "strengths": [],
  "weaknesses": [],
  "improvement_suggestions": [],
  "rewrite_examples": []
}}
    """

    response = openai.ChatCompletion.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )

    return response.choices[0].message.content
