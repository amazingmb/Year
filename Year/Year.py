

def is_year_leap(Year):
      if f"Year % 4 == 0 and Year % 100 != 0 or Year % 400 == 0" :
        print("True")
      else: print("False")

is_year_leap(input("Enter year: "))