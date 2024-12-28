import sys

def count_characters(document) -> dict:
  letter_counts = {}
  document = document.lower()
  for character in document:
    if not character.isalpha():
      continue
    if character in letter_counts:
      letter_counts[character] += 1
    else:
      letter_counts[character] = 1
  return letter_counts
    
def count_words(document) -> int:
  return len(document.split())

def read_file_contents(file_path) -> str:
  with open(file_path) as f:
    return f.read()  

def main() -> int:
  book_path = "books/frankenstein.txt"
  file_contents = read_file_contents(book_path)
  num_words = count_words(file_contents)
  
  print(f"--- Begin report of {book_path} ---")
  print(f"{num_words} words found in document\n")
  character_dict = count_characters(file_contents)
  for k in sorted(character_dict, key=character_dict.get, reverse=True):
    print(f"The '{k}' character was found {character_dict[k]} times")
    
  print("--- End report ---")
  return 0

if __name__ == '__main__':
    sys.exit(main()) 