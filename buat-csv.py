import pandas as pd


# Definisikan label hiragana
hiragana_labels = {
    "あ": ("a", 0),
    "い": ("i", 1),
    "う": ("u", 2),
    "え": ("e", 3),
    "お": ("o", 4),
    "か": ("ka", 5),
    "き": ("ki", 6),
    "く": ("ku", 7),
    "け": ("ke", 8),
    "こ": ("ko", 9),
    "さ": ("sa", 10),
    "し": ("shi", 11),
    "す": ("su", 12),
    "せ": ("se", 13),
    "そ": ("so", 14),
    "た": ("ta", 15),
    "ち": ("chi", 16),
    "つ": ("tsu", 17),
    "て": ("te", 18),
    "と": ("to", 19),
    "な": ("na", 20),
    "に": ("ni", 21),
    "ぬ": ("nu", 22),
    "ね": ("ne", 23),
    "の": ("no", 24),
    "は": ("ha", 25),
    "ひ": ("hi", 26),
    "ふ": ("fu", 27),
    "へ": ("he", 28),
    "ほ": ("ho", 29),
    "ま": ("ma", 30),
    "み": ("mi", 31),
    "む": ("mu", 32),
    "め": ("me", 33),
    "も": ("mo", 34),
    "や": ("ya", 35),
    "ゆ": ("yu", 36),
    "よ": ("yo", 37),
    "ら": ("ra", 38),
    "り": ("ri", 39),
    "る": ("ru", 40),
    "れ": ("re", 41),
    "ろ": ("ro", 42),
    "わ": ("wa", 43),
    "を": ("wo", 44),
    "ん": ("n", 45)
}


data = [(hiragana, romaji, label) for hiragana, (romaji, label) in hiragana_labels.items()]
df = pd.DataFrame(data, columns=['Hiragana', 'Romaji', 'Label'])

# Simpan DataFrame ke file CSV
df.to_csv('data-label/hiragana_labels.csv', index=False)