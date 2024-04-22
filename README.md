# Pig Latin Converter

This Python script provides a simple tool to convert text into Pig Latin. Pig Latin is a language game or argot in which English words are altered, usually by moving the first letter of each word to the end of the word and adding "ay". Punctuation marks are left untouched.

## Usage
Clone the repository or download the piglatingen.py file.
Import the pig_it function into your Python script.
Call the pig_it function with a string as input to convert it into Pig Latin.

## Example:

```python

from piglatingen import pig_it

text = "Pig latin is cool"
pig_latin_text = pig_it(text)
print(pig_latin_text)  # Output: igPay atinlay siay oolcay
```
## Functionality
Converts text into Pig Latin by moving the first letter of each word to the end and adding "ay".
Preserves punctuation marks and other non-alphabetic characters.

Feel free to use this tool to have fun with Pig Latin or incorporate it into your projects where text conversion is needed!
