if __name__ == '__main__':
    n = int(input())
    scores = map(int, input().split())
     # Remove duplicates and sort the scores in descending order
    unique_scores = sorted(set(scores), reverse=True)
    # Print the runner-up score
    print(unique_scores[1])
