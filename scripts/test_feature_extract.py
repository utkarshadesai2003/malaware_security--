from app.feature_extractor import extract_features

path = "notepad.exe"  # replace with your actual .exe file path

features = extract_features(path)
print("Extracted features:", features)
