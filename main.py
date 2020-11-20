# Tha main application's program

from tkinter import *
from tkinter.ttk import Combobox
import pandas as pd

# Spreadsheets
pp=pd.read_csv('population.csv')
dataset=pd.read_csv('dataset.csv')

# Variables
inftime=0
finftime=inftime+1
reptime=0
ppn=0

class Window:
  def __init__(program, win):
    # List of coordinates
    program.coordinates=("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20")
    
    # Code to add widgets
    program.btncalc=Button(win, text="Calculate Data", command=program.getcoordinates)
    program.btncalc.place(x=170, y=205)
    #program.btntime=Button(win, text="Button 2"), command=)
    #program.btntime.place(x=200, y=260)
    
    # Headings
    program.title=Label(win, text="Dataset Application", fg="black", bg="#9fe1e1", font=("Arial", 16))
    program.title.place(x=250, y=29)
    program.lblstats=Label(win, text="Total Statistics", bg="#9fe1e1", font=("Arial", 14))
    program.lblstats.place(x=400, y=70)
    program.lblstats=Label(win, text="Specified Data", bg="#9fe1e1", font=("Arial", 14))
    program.lblstats.place(x=150, y=70)
    
    # Display Statistics
    program.lbltime=Label(win, text="Average Time: ", bg="#9fe1e1")
    program.lbltime.place(x=350, y=105)
    program.lblppn=Label(win, text="Total Population: ", bg="#9fe1e1")
    program.lblppn.place(x=350, y=150)
    program.lblresc=Label(win, text="Cases with \nRespiratory Issues: ", bg="#9fe1e1")
    program.lblresc.place(x=350, y=195)
    program.lbldbt=Label(win, text="Cases with Diabetes: ", bg="#9fe1e1")
    program.lbldbt.place(x=350, y=240)
    program.lblabbp=Label(win, text="Cases with Abnormal \nBlood Pressure: ", bg="#9fe1e1")
    program.lblabbp.place(x=350, y=285)
    program.lblaged=Label(win, text="Cases Aged Above 60: ", bg="#9fe1e1")
    program.lblaged.place(x=350, y=330)
    program.lblagalive=Label(win, text="Alive: ", bg="#9fe1e1")
    program.lblagalive.place(x=350, y=355)
    program.lblagdead=Label(win, text="Dead: ", bg="#9fe1e1")
    program.lblagdead.place(x=350, y=375)
    program.lblttc=Label(win, text="--------------------------------------------------------", bg="#9fe1e1")
    program.lblttc.place(x=340, y=405)
    program.lblttc=Label(win, text="Total: ", bg="#9fe1e1")
    program.lblttc.place(x=350, y=435)
    program.lblttn=Label(win, text="462880 cases", bg="#9fe1e1")
    program.lblttn.place(x=490, y=435)
    program.lbltta=Label(win, text="Alive: ", bg="#9fe1e1")
    program.lbltta.place(x=350, y=465)
    program.lblttd=Label(win, text="Dead: ", bg="#9fe1e1")
    program.lblttd.place(x=350, y=495)
    # program.lblavg=Label(win, text="Value", bg="#9fe1e1")
    # program.lblavg.place(x=490, y=95)
    # program.txtx=Entry(win, text="Enter the X-coordinate", bd=2)
    # program.txtx.place(x=150, y=100)
    # program.txty=Entry(win, text="Enter the Y-coordinate", bd=2)
    # program.txty.place(x=150, y=150)
    
    # Left Section
    program.lblx=Label(win, text="X-Coordinate", bg="#9fe1e1")
    program.lblx.place(x=20, y=110)
    program.lbly=Label(win, text="Y-Coordinate", bg="#9fe1e1")
    program.lbly.place(x=20, y=155)
    program.ddx=Combobox(win, values=program.coordinates)
    program.ddx.place(x=150, y=110)
    program.ddy=Combobox(win, values=program.coordinates)
    program.ddy.place(x=150, y=155)
    program.lblerror=Label(win, text="ERROR! Please enter a value \nbetween 1 and 20.", fg="#ffffff", bg="orange")
    program.lblspresp=Label(win, text="Respiratory Symptoms: ", bg="#9fe1e1")
    program.lblspresp.place(x=20, y=245)
    program.lblds=Label(win, text="Diabetic: ", bg="#9fe1e1")
    program.lblds.place(x=20, y=285)
    program.lblspbp=Label(win, text="BP Anomalies: ", bg="#9fe1e1")
    program.lblspbp.place(x=20, y=325)
    program.lblalive=Label(win, text="Alive: ", bg="#9fe1e1")
    program.lblalive.place(x=20, y=365)
    program.lblspdead=Label(win, text="Dead: ", bg="#9fe1e1")
    program.lblspdead.place(x=20, y=405)
    program.lblcase=Label(win, text="No. of cases: ", bg="#9fe1e1")
    program.lblcase.place(x=20, y=445)
    program.lblppd=Label(win, text="Population Density: ", bg="#9fe1e1")
    program.lblppd.place(x=20, y=485)
    program.lblperc=Label(win, text="% Composition: ", bg="#9fe1e1")
    program.lblperc.place(x=20, y=525)
    program.lblstatus=Label(text="Unknown", bg="#9fe1e1", font=("Arial", 13))
    program.lblstatus.place(x=175, y=560)

    # Static Data
    program.lblspacase=Label(text="-", bg="#9fe1e1")
    program.lblspacase.place(x=175, y=365)
    program.lblspdcase=Label(text="-", bg="#9fe1e1")
    program.lblspdcase.place(x=175, y=405)
    program.lblspcasen=Label(text="-", bg="#9fe1e1")
    program.lblspcasen.place(x=175, y=445)
    program.lblppdn=Label(text="-", bg="#9fe1e1")
    program.lblppdn.place(x=175, y=485)
    program.lblpercn=Label(text="-", bg="#9fe1e1")
    program.lblpercn.place(x=175, y=525)
    program.lblspres=Label(text="-", bg="#9fe1e1")
    program.lblspres.place(x=175, y=245)
    program.lbldscases=Label(text="-", bg="#9fe1e1")
    program.lbldscases.place(x=175, y=285)
    program.lblspabbp=Label(text="-", bg="#9fe1e1")
    program.lblspabbp.place(x=175, y=325)
    
    # Bind to functions
    program.btncalc.bind('<Button-1>', program.getcoordinates)
    #program.btntime.bind('<Button-1>', program.avgtime)
    
    # Execute the functions to calculate statistics
    print("Initializing complete. Performing next steps before starting program...")
    print("EXECUTE function avgtime()..")
    program.avgtime()
    print("\nEXECUTE function getpp()..")
    program.getpp()
    print("\nEXECUTE function rescases()..")
    program.rescases()
    print("\nEXECUTE function dcases()..")
    program.dcases()
    print("\nEXECUTE function abbpcases()..")
    program.abbpcases()
    print("\nEXECUTE function agedcases()..")
    program.agedcases()
    print("\nEXECUTE function totaln()..")
    program.totaln()
        
  # Find the average time taken by a patient to report infections
  def avgtime(program):
    # print(dataset.head[2:3])
    # Get the average time
    
    # For Debug only
    # ycoordinate=int(program.ddy.get())
    
    rown=0
    tmr=int(dataset.iloc[rown,1])
    tmi=int(dataset.iloc[rown,0])+1
    # print("\nThe total time taken is: ")
    # print(tmr-tmi)

    ftmr=tmr+int(dataset.iloc[rown,1])
    rown=rown+1
    ftmi=tmi+int(dataset.iloc[rown,0])
    
    for i in range(462879):
      ftmr=ftmr+int(dataset.iloc[rown,1])
      rown=rown+1
      ftmi=ftmi+int(dataset.iloc[rown,0])

    totaltime=ftmr-ftmi
    # print(totaltime)
    avgtime=totaltime/462880
    print("\nThe average time is: ")
    print(int(avgtime))

    program.lblavg=Label(text=str(int(avgtime))+" days", bg="#9fe1e1")
    program.lblavg.place(x=490, y=105)

  # Get the population
  def getpp(program):
    rown=0
    ppn=0
    
    for i in range(400):
      ppn=ppn+int(pp.iloc[rown,2])
      rown=rown+1

    print("The total population is: "+str(ppn)+" people")
    program.lblppnv=Label(text=str(ppn)+" people", bg="#9fe1e1")
    program.lblppnv.place(x=490, y=150)
  
  # Find the number of cases with respiratory illnesses
  def rescases(program):
    riln=0
    rown=0

    for i in range(462880):
      outcome=str(dataset.iloc[rown,6])

      if outcome.upper().find("TRUE"):
        riln=riln+1
        rown=rown+1
      else:
        rown=rown+1

    print("Number of cases with respiratory illnesses is: "+str(riln))
    program.lblrescases=Label(text=str(riln)+" cases", bg="#9fe1e1")
    program.lblrescases.place(x=490, y=195)

  # Find the number of cases with diabetes
  def dcases(program):
    dbtn=0
    rown=0
  
    for i in range(462880):
      outcome=str(dataset.iloc[rown,5])

      if outcome.upper().find("TRUE"):
        dbtn=dbtn+1
        rown=rown+1
      else:
        rown=rown+1

    print("Number of cases with diabetes is: "+str(dbtn))
    program.lbldbtn=Label(text=str(dbtn)+" cases", bg="#9fe1e1")
    program.lbldbtn.place(x=490, y=240)

  # Find the number of cases with abnormal blood pressure
  def abbpcases(program):
    abbpn=0
    rown=0

    for i in range(462880):
      outcome=str(dataset.iloc[rown,7])
      
      if outcome.upper().find("TRUE"):
        abbpn=abbpn+1
        rown=rown+1
      else:
        rown=rown+1

    print("Number of cases with abnormal blood pressure is: "+str(abbpn))
    program.lblabbpn=Label(text=str(abbpn)+" cases", bg="#9fe1e1")
    program.lblabbpn.place(x=490, y=285)

  # Calculate the number of patients aged above 60
  def agedcases(program):
    agedn=0
    rown=0

    for i in range(462880):
      outcome=dataset.iloc[rown,4]
     
      if outcome>=60:
        agedn=agedn+1
        rown=rown+1
      else:
        rown=rown+1

    print("Number of cases with patients aged above 60 is: "+str(agedn))
    program.lblabbpn=Label(text=str(agedn)+" cases", bg="#9fe1e1")
    program.lblabbpn.place(x=490, y=330)

    rown=0
    aliven=0
    deadn=0

    print("\nEXECUTE subfunction agedcases()->aliven()..")
    for j in range(462880):
      status=str(dataset.iloc[rown,8]).upper()
      age=dataset.iloc[rown,4]
      
      if status=="ALIVE" and age>=60:
        aliven=aliven+1
        rown=rown+1
      else:
        rown=rown+1

    print("Number of patients aged above 60 and alive is: "+str(aliven))
    program.lblabbpn=Label(text=str(aliven)+" cases", bg="#9fe1e1")
    program.lblabbpn.place(x=490, y=355)

    print("\nEXECUTE subfunction agedcases()->deadn()..")
    deadn=agedn-aliven
    print("Number of patients aged above 60 and dead is: "+str(deadn))
    program.lblabbpn=Label(text=str(deadn)+" cases", bg="#9fe1e1")
    program.lblabbpn.place(x=490, y=375)

  def totaln(program):
    aliven=0
    rown=0

    for i in range(462880):
      outcome=str(dataset.iloc[rown,8]).upper()
      
      if outcome=="ALIVE":
        aliven=aliven+1
        rown=rown+1
      else:
        rown=rown+1

    print("Total no. of patients alive is: "+str(aliven))
    program.lblabbpn=Label(text=str(aliven)+" cases", bg="#9fe1e1")
    program.lblabbpn.place(x=490, y=465)
    
    deadn=462880-aliven
    print("Total no. of patients dead is: "+str(deadn))
    program.lblabbpn=Label(text=str(deadn)+" cases", bg="#9fe1e1")
    program.lblabbpn.place(x=490, y=495)

  def getcoordinates(program):
    # For debug only
    # print(pp.head(5))
    
    xc=int(program.ddx.get())
    yc=int(program.ddy.get())
    rown=0
    cases=0
    
    # Remove previous errors
    if program.lblerror:
      program.lblerror.place(x=0, y=1000)
    if program.lblspres:
      program.lblspres.place(x=1000, y=1000)
    if program.lbldscases:
      program.lbldscases.place(x=1000, y=1000)
    if program.lblspcasen:
      program.lblspcasen.place(x=1000,y=1000)
    if program.lblppdn:
      program.lblppdn.place(x=1000,y=1000)
    if program.lblpercn:
      program.lblpercn.place(x=1000,y=1000)
    if program.lblspacase:
      program.lblspacase.place(x=1000, y=1000)
    if program.lblspdcase:
      program.lblspdcase.place(x=1000, y=1000)
    if program.lblspabbp:
      program.lblspabbp.place(x=1000, y=1000)
    
    if xc>=1 and yc>=1 and xc<=20 and yc<=20:
      for i in range(462880):
        xcn=int(dataset.iloc[rown,2])
        ycn=int(dataset.iloc[rown,3])
        
        if xcn==xc and ycn==yc:
          cases=cases+1
          rown=rown+1
        else:
          rown=rown+1
      
      # Reset values to 0
      rown=0
      xcn=0
      ycn=0
    
      for j in range(400):
        xcn=int(pp.iloc[rown,0])
        ycn=int(pp.iloc[rown,1])
        if xcn==xc and ycn==yc:
          population_density=int(pp.iloc[rown,2])
          break
        else:
          rown=rown+1
      
      # Reset previous values
      rown=0
      xcn=0
      ycn=0
      rescases=0

      # Find cases with respiratory issues in specified coordinates      
      for r in range(462880):
        resoutcome=str(dataset.iloc[rown,6])
        xcn=int(dataset.iloc[rown,2])
        ycn=int(dataset.iloc[rown,3])
        
        if xcn==xc and ycn==yc and resoutcome.upper().find("TRUE"):
          rescases=rescases+1
          rown=rown+1
        else:
          rown=rown+1
      
      program.lblspres=Label(text=str(rescases)+" cases", bg="#9fe1e1")
      program.lblspres.place(x=175, y=245)
      
      rown=0
      xcn=0
      ycn=0
      dscases=0
      
      # Find cases with diabetes
      for d in range(462880):
        doutcome=str(dataset.iloc[rown,5])
        xcn=int(dataset.iloc[rown,2])
        ycn=int(dataset.iloc[rown,3])
        
        if xcn==xc and ycn==yc and doutcome.upper().find("TRUE"):
          dscases=dscases+1
          rown=rown+1
        else:
          rown=rown+1
      
      program.lbldscases=Label(text=str(dscases)+" cases", bg="#9fe1e1")
      program.lbldscases.place(x=175, y=285)

      rown=0
      xcn=0
      ycn=0
      abbpcases=0
      
      # Find cases with anomalies in blood pressure
      for bp in range(462880):
        bpoutcome=str(dataset.iloc[rown,7])
        xcn=int(dataset.iloc[rown,2])
        ycn=int(dataset.iloc[rown,3])
        
        if xcn==xc and ycn==yc and bpoutcome.upper().find("TRUE"):
          abbpcases=abbpcases+1
          rown=rown+1
        else:
          rown=rown+1
      
      program.lblspabbp=Label(text=str(abbpcases)+" cases", bg="#9fe1e1")
      program.lblspabbp.place(x=175, y=325)
      
      rown=0
      xcn=0
      ycn=0
      acases=0
      dcases=0
      
      # Find no. of people alive and dead
      for spalive in range(462880):
        status=str(dataset.iloc[rown,8]).upper()
        xcn=int(dataset.iloc[rown,2])
        ycn=int(dataset.iloc[rown,3])
        
        if xcn==xc and ycn==yc and status.upper().find("ALIVE"):
          acases=acases+1
          rown=rown+1
        else:
          rown=rown+1

      dcases=cases-acases
      
      program.lblspacase=Label(text=str(acases)+" cases", bg="#9fe1e1")
      program.lblspacase.place(x=175, y=365)
      program.lblspdcase=Label(text=str(dcases)+" cases", bg="#9fe1e1")
      program.lblspdcase.place(x=175, y=405)
      
      per_comp=cases/population_density * 100
      if per_comp==0:
        if program.lblstatus:
          program.lblstatus.place(x=1000, y=1000)
        print("You got lucky! There are no cases in your area.")
        program.lblstatus=Label(text="SAFE", fg="green", bg="#9fe1e1", font=("Arial", 14))
        program.lblstatus.place(x=175, y=560)
      elif per_comp>0 and per_comp<50:
        if program.lblstatus:
          program.lblstatus.place(x=1000, y=1000)
        print("You have an average risk.")
        program.lblstatus=Label(text="AT RISK", fg="yellow", bg="#9fe1e1", font=("Arial", 13))
        program.lblstatus.place(x=175, y=560)
      elif per_comp>=50 and per_comp<80:
        if program.lblstatus:
          program.lblstatus.place(x=1000 ,y=1000)
        print("You are at moderate risk!")
        program.lblstatus=Label(text="MODERATE RISK", fg="orange", bg="#9fe1e1", font=("Arial", 13))
        program.lblstatus.place(x=175, y=560)
      elif per_comp>=80:
        if program.lblstatus:
          program.lblstatus.place(x=1000, y=1000)
        print("You have a high risk!")
        program.lblstatus=Label(text="HIGH RISK", fg="red", bg="#9fe1e1", font=("Arial", 13))
        program.lblstatus.place(x=175, y=560)
      elif per_comp==100:
        if program.lblstatus:
          program.lblstatus.place(x=1000, y=1000)
        print("You are infected!")
        program.lblstatus=Label(text="INFECTED", fg="red", bg="#9fe1e1", font=("Arial", 13))
        program.lblstatus.place(x=175, y=560)
      
      print("In area x="+str(xcn)+" and y="+str(ycn)+", the no. of cases is: "+str(cases))
      print("Population Density is: "+str(population_density))
      print("The percentage composition is: "+str(per_comp)+"%")
      
      program.lblspcasen=Label(text=str(cases)+" cases", bg="#9fe1e1")
      program.lblspcasen.place(x=175, y=445)
      program.lblppdn=Label(text=str(population_density), bg="#9fe1e1")
      program.lblppdn.place(x=175, y=485)
      program.lblpercn=Label(text=str(int(per_comp))+"%", bg="#9fe1e1")
      program.lblpercn.place(x=175, y=525)
    else:
      
      program.lblerror.place(x=4, y=200)

window=Tk()
programwin=Window(window)
window.title('Application')
window.geometry("700x600+10+10")
window.configure(bg="#9fe1e1")
window.mainloop()
