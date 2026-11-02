# Exercise 8-13: Membuat profil dengan keyword arguments.
def build_profile(first, last, **user_info):
    profile = {"first_name": first, "last_name": last}
    profile.update(user_info)
    return profile

my_profile = build_profile(
    "Samuel",
    "Kristian",
    kelas="XI",
    hobi="pemrograman",
    kota="Surakarta",
)
print(my_profile)
