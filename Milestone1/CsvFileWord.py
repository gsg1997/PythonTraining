import pandas as pd
import re
from collections import Counter

try:
    # Read the CSV file into a DataFrame
    Filepath = r"C:\Users\Administrator\Pictures\UST Trainining\Milestone1\CSVTest.csv"
    df = pd.read_csv(Filepath)

    # Concatenate all text in the 'Title' column into one large string
    CsvText = " ".join(df['Title'].astype(str))

    # Use re.findall to get all words
    words = re.findall(r'\b\w+\b', CsvText)

    # Count the frequency of each word using Counter
    wordCounter = Counter(words)

    # Print the word count result
    print(wordCounter)

except Exception as e:
    
    print("Exception Occurred: " + str(e))
