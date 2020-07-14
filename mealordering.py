import csv

print("Enter the product ID: ")
productid=list(input().split())
dict={}
#quantity=int(input("Enter the quantity: "))
for id in productid:
    if id in dict.keys():
        dict[id]+=1
    else:
        dict [id]=1
csv_file=csv.reader(open("shoppinglist.csv", "r"),delimiter=",")

total=0
for id,count in dict.items():
    for row in csv_file:
        if id==row[0]:
            product_id=row[0]
            product_name=row[1]
            product_price=row[2]
            print("\nProduct ID: {}".format(row[0]))
            print("Product Name: {}".format(row[1]))
            print("Product Price: {}".format(row[2]))
            total+=count * (int(product_price))
            break

print("\nThe Total Amount Payable is: {}".format(total))







#import csv
#
#
# def findProduct(productId):
#     csv_file = csv.reader(open('shoppinglist.csv', 'r'), delimiter=',')
#     productPrice = 0
#     productName = ''
#     isFound = False
#     for row in csv_file:
#         if productId == row[0]:
#             productName = row[1]
#             productPrice = row[2]
#             isFound = True
#             break
#     result = {
#         'isFound': isFound,
#         'productName': productName,
#         'productPrice': productPrice,
#         'productId': productId
#     }
#     return result
#
#
# total = 0
# printList = []
# while (True):
#     productid = input("Enter a product Id: ")
#     result = findProduct(productid)
#     if not (result['isFound']):
#         print("Product is not found...")
#         continue
#
#     quantity = int(input("Enter the quantity: "))
#     if (quantity <= 0):
#         print("Please select atleast 1 quantity.")
#         continue
#     total += quantity * (int(result['productPrice']))
#     temp = [result['productName'], quantity, result['productPrice']]
#     printList.append(temp)
#     addMore = input("Add more Items? (Y/N) : ")
#     if (addMore.lower() == 'n'):
#         break
#
# print("\nBill\n====\n\n[Product Name] [Product Price] [Quantity]")
# for item in printList:
#     print("{}  {}  {}".format(item[0], item[2], item[1]))
# print("The total Amount payable is : {}".format(total))