#Multi level inheritance
# class Dad:
#     basketball = 1
# class Son(Dad):
#     dance = 1
#     basketball = 1
#     def isdance(self):
#         return f"he can dance {self.dance} no of times"
# class Grandson(Son):
#     dance = 6
#     guitar = 1
#     def isdance(self):
#         return f"fuck yeah!"\
#         f"he can dance {self.dance} no of times"
#     def isguitar(self):
#         return f" he can play guitar {self.guitar} no of times"
#
# shahid = Dad()
# hammad = Son()
# nouman = Grandson()
# print(nouman.isguitar())

#Quiz
class Electronicdevice:
    laptop = 1
    pc = 1
    tv = 1
class pocketgadget(Electronicdevice):
    watch = 1
    cellphone = 1
    def ispocketgadget(self):
        return f"they have {self.watch} watch and also {self.cellphone} phone in pocket"
class phone(pocketgadget):
    musicfile = 30
    videofile = 13
    movies = 10
    calculator = 1
    def isphone(self):
        return f"nouman phone have {self.musicfile} music and {self.videofile} videos and " \
               f"{self.movies} movies and also have {self.calculator} calculator"
shahid = Electronicdevice()
Hammad = pocketgadget()
nouman = phone()
print(nouman.isphone())