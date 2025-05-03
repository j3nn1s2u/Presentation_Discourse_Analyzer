# Presentation Discourse Analyzer (PDA)

A lightweight NLP-based tool that helps analyze student presentation scripts or written reports by classifying each paragraph into rhetorical sections such as Opening, Background, Value Creation, Marketing 4Ps, Action Ideas, and Closing.

---

## 🔍 Project Objective
This tool was developed as part of a self-learning journey into NLP for applying to the Computational Linguistics Master's program. The goal is to demonstrate:
- Technical adaptability despite no prior background in NLP
- Applied English & Linguistics knowledge in discourse structure
- Capability to complete an end-to-end NLP mini-project

---

## 💡 Features
- Paragraph segmentation and pre-cleaning
- Rule-based paragraph classification (no ML required)
- Easy-to-read JSON output for review and further evaluation

---

## 🛠️ Installation
```bash
# Clone the repository
$ git clone https://github.com/yourusername/Presentation_Discourse_Analyzer.git

# Move into project folder
$ cd Presentation_Discourse_Analyzer

# (Optional) Create a virtual environment
$ python -m venv venv
$ source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install required libraries
$ pip install -r requirements.txt
```

---

## 🚀 Usage
```bash
# Run the analyzer on input.txt
$ python main.py
```

Make sure you place your input text file inside the `inputs/` folder.

---

## 📁 Output
- The program will output a file: `outputs/classified_paragraphs.json`
- Sample output format:
```json
[
  { "paragraph": "Hello everyone...", "label": "Opening" },
  { "paragraph": "This campaign started in...", "label": "Background" }
]
```

---

## 📈 Optional Enhancements
- Add visualizations of label frequency
- Export to `.xlsx` or `.csv`
- Deploy as a simple web tool

---

## 🙋‍♀️ Author's Note
This tool was developed as a beginner-friendly NLP project without relying on complex machine learning or external APIs. It is designed to be extensible and showcases both learning progress and technical motivation.

---

## 📄 License
MIT License
