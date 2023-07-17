# Python Word Counter
# By Marcus Secu on 2023-7-17
# A program that counts the amount of words in text files given a custom delimiter.

# Imports
import os

# Determines separation between words.
delimiter = ' '

def main():
    """ Main function of program. """

    # List all text files in directory
    text_file_names = os.listdir('text')
    
    # Check if there are any files
    if len(text_file_names):

        # Combined data of all files
        combined_file_text = ''

        # Loop through all files and combine them
        for file_name in text_file_names:
            with open('text/{}'.format(file_name)) as raw_file_contents:
                file_data = raw_file_contents.readlines()
                for line in file_data:
                    combined_file_text += (delimiter+line)

        # Clean up combined string
        excluded_string_data = ['\n', '']
        for filter in excluded_string_data:
            combined_file_text = combined_file_text.replace(filter, '')

        # Split combined data into separate words given delimiter
        combined_file_words = combined_file_text.split(delimiter)

        # Clean up list of words
        excluded_list_data = ['']
        for item in excluded_list_data:
            while item in combined_file_words:
                combined_file_words.remove(item)

        # Print word and character count.
        print(F"""
FILES: {text_file_names}
WORDS: {len(combined_file_words)}
CHARACTERS: {len(" ".join(combined_file_words))}
        """)

if __name__ == '__main__':
    main()