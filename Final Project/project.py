import re

def identify_generation(text):
    #Identify the likely generation based on the input text
    gen_z_keywords = ["vibe", "lit", "sus", "nocap", "bet", "fam", "yeet", "mid", "lowkey", "highkey", "tea", "mood", "ghost", "simp", "clout", "cringe", "slaps", "deadass", "trash", "flex"]
    boomer_keywords = ["groovy", "rad", "hip", "farout", "coolcat", "bologna", "digit", "righton", "boss", "bread", "happening", "solid", "sweet", "killer", "awesome", "dynamite", "gear", "fab", "peachy", "blast"]
    gen_alpha_keywords = ["slay", "extra", "yas", "npc", "unhinged", "maincharacter", "touchgrass", "ratio", "based", "cheugy", "yassification", "chroniconline", "feral", "goblinmode", "kinnie", "alt", "hyperfix", "delulu", "situationship", "rizz"]
    text = text.lower()
    gen_z_count = sum(word in text for word in gen_z_keywords)
    boomer_count = sum(word in text for word in boomer_keywords)
    gen_alpha_count = sum(word in text for word in gen_alpha_keywords)

    counts = {"Gen Z": gen_z_count, "Boomer": boomer_count, "Gen Alpha": gen_alpha_count}
    likely_gen = max(counts, key=counts.get)
    return likely_gen if counts[likely_gen] > 0 else "Unknown Generation"

def clean_text(text):
    #Clean text by removing special characters and extra spaces
    return re.sub(r"[^a-zA-Z0-9\s]", "", text).strip()

def analyze_text():
    #Prompt user for input, clean the text, and identify the generation
    user_input = input("Enter a phrase or sentence: ")
    cleaned_input = clean_text(user_input)
    generation = identify_generation(cleaned_input)
    print(f"Based on your input, you might belong to: {generation}")

def main():
    #Main function to run the program
    print("Welcome to the Generation Identifier!")
    analyze_text()

if __name__ == "__main__":
    main()
