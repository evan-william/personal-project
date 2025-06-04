from collections import Counter

def min_sum_after_discard(cards):
    total_sum = sum(cards)  # Hitung jumlah total kartu
    card_counts = Counter(cards)  # Hitung frekuensi setiap angka pada kartu
    
    min_sum = total_sum  # Inisialisasi dengan total sum (tanpa pembuangan)

    # Coba mengurangi nilai dengan membuang 2 atau 3 kartu dengan angka yang sama
    for num, count in card_counts.items():
        if count >= 2:
            min_sum = min(min_sum, total_sum - num * 2)  # Buang dua kartu yang sama
        if count >= 3:
            min_sum = min(min_sum, total_sum - num * 3)  # Buang tiga kartu yang sama
    
    return min_sum

# Input
cards = list(map(int, input().split()))

# Output
print(min_sum_after_discard(cards))
