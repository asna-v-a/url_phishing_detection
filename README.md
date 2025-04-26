# 📄 URL Phishing Detection using Machine Learning

🔎 A machine learning model to detect phishing URLs by analyzing URL-based features and patterns. Deployed as an interactive web application using Streamlit for real-time prediction.

---

## 📌 Problem Statement
Phishing attacks through fake websites are a major cybersecurity threat.  
This project aims to automatically classify URLs as either **legitimate** or **phishing** using a machine learning model trained on extracted URL features.

---

## 📊 Dataset and Feature Engineering
The dataset used for this project contains over **20,000 labeled URLs**, classified as either **phishing** or **legitimate**. Below is a list of features used in the model:

### Key Features:
- **`domain_length`**: Length of the domain name (e.g., 'example.com').
- **`is_trusted_domain`**: A binary feature indicating whether the domain is from a trusted source (True/False).
- **`subdomain_count`**: The number of subdomains in the URL (e.g., 'sub.example.com').
- **`has_www`**: Indicates whether the URL contains the 'www' prefix (True/False).
- **`url_length`**: The total length of the entire URL string.
- **`path_length`**: Length of the path in the URL (e.g., 'example.com/path/to/page').
- **`query_length`**: Length of the query string in the URL (e.g., 'example.com/search?q=hello').
- **`fragment_length`**: Length of the fragment identifier in the URL (e.g., 'example.com/#section').
- **`path_depth`**: Depth of the URL path (number of slashes in the path).
- **`dots_count`**: Count of dots (.) in the URL, indicating multiple subdomains or special URL formatting.
- **`digits_count`**: Count of digits in the URL, which may signal suspicious activity.
- **`special_chars_count`**: Number of special characters (e.g., '-', '_', '&', '%') in the URL.
- **`has_ip_address`**: Boolean feature indicating whether the URL contains an IP address.
- **`has_at_symbol`**: Boolean feature indicating if the URL contains the '@' symbol, often used in phishing URLs.
- **`has_double_slash`**: Boolean feature indicating if the URL contains a double slash ('//'), which can be indicative of a phishing attempt.
- **`has_dash_in_domain`**: Boolean feature indicating if the domain name contains a dash ('-').
- **`has_https`**: Indicates whether the URL starts with 'https' (True/False).
- **`has_suspicious_words`**: Boolean feature indicating the presence of suspicious keywords (e.g., 'free', 'update', 'verify') in the URL.
- **`excessive_subdomains`**: Binary feature indicating whether the URL contains an unusually high number of subdomains.
- **`suspicious_tld`**: Indicates whether the URL contains a suspicious top-level domain (TLD) (e.g., '.xyz', '.top').
- **`Labels`**: Target variable, where '0' indicates a legitimate URL and '1' indicates a phishing URL.

---

## ⚙️ Approach
- **Data Preprocessing:** Cleaned and standardized URL features.
- **Feature Engineering:** Extracted meaningful attributes from URLs to improve prediction performance.
- **EDA:** Performed exploratory data analysis and visualized patterns using Matplotlib and Seaborn.
- **Model Building:**
  - Trained a **Random Forest Classifier** achieving 96.2% accuracy.
  - Compared multiple models (Logistic Regression, SVM, Decision Tree, XGBoost).
- **Model Evaluation:**
  - Confusion Matrix, ROC Curve, and Precision-Recall Curve were plotted.
- **Deployment:**
  - Deployed the trained model via a **Streamlit** app for real-time URL phishing detection.

---

## 🏆 Results
- **Random Forest Classifier:** 96.2% Accuracy
- **ROC AUC Score:** 0.97
- **Highlights:**
  - Strong precision and recall for both legitimate and phishing URLs.
  - Balanced performance across classes.

### 📈 Key Metrics:
| Metric                | Score |
|------------------------|-------|
| Accuracy               | 96.2% |
| Precision (Legitimate) | 0.97  |
| Recall (Legitimate)    | 0.96  |
| Precision (Phishing)   | 0.96  |
| Recall (Phishing)      | 0.97  |

**Visualizations:**
- Confusion Matrix
- Precision-Recall 

---

## 🚀 Future Work
- Enhance feature engineering using advanced domain-based and NLP-based features.
- Extend detection capability to newly emerging phishing tactics and new TLDs (.top, .xyz).
- Deploy an API service for large-scale phishing URL scanning.

---

## 🛠️ Tech Stack
- Python
- Scikit-learn
- Pandas
- Matplotlib, Seaborn
- Streamlit

---

## 🗂️ Project Structure
```bash
/notebooks
    └── url_phishing_detection.ipynb  # EDA, feature engineering, model training
/data
    └── phishing_data.csv             # Dataset
/models
    └── phishing_detector.pkl         # Saved machine learning model
/streamlit_app
    └── app.py                        # Streamlit web app for real-time prediction
README.md                             # Project documentation
requirements.txt                      # Python dependencies
```

---

## 📥 Installation & Run Instructions
```bash
# 1. Clone the repository
git clone https://github.com/yourusername/url-phishing-detection.git
cd url-phishing-detection

# 2. Install dependencies
pip install -r requirements.txt

# 3. Launch the Streamlit app
streamlit run streamlit_app/app.py
```

## 🤝 Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request.

---

Let me know if you’d like me to refine anything else or add more details! 
