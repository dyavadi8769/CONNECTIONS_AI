from transformers import pipeline
import numpy as np
import random

# Initialize the zero-shot classification pipeline with a well-trained model
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

def classify_and_group_words(words, labels=["Action", "Object", "Concept", "Place"], target_group_size=4):
    """
    Classifies each word to one of four dynamic groups using zero-shot classification.
    """
    grouped_words = {label: [] for label in labels}
    
    # Classify each word into one of the four groups
    for word in words:
        result = classifier(word, candidate_labels=labels)
        best_label = result['labels'][0]  # Get the label with the highest confidence score
        print(f"Classifying word: {word}, Best label: {best_label}, Confidence: {result['scores'][0]}")
        grouped_words[best_label].append(word)
    
    # Filter out groups to ensure each has the target group size
    valid_groups = [group for group in grouped_words.values() if len(group) == target_group_size]

    print("Valid groups formed by classifier:", valid_groups)
    
    # If fewer than 4 groups of the required size, use a fallback
    if len(valid_groups) < 4:
        print("Insufficient valid groups, using fallback guesses...")
        valid_groups.extend(fallback_guess(words, valid_groups))
    
    return valid_groups[:4]  # Ensure exactly 4 groups

def fallback_guess(words, previous_guesses):
    """
    Generates a fallback guess by randomly selecting groups of 4 from available words.
    """
    available_words = [word for word in words if sorted(word) not in previous_guesses]
    random.shuffle(available_words)
    fallback_groups = [available_words[i:i + 4] for i in range(0, len(available_words), 4)]
    fallback_groups = [group for group in fallback_groups if len(group) == 4]
    print("Generated fallback groups:", fallback_groups)
    return fallback_groups

def model(words, strikes, isOneAway, correctGroups, previousGuesses, error):
    try:
        print("Model input words:", words)
        
        # Step 1: Classify and group words using zero-shot classification
        all_groups = classify_and_group_words(words)
        
        # Step 2: Filter out already guessed groups
        possible_guesses = [group for group in all_groups if sorted(group) not in previousGuesses]
        print("Possible guesses after filtering:", possible_guesses)
        
        # Step 3: If no valid guesses from classification, use fallback guessing
        if not possible_guesses:
            possible_guesses = fallback_guess(words, previousGuesses)

        # Select the best guess
        best_guess = possible_guesses[0] if possible_guesses else ["default_word1", "default_word2", "default_word3", "default_word4"]

        # Handle "one away" condition by substituting words if necessary
        if isOneAway and best_guess:
            best_guess = adjust_one_away_guess(best_guess, correctGroups, words)

        # Decide whether to end the turn
        endTurn = strikes >= 4 or not best_guess

        print("Final guess for this round:", best_guess)
        return best_guess, endTurn

    except Exception as e:
        # Return default guess to avoid empty response
        print("Error in model function:", e)
        return ["default_word1", "default_word2", "default_word3", "default_word4"], True

def adjust_one_away_guess(guess, correctGroups, words):
    """
    Adjust the guess if it is one word away from being correct by trying alternative words.
    """
    for correct_group in correctGroups:
        for i, word in enumerate(guess):
            modified_guess = guess[:i] + [w for w in words if w not in guess and w not in correct_group][:1] + guess[i+1:]
            if set(modified_guess) != set(guess):  # Ensure we made a change
                return modified_guess
    return guess
