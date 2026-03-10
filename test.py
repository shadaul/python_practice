# #Напишите программу, которая предлагает пользователю отгадать "загаданное компьютером" (случайно сгенерированное) число. После каждой неудачной попытки программа выводит сообщение о том, больше или меньше введенное человеком число, чем загаданное. Программа должна подсчитывать количество попыток, за которые человек угадывает число.
# # import random

# # rand_num = random.randrange(1,101)

# # counter = 0

# # while True:
# #     user_input = int(input(f"Popitka nomer: {counter} \n print quessed number: "))
    
# #     if user_input == rand_num:
# #         print(f"you are right, sdelal za {counter} popitok")
# #         break #False
# #     elif user_input > rand_num:
# #         print("very high")
# #     else:
# #         print("very low")


# #     counter += 1

# #     if counter == 100:
# #         break



# # x = [[1 , 2 , 3], [4,5,6]] #

# # b = x.copy()

# # b[0] = 20

# # print(x)




# class Mycar:

#     def __init__(self, model: str, year: int):
#         self.model = model
#         self.year = year


#     def make_younger(self):
#         self.year = self.year + 10
        

# import time


# l = [1, 2, 3]
# print(l.index([1]))

# x = Mycar(
#     model = "Audi",
#     year = 1993
# )

# y = x.make_younger()

# # print(y)


# class Calculator:

#     def __init__(self,num1: int, num2: int, symb1: str):
#         self.num1 = num1
#         self.num2 = num2
#         self.symb1 = symb1
#         self.result = None

#     @staticmethod    
#     def get_time():
#         return "sadsadsdsds" #Calculator.get_time()

#     def calc_sum(self):
#         if self.symb1 == "+":
#             self.result = self.num1 + self.num2 #Calculator.calc_sum(self) or self.calc_sum()
    
#     def calc_minus(self):
#         if self.symb1 == "-":
#             self.result = self.num1 - self.num2
        
#     def calculate(self):
#         if self.symb1 == "+":
#             self.calc_sum()
#         if self.symb1 == "-":
#             self.calc_minus()
#     def get_result(self, hello: str = None):
#         if hello:
#             print(hello)

#         return self.result      


# a = Calculator(
#     num1 = 3,
#     num2 = 2,
#     symb1 = "-"
# )

# b = a.calculate()

# result = a.get_result(hello="hello")


# print(result)




# for (int i = 0; i < 5; i++) {
#   cout << i << "\n";
# }


# *args 
# **kwargs
# def lolol(name: str,*kik ,**ages):
#     print(f"Name: {name}")
#     for i in kik:
#         print(i, "*args")

#     for age, lol in ages.items():
#         print(age,"=", lol, "**kwargs")


# lolol("yury",2 ,3, 4, 5, age1=12, age2=4, age3=25)






# test = [[1, 2, 4, 6], ["l", "i", "p"]]
# for index, data in enumerate(test):
#     print(f"index; {index}","data" ,*data)



print("hello","world")
















