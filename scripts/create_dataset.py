import csv

# Format: [num_sections, entry_point, header_size, machine, file_size, entropy, label]
# label: 1 = malware, 0 = safe

data = [
    [7, 7008, 4096, 34404, 348160, 3.75, 0],  # notepad.exe (benign)
    [5, 6000, 512, 332, 150000, 7.5, 1],      # fake malware sample
    [6, 4000, 1024, 332, 120000, 6.9, 1],     # another fake malware
    [8, 9000, 4096, 332, 250000, 2.5, 0],     # another clean one
]

with open("sample_dataset.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["sections", "entry_point", "header_size", "machine", "file_size", "entropy", "label"])
    writer.writerows(data)

print("✅ Sample dataset created!")
