def get_user_input():
    n_string = input("Enter here: ")
    n =  n_string.split(",") 
    numlist = [float(x) for x in n]
    return numlist 

def sort_temperature(numlist1):
    numlist1.sort()
    print('Temp ascending = ', numlist1)
    return

def average_temp(numlist2):
      average = sum(numlist2) / len(numlist2)
      return average

def calc_median_temp(numlist3):
     numlist3.sort()
     middle = len(numlist3) // 2
     res = (numlist3[middle] + numlist3[~middle]) / 2
     return res

def find_max(numlist4):
     numlist4.sort()
     maximum = max(numlist4)
     return maximum

def find_min(numlist5):
     numlist5.sort()
     minimum = min(numlist5)
     return minimum

def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

def main():
    display_main_menu()
    numlist = get_user_input()
    sort_temperature(numlist)
    print("Average = " , str(average_temp(numlist)))
    print("Median = " , str(calc_median_temp(numlist)))
    print('Min Temp = ' , str(find_min(numlist)))
    print('Max Temp = ' , str(find_max(numlist)))

if __name__ == "__main__":
    main()

    