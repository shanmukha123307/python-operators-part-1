amount=int(input("please enter the amount "))
note_1=amount//100
note_2=(amount%100)//50
note_3=((amount%100)%50)//10
print("notes of 100 are",note_1)
print("notes of 50 are",note_2)
print("notes of 10 are",note_3)