import csv
# For the average
from statistics import mean 

def calculate_averages(input_file_name, output_file_name):
 with open(input_file_name) as f:
   reader=csv.reader(f)
   with open(output_file_name,'w',newline='') as w:
     writer=csv.writer(w)

     for row in reader:
      name=row [0] 
      grades=list()
      for i in row [1:]:
        grades.append(float(i))

      #print(name, mean(grades)) 
      writer.writerow([name, mean(grades)]) 



def calculate_sorted_averages(input_file_name, output_file_name):
 with open(input_file_name) as f:
   reader=csv.reader(f)
   with open(output_file_name,'w',newline='') as w:
     writer=csv.writer(w)
     total=[]

     for row in reader:
        name=row [0] 
        grades=list()
        
        for i in row [1:]:
         grades.append(float(i))

       
        s=(name,mean(grades)) # sort 
        total.append(s)
        total.sort(key=lambda k: (k[1],k[0])) 
        
     for i in total: #name and average 
      #print(i[0],i[1])
      writer.writerow([i[0],i[1]])   


def calculate_three_best(input_file_name, output_file_name):
 with open(input_file_name) as f:
   reader=csv.reader(f)
   with open(output_file_name,'w',newline='') as w:
     writer=csv.writer(w)
     total=[]

     for row in reader:
        name=row [0] 
        grades=list()
        
        for i in row [1:]:
         grades.append(float(i))

       
        s=(name,mean(grades)) # sort 
        total.append(s) 
        total.sort(key=lambda k: (-k[1],k[0])) 
     for i in total[:3]: 
      #print(i[0],i[1])
      writer.writerow([i[0],i[1]])



def calculate_three_worst(input_file_name, output_file_name):
 with open(input_file_name) as f:
   reader=csv.reader(f)
   with open(output_file_name,'w',newline='') as w:
     writer=csv.writer(w)
     total=[]

     for row in reader:
        name=row [0] 
        grades=list()
        
        for i in row [1:]:
         grades.append(float(i))

       
        s=(name,mean(grades)) # sort 
        total.append(s)
        total.sort(key=lambda k: k[1])

     for i in total[:3]: 
       #print(i[1])
       writer.writerow([i[1]])  



def calculate_average_of_averages(input_file_name, output_file_name):
 with open(input_file_name) as f:
   reader=csv.reader(f)
   with open(output_file_name,'w',newline='') as w:
     writer=csv.writer(w)
     total=[]

     for row in reader:
        name=row [0] 
        grades=list()
        
        for i in row [1:]:
         grades.append(float(i))

       
        s=(name,mean(grades)) # sort 
        total.append(s)
        total.sort(key=lambda k: k[1]) 

        average2=[] 
     for i in total: 
      average2.append(i[1])
     #print(mean(average2))
     writer.writerow([mean(average2)])          