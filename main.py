import connect
from readfile import Readfile

path = "form.xlsx"
savepath = "newform.xlsx"

sheet = Readfile(path)
max_row = sheet.get_maxrow()

def main():
    for i in range(2, max_row):
        OGR_NUM = sheet.get_value(i, 1) 
        TC_KIM = sheet.get_value(i,2)
        print(OGR_NUM.value, TC_KIM.value)
        array = connect.login(OGR_NUM.value, TC_KIM.value)
        sheet.set_list(i,3,array)
        print(array)
        sheet.save(savepath)

if __name__ == "__main__":
    main()