def generate_saudi_numbers(filename="saudi_numbers.txt"):
    prefixes = ["050", "051", "053", "054", "055", "056", "057", "058", "059"]
    with open(filename, "w") as file:
        for prefix in prefixes:
            for i in range(1000000):  # من 000000 إلى 999999
                number = f"{prefix}{i:06d}"
                file.write(number + "\n")
    print(f"تم إنشاء جميع أرقام الهواتف وحفظها في {filename}")

# تشغيل الدالة
generate_saudi_numbers()
