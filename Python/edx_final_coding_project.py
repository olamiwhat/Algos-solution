print("Report Type include All items (\"A\") or Total only (\"T\")")
while True:
    report = input("enter report type, \"A\" or \"T\": ")
    if report.upper() == "A" or report.upper() == "T":
        break
    print (report, "is an invalid input")
        
#print (report)
def adding_report(report = "T"):
    total = 0
    item = ""
    while True:
        num = input("enter an integer or \"Q\" to quit: ")
        if num.isdigit():
            total = total + int(num)
            if report.upper() == "A":
                item = item + num + "\n"
        elif num.upper().startswith("Q"):
            if report.upper() == "A":
                print("Item" + "\n" + item)
            print("Total" + "\n"+ str(total))
            break
        else:
            print("input is invalid!")


adding_report(report)
