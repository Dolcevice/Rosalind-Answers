def mendel(k : int, m : int, n : int):
    total_count = k + m + n
    chanceK = k / total_count
    chanceKK = chanceK * (k - 1) / (total_count - 1)
    chanceKM = chanceK * (m) / (total_count - 1)
    chanceKN = chanceK * (n) / (total_count - 1)
    chanceM = m / total_count
    chanceMM = 0.75 * chanceM * (m - 1) / (total_count - 1)
    chanceMK = chanceM * (k) / (total_count - 1)
    chanceMN = 0.5 * chanceM * (n) / (total_count - 1)
    chanceN = n / total_count
    chanceNK = chanceN * (k) / (total_count - 1)
    chanceNM = 0.5 * chanceN * (m) / (total_count - 1)
    return chanceKK + chanceKM + chanceKN + chanceMM + chanceMK + chanceMN + chanceNK + chanceNM

print(mendel(22, 20, 30))