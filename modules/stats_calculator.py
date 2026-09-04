def calculate_team_stats(df):
    if df is None or df.empty:
        print("\n[ERROR] No data found! Please Load Data (Option 1) first.")
        return

    avg_strike_rate = df['strike_rate'].mean()
    top_scorer = df.loc[df['runs_scored'].idxmax()]['player_name']
    
    print("\n[FRANCHISE STATISTICS]")
    print("-" * 45)
    print(f"Average Team Strike Rate: {avg_strike_rate:.2f}")
    print(f"Top Run Scorer: {top_scorer}")
    print("-" * 45)