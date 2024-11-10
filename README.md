# CONNECTIONS_AI

## Background
The Connections game from The New York Times (NYT) has become a popular brain teaser, challenging players to associate words based on categories. With advancements in artificial intelligence (AI), the question arises: can we teach AI to recognize categorical patterns? The objective is to develop a bot capable of effectively categorizing a set of words into four distinct groups based on their connections.

## Task
- As a participant we would like you to “solve” this game Connections AI to the best of your abilities. You will be given the board of 16 words arranged randomly, and you will have to select the best 4 words possible that match a group for four distinct groups in order to ensure your success. We will provide you with the API for the game and some starter code. We encourage you to be creative with different models and possible logic, exploring new ways of “solving” the game.

## Rules of the Game

- Connections AI is a single player game with 16 words on the board
- Each word will only belong to one of the four groups of four
- Each group will have four words
- Players will start with 4 chances/lives
- To play, players will select four words that match a certain category
- When a player guessed 3/4 words correctly, the Player will receive a one word away warning
- If they correctly select four words that match one of the four categories, the Player will continue to guess the next category
- If they select the wrong four words, the Player will lose a life.
- Player wins when all 16 words are correctly matched with their category. Accuracy of guessing groups matter.

## Words
- The words will be represented by a 16 element 1D array. Each word will be arranged in a random order. The words should be grouped together and outputted as a 4x4 2D array.

## Implementation Algorithms
Common ways to use algorithms to solve games are as follows:

1. Natural Language Processors (NLP) Libraries - strong approach for understanding linguistics. Entirely heuristic approaches are weaker than the methods below, but perform far better than picking random moves. As some form of heuristics will be used in most of the below approaches, they are still important to understand.
- NLTK - Offers a wide array of tools for linguistic analysis and can help with tokenization, stemming, lemmatization, and basic word associations.
- spaCy - Provides fast tokenization and supports pre-trained word embeddings that are helpful for semantic similarity tasks.
- Hugging Face Transformers - Useful for fine-tuning large language models (LLMs) and includes access to pretrained models for word embeddings, contextual associations, and understanding relationships among words.

2. Data Sources - training your model on real world data. There are many datasets out there to give contextual meaning to tokens and words for the model to analyze Transforming the data is often necessary to help the model perform analysis.
- WordNet: A lexical database that groups English words into sets of synonyms. Useful for identifying connections based on synonyms and hypernyms.
- ConceptNet: A semantic network with a rich set of relationships between words, offering data on associations, common sense knowledge, and word similarity.
- Thesaurus Data: Online thesauruses can be scraped or accessed via APIs (like Merriam-Webster or Collins) to gather synonyms, antonyms, and related words.
- NY Times API: If available, this API may offer useful data on word frequency, usage context, and trends, which can inform connections.
- Wikipedia and Wikidata: Offers relational and hierarchical data on terms, categories, and named entities that can provide rich contextual connections.

3. Machine Learning Frameworks - tools to build and fine-tune your model. Many pretrained models are available with these frameworks that could give an advantage to a ground up model.
- TensorFlow: Useful for building neural network architectures and experimenting with word embeddings and sequence modeling for relationship extraction.
- PyTorch: Highly versatile for implementing deep learning models, such as LSTMs or transformers, which can be adapted for identifying word relationships.
- Scikit-Learn: Great for simpler models and for preprocessing steps such as clustering word vectors or performing dimensionality reduction.
- Gensim: Specializes in word embedding models like Word2Vec, Doc2Vec, and FastText, ideal for finding semantic similarities.

## Restrictions
- Max of four lives
- Any failed guesses will result in a loss of life

## Resources
1. Additional Resources - helpful resources to transform data and tune your model.

- Google’s Universal Sentence Encoder: Provides embeddings that capture sentence-level meaning, which can be useful for understanding word associations in different contexts.
- NLTK's SemCor Dataset: Contains annotated sentences with WordNet senses, which can aid in semantic disambiguation when identifying word connections.
- Stanford NLP: Includes tools like Named Entity Recognition (NER) and dependency parsing, which can assist in finding deeper relationships among terms.

## Tutorials and Documentation - to help you get started.
-Hugging Face Course: A free course on transformers that teaches how to leverage transformer models for various NLP tasks.
-paCy Documentation: Detailed guides and case studies on leveraging spaCy’s NLP capabilities.
-Kaggle: Explore notebooks on semantic similarity, word embeddings, and NLP preprocessing, which might offer inspiration and reusable code for similar tasks.


## Webhooks

"GET /"
{
"guess": "<["a", "b", "c", "d"]>",
"endTurn": "<BOOLEAN>"
}

## Testing
There will be an api provided at this endpoint: /. By sending a POST request to the endpoint, it will receive the status of the game and use your model then evaluate the guess. This is a test game, and the model will be using random example words.
Example: Setup your model to use the inputs and output a 4 word 1D array and endTurn boolean to the POST request.

## Grading
After submitting, your models will be evaluated on a testing dataset. Each guess is weighted differently depending on the number of correct guesses. There are no groups worth more than others based on difficulty. Instead, the group with the least successful guess will have the highest multiplier. This encourages to guess with confidence and accurately on the first attempt.
Example:
- Group 1: 4/4 - 1x
- Group 2: 3/4 - 2x (0 points)
- Group 3: 2/4 - 3x (0 points)
- Group 4: 2/4 - 3x (0 points)

There is also a penalty on the total score possible for strikes.

Example:
- 0 Strikes: 100%
- 1 Strike: 90%
- 2 Strikes: 75%
- 3 Strikes: 50%
- 4 Strikes: 25%

For each guess, points will only be awarded 1 point if the model gets 4/4 correct. They will not be awarded any partial points.

Each “guess” is defined as a submission of a group of 4 words. If the model does not get 4/4 correct in the group, then the guess counts as incorrect. We will be tallying the points and multipliers at the end of their guesses, not after every guess. Once the model reaches 4 strikes, their turn ends and we can tally the points.

The model will also have an option to stop guessing. This option will end their current turn, tally the points and finally move on to the next test set.

Example Scenarios:

All Correct with 0 strikes

- Group 1: 1 (correct) x 1 (weight) x 100% = 1 point
- Group 2: 1 (correct) x 2 (weight) x 100% = 2 points
- Group 3: 1 (correct) x 3 (weight) x 100% = 3 points
- Group 4: 1 (correct) x 3 (weight) x 100% = 3 points
- Total Score = 9 points

All Correct with 1 strike

- Group 1: 1 (correct) x 1 (weight) x 90% = 0.9 points
- Group 2: 1 (correct) x 2 (weight) x 90% = 1.8 points
- Group 3: 1 (correct) x 3 (weight) x 90% = 2.7 points
- Group 4: 1 (correct) x 3 (weight) x 90% = 2.7 points
- Total Score = 8.1 points

2 Correct Groups - 2 strikes
- Group 1: 1 (correct) x 1 (weight) x 75% = 0.75 points
- Group 2: 1 (correct) x 2 (weight) x 75% = 1.5 points
- Group 3: 0 (incorrect) x 3 (weight) x 75% = 0 points
- Group 4: 0 (incorrect) x 3 (weight) x 75% = 0 points
- Total Score = 2.25 points

Model Input and Output:
- Model Input: 16 words (array), strikes (int), isOneAway (bool), 
- CorrectGroups (2D array), previousGuesses (2D array), error (string)
- Example: ()
- Model Output: 4 words (array), endTurn (bool)
Example: ['Best Boy', 'Idea', 'Kroner', 'Stables']