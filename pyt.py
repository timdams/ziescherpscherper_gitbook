import os

def count_markdown_characters(root_folder):
    total_chars = 0

    for foldername, _, filenames in os.walk(root_folder):
        for filename in filenames:
            if filename.lower().endswith(".md"):
                filepath = os.path.join(foldername, filename)
                with open(filepath, "r", encoding="utf-8") as f:
                    total_chars += len(f.read())

    return total_chars


if __name__ == "__main__":
    folder = r"C:\Users\damst\Koofr\PROGPROJECTS\cursus\ziescherpscherper_gitbook"   # <-- aanpassen
    total = count_markdown_characters(folder)
    print(f"Totaal aantal tekens in alle markdownfiles: {total}")
