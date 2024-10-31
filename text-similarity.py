import argparse
import csv
import difflib

# Set the confidence score
CONFIDENT_SCORE = 70

def calculate_similarity2(word1, word2):
    similarity_ratio = difflib.SequenceMatcher(None, word1, word2).ratio()
    return similarity_ratio

def main():
    parser = argparse.ArgumentParser(description="Calculate text similarity from a CSV file.")
    parser.add_argument("csv_file", help="Path to the input CSV file")
    args = parser.parse_args()

    with open(args.csv_file, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            FLAG = 'N'
            if len(row) < 2:
                continue
            # FirstName Colums
            word1, word2 = row[0], row[2]
            # LastName Colums
            word3, word4 = row[1], row[3]
            # Compare the similarity between two FirstName
            similarity_ratio1 = calculate_similarity2(word1, word2)
            # Compare the similarity between two LastName
            similarity_ratio2 = calculate_similarity2(word3, word4)
            similarity_percentage1 = similarity_ratio1  * 100
            similarity_percentage2 = similarity_ratio2  * 100
            average_similarity = (similarity_percentage1 + similarity_percentage2) / 2
            if average_similarity > CONFIDENT_SCORE:
                FLAG = 'Y'
            print(f"{row[0]},{row[1]},{row[2]},{row[3]},{FLAG},{average_similarity:.2f}%")

if __name__ == "__main__":
    main()