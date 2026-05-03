import re

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def process_file():
    with open("sample_input.txt", "r") as f:
        lines = f.readlines()

    cleaned = [clean_text(line) for line in lines if line.strip()]

    with open("sample_output.txt", "w") as f:
        for line in cleaned:
            f.write(line + "\n")

if __name__ == "__main__":
    process_file()
