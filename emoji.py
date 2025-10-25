# emoji_demo.py

# Import the emoji library
import emoji

# Print a single emoji
print(emoji.emojize("Hello World! :earth_americas:"))

# Print multiple emojis
print(emoji.emojize("I love Python! :snake: :smile: :fire:"))

# Combine emojis in a sentence
print(emoji.emojize("Let's grab some coffee! :coffee: :thumbs_up:"))

# You can also disable alias conversion
print(emoji.emojize("Good night! :crescent_moon: :zzz:", language='alias'))
