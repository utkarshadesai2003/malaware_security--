import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

# Load dataset
df = pd.read_csv("data/PE_Dataset_Labeled.csv")

# Drop missing values
df.dropna(inplace=True)

# Convert HEX columns to integers
hex_columns = ["Address_of_Entry_Point", "Image_Base", "Checksum", "DLL_Characteristics", "File_Alignment"]

for col in hex_columns:
    df[col] = df[col].apply(lambda x: int(str(x), 16) if isinstance(x, str) and x.startswith("0x") else x)

# Prepare features and labels
X = df[hex_columns]
y = df["Label"]

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

# Evaluate
accuracy = model.score(X_test, y_test)
print(f"✅ Model trained with accuracy: {accuracy * 100:.2f}%")

# Save model
joblib.dump(model, "models/malware_model.pkl")
print("✅ Model saved as malware_model.pkl")
