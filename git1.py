import csv
namee=[]
Descriptionss=[]
priorityy=[]




class task():
    def __init__(self,name,Description,Priority):
        self.name=name
        self.Description=Description
        self.priority=Priority
        namee.append(self.name)
        Descriptionss.append(self.Description)
        priorityy.append(self.priority)
    



class todolist(task):
    
    def remov_name(remov):
        if remov in namee:
            namee.remove(remov)
        else:
             print(f"{remov} not found too name")  
    def remov_description(remov):
        if remov in Descriptionss:
            Descriptionss.remove(remov)
        else:
             print(f"{remov} not found too Descriptions")
    def remov_priority(remov):
        if remov in priorityy:
                priorityy.remove(remov)
        else:
                 print(f"{remov} not found too priority")                  
    def show_all():
        for row in zip(namee  ,Descriptionss   , priorityy):
            print(f"{row[0]} | {row[1]} | {row[2]}")
        






salamati=task("varzesh","miram bashgah va kami pyade ravi mikonam", "mohm")
barname_nvisi=task("python","python jame jadi ro yad migiram","kheili mohm")
pool_darbiarm=task("khoshnam","onja bastani mifrosham v zorat mizanam","mohm")
enarxi=task("gahve","badastgah esperso sazm gahve dorost konm","ziad mohm nist")
fotsaal=task("salon","miram ta fitsal bazi bokonam","mohm nis")
zibayi=task("brm arayeshgah","miram arayeshgah pish sajad bartar","mohm")




with open('task.csv', 'w', newline='', encoding='utf-8-sig') as file:
    writer = csv.writer(file)
    
    # نوشتن هدر
    writer.writerow(['name', 'Discraptins', 'priority'])
    
    # نوشتن داده‌ها با ترکیب لیست‌ها
    for row in zip(namee, Descriptionss, priorityy):
        writer.writerow(row)







todolist.remov_name("SS")
todolist.remov_description("SS")
todolist.remov_priority("ss")
todolist.show_all()