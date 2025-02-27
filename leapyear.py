year = int(input("Enter Year: "))
if year % 4 == 0:  #memeriksa apakah tahun dapat dibagi 4
     if year % 100 == 0: #dapat dibagi 100
          if year % 400 == 0: #dibagi 400
               print("Leap Year")
          else:
               print("Not Leap Year")
     else:
          print("Leap Year") #Tahun kabisat tapi tidak dapat dibagi 100
else:
     print("Not Lap Year")
      
