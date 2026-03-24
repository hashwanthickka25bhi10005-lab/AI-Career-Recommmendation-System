def analyze_resume(text):
    text = text.lower()

    if "coding" in text or "programming" in text:
        return "Software Engineer"
    elif "design" in text:
        return "Designer"
    elif "management" in text:
        return "Manager"
    else:
        return "General Career"
