import streamlit as st
from scorer import score_resume
from parser import parse_pdf, parse_docx


st.set_page_config(page_title="AI Resume Scorer")

st.title("📄 AI Resume Scorer")
st.write("Upload your resume and (optionally) a job description to get an AI-based score and feedback.")


uploaded_resume = st.file_uploader("Upload resume (PDF or DOCX)", type=["pdf", "docx"])
job_description = st.text_area("Paste Job Description (optional)")


if st.button("Score Resume") and uploaded_resume is not None:

    file_type = uploaded_resume.name.split(".")[-1]

    if file_type == "pdf":
        resume_text = parse_pdf(uploaded_resume)
    else:
        resume_text = parse_docx(uploaded_resume)

    with st.spinner("Analyzing resume with AI..."):
        result = score_resume(resume_text, job_description)

    st.subheader("Evaluation Result")
    st.json(result)
