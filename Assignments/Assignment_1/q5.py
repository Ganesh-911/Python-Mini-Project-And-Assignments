print("Enter the page numbers between 1 and 25")

page = 0

count = 0

your_list = []

page_list = range(1,26)

while(count < 25):

    page = int(input("Enter page number (Enter -1 to exit) : "))

    if page == -1:
        break
        
    elif page <= 0 and page != -1:

        print("Page number cannot be negetive")

    elif page > 25:

        print("Please enter number less than 25.")

    else:
        
        your_list.append(page)

        count += 1

print("Your_list is : ", set(your_list))

print("The missing pages are : ", list(set(page_list)-set(your_list)))