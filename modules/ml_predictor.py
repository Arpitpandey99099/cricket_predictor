from sklearn.ensemble import RandomForestClassifier

def train_and_predict(df):
    if df is None or df.empty:
        print("\n[ERROR] No data found! Please Load Data (Option 1) first.")
        return

    print("\n[INFO] Training Machine Learning Model...")
    
    # Selecting numerical features for prediction
    X = df[['matches_played', 'runs_scored', 'strike_rate', 'average', 'recent_form_score']]
    y = df['next_match_performance']

    # Training a basic RandomForest Model
    model = RandomForestClassifier(n_estimators=10, random_state=42)
    model.fit(X, y)

    print("[SUCCESS] Model trained successfully!")
    print("\n[PREDICTIONS ON CURRENT ROSTER]")
    print("-" * 45)
    
    predictions = model.predict(X)
    for i, player in enumerate(df['player_name']):
        print(f"{player} -> Predicted Next Match Form: {predictions[i]}")
    print("-" * 45)