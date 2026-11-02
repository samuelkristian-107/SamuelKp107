# Exercise 6-12: Pengembangan dictionary bertingkat.
# Contoh tambahan: data sekolah dan beberapa mata pelajaran setiap kelas.
sekolah = {
    "XI IPA 1": {"wali_kelas": "Bu Rina", "mata_pelajaran": ["Matematika", "Biologi", "Kimia"]},
    "XI IPS 1": {"wali_kelas": "Pak Dedi", "mata_pelajaran": ["Ekonomi", "Sejarah", "Geografi"]},
}
for kelas, data in sekolah.items():
    print(f"\nKelas: {kelas}")
    print(f"Wali kelas: {data['wali_kelas']}")
    print("Mata pelajaran:")
    for mapel in data["mata_pelajaran"]:
        print(f"- {mapel}")
