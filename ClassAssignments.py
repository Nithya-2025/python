class ClassAssignments:
    def Subfields():
        sub_fields = ["Machine Learning",  "Neural Networks", "Vision", "Robotics", "Speech Processing", "Natural Language Processing"]
        print("Sub-fields in AI are: ")
        for sf in sub_fields:
            print(sf)
            
    def OddEven():
        num = int(input("Enter a number:"))
        if(num%2==0):
            res = "is an Even number"
        else:
            res = "is Odd number"
        print(num, res)

    def Elegible():
        sex = input("Your gener:")
        age = int(input("Your age:"))
        if((sex == "male" or sex =="m") and age>=21):
            result = "Eligible"
        elif((sex == "female" or sex =="f") and age>=18):
            result = "Eligible"
        else:
            result = "Not Eligible"
        print(result)

    def percentage():
        s1 = int(input("Subject1: "))
        s2 = int(input("Subject2: "))
        s3 = int(input("Subject3: "))
        s4 = int(input("Subject4: "))
        s5 = int(input("Subject5: "))
        print( (s1+s2+s3+s4+s5)/5)

    def triangle_area():
        height = float(input("Height: "))
        breath = float(input("Breath: "))
        print("Area of a triangle is ", (height*breath)/2)
        
    def triangle_perimeter():
        height1 = float(input("Height1 "))
        height2 = float(input("Height2 "))
        breath = float(input("Breath "))
        print("Area of a perimeter is :", height1+height2+breath)