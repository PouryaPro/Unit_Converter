def unit_converter():
    print("ماشین‌حساب تبدیل واحد")
    print("1. تبدیل طول (متر به کیلومتر)")
    print("2. تبدیل وزن (کیلوگرم به گرم)")
    print("3. تبدیل دما (سلسیوس به فارنهایت)")
    print("4. خروج")

    while True:
        choice = input("یک گزینه انتخاب کنید (1-4): ")

        if choice == "1":
            meters = float(input("مقدار طول در متر: "))
            kilometers = meters / 1000
            print(f"{meters} متر برابر است با {kilometers} کیلومتر")

        elif choice == "2":
            kilograms = float(input("مقدار وزن در کیلوگرم: "))
            grams = kilograms * 1000
            print(f"{kilograms} کیلوگرم برابر است با {grams} گرم")

        elif choice == "3":
            celsius = float(input("دما در سلسیوس: "))
            fahrenheit = (celsius * 9/5) + 32
            print(f"{celsius} درجه سلسیوس برابر است با {fahrenheit} درجه فارنهایت")

        elif choice == "4":
            print("خروج از برنامه. خداحافظ!")
            break

        else:
            print("لطفاً یک گزینه معتبر انتخاب کنید.")


# اجرای برنامه
unit_converter()
