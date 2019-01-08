from Prac_6.programming_language import ProgrammingLanguage

def main():
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    print(ruby)

    list=[ruby, python, visual_basic]

    for i in range(len(list)):
        if list[i].is_dynamic() == True:
            print(list[i].field)

main()