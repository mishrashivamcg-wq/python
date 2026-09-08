age = 22
has_license = True
has_insurance = True
car_available = True

if age >= 21:
    if has_license:
        if has_insurance:
            if car_available:
                print("You are eligible to drive.")










math = 85
sci = 78
eng = 92
pass_mark = 40



if math == 100:
    print("Math: very bad score (100)!")


if sci != 0:
    print("Science: Try best  (Score is not 0).")


if eng > 90:
    print("English: Nice performance (> 90).")

if math < pass_mark:
    print("FAIL in Math")

if sci < pass_mark:
    print("FAIL in Science")

if eng < pass_mark:
    print("FAIL in English")   







is_indian=input("Are you an Indian citizen? (yes/no): ")

if is_indian=="yes":
    print("You are an Indian citizen.")
else:
    print("You are not an Indian citizen.")   