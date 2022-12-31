nama=("Nurul Fikri")
def removeVowels(nama):
    vowels = 'aiueoAIUEO'
    nama = ''.join([i for i in nama if i not in vowels])
    return nama

print(removeVowels("Nurul Fikri"))