import streamlit as st
import re
from urllib.parse import urlparse
import joblib
import numpy as np

# Preprocessing function for the URL (if needed)
def preprocess_url(url):
    url = url.strip().lower()
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url
    return url

# Extract features from the URL
def get_domain(url):
    parsed = urlparse(url)
    domain = parsed.netloc.lower()
    if domain.startswith('www.'):
        domain = domain[4:]
    return domain

def count_subdomains(domain):
    return len(domain.split('.')) - 1

def has_ip(domain):
    return bool(re.match(r'\d+\.\d+\.\d+\.\d+', domain))

def has_suspicious_words(url):
    suspicious = ['login', 'signin', 'verify', 'secure', 'account', 
                  'update', 'confirm', 'banking', 'password', 'credential']
    return any(word in url.lower() for word in suspicious)

def has_suspicious_tld(domain):
    suspicious_tlds = ['.tk', '.ml', '.ga', '.cf', '.gq', '.xyz']
    return any(domain.endswith(tld) for tld in suspicious_tlds)

def extract_features(url):
    trusted_domains = {
        'google.com', 'youtube.com', 'github.com', 'microsoft.com', 'amazon.com',
        'facebook.com', 'twitter.com', 'linkedin.com', 'apple.com', 'yahoo.com',
        'wikipedia.org', 'instagram.com', 'paypal.com', 'bankofamerica.com', 'chase.com',
        'vimeo.com', 'netflix.com', 'microsoftonline.com', 'dropbox.com', 'slack.com'
    }

    url = preprocess_url(url)
    parsed = urlparse(url)
    domain = get_domain(url)
    
    features = {
        'domain_length': len(domain),
        'is_trusted_domain': int(domain in trusted_domains),
        'subdomain_count': count_subdomains(domain),
        'has_www': int(parsed.netloc.startswith('www.')),
        'url_length': len(url),
        'path_length': len(parsed.path),
        'query_length': len(parsed.query),
        'fragment_length': len(parsed.fragment),
        'path_depth': len([x for x in parsed.path.split('/') if x]),
        'dots_count': domain.count('.'),
        'digits_count': sum(c.isdigit() for c in url),
        'special_chars_count': sum(not c.isalnum() for c in url),
        'has_ip_address': int(has_ip(domain)),
        'has_at_symbol': int('@' in url),
        'has_double_slash': int('//' in parsed.path),
        'has_dash_in_domain': int('-' in domain),
        'has_https': int(url.startswith('https://')),
        'has_suspicious_words': int(has_suspicious_words(url)),
        'excessive_subdomains': int(count_subdomains(domain) > 3),
        'suspicious_tld': int(has_suspicious_tld(domain))
    }
    return features

# Load the trained model (Assuming you have trained and saved it already)
model = joblib.load(r'C:\Users\asnav\OneDrive\Documents\MachineLearningProjects\url_phishing_detection\model\phishing_model.pkl')  # Make sure to save your model first

# Predict function
def predict_url(url):
    features = extract_features(url)
    
    # Convert the dictionary of features into a numpy array
    feature_values = np.array(list(features.values())).reshape(1, -1)  # Reshape for a single sample
    
    result = model.predict(feature_values)[0]
    return "Phishing" if result == 1 else "Legitimate"

# Streamlit UI setup
st.title("Phishing URL Detection")
st.subheader("Enter a URL to check if it's Phishing or Legitimate:")

url_input = st.text_input("Enter URL", "https://www.google.com")
if st.button("Predict"):
    prediction = predict_url(url_input)
    st.write(f"Prediction: **{prediction}**")
