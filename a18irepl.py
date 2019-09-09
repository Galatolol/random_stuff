import random

def randomize_companies():
    company_list = ["1","2","3","4","5","6","7","9","10","11","12","13","14","A", "B"]

    random.shuffle(company_list)

    result = "Companies order: {}".format(", ".join(["8"] + company_list[:-2]))
    return result

randomize_companies()