#quote daxilində necə xarakter olduğunu tapın 

#quote = "Programming isn't about what you know; it's about what you can figure out."
#print(len(quote))

################################################################################################################

#quote daxilində necə boşluq olduğunu tapın link
#def  bosluq_tap(string)
     #count = 0
     #for i in range(0, len(string));
     #if string[1] == " "
       # count+=1
     #return count
 #string = "Programming isn't about what you know; it's about what you can figure out"
# print("bosluq sayi",bosluq_tap(string))

################################################################################################################

#quote ifadəsini sözlərini ayrı ayrı ekrana çap edin link

#quote = "Programming isn't about what you know; it's about what you can figure out."

#print(quote.split())


################################################################################################################

#quote daxilində olan ' işarəsini silərək yeni əldə edilən ifadəni ekrana çap edin link

#quote = "Programming isn't about what you know; it's about what you can figure out."

#x = quote.replace("'", " ")

#print(x)

################################################################################################################

#quote daxilində necə hərf olduğunu tapın

#quote = "Programming isn't about what you know; it's about what you can figure out."








################################################################################################################


#quote daxilində necə ədəd o hərfi olduğunu tapın

#quote = "Programming isn't about what you know; it's about what you can figure out"
#counter = Counter(quote)
#print(counter['o']) 


################################################################################################################

#list-i tərs çevirərək ekrana çap edin

#nums=[23,56,78,100,14,70,300,236]

#nums.reverse()

#print('Ters_cevirilmis:', nums)



################################################################################################################

nums=[23,56,78,100,14,70,300,236]

def ikiliededleritapin():
    for eded in nums:
     if eded>10 and eded<100:
            print(eded)
ikiliededleritapin()
            






