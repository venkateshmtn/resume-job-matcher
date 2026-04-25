def build_prompt(context, job_desc):
    return f"""
You are an AI Resume Matcher.

TASK:
Compare the resume with the job description and extract ONLY relevant technical skills.

STRICT RULES:
- DO NOT explain anything
- DO NOT write sentences or paragraphs
- DO NOT copy text from resume or job description
- ONLY extract skills (e.g., Python, SQL, Machine Learning, TensorFlow)
- IGNORE soft skills and company descriptions
- DO NOT use placeholders like "skill 1", "skill 2"

OUTPUT FORMAT (FOLLOW EXACTLY):

Match Score: <number>%

Matched Skills:
• skill
• skill

Missing Skills:
• skill
• skill

Final Verdict:
• one short line

----------------------

Resume:
{context}

Job Description:
{job_desc}

----------------------

ONLY RETURN FINAL STRUCTURED OUTPUT:
"""