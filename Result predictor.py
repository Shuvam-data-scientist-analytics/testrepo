t_math=int(input("Enter your 10th marks(math):"))
p1_math=int(input("Enter 12th pre board best marks(math):"))
p2_math=int(input("Enter 11th final best marks(math):"))
p_math=int(input("Enter practical marks(math):"))

math1 = (t_math/100) * (0.3*80)
math2 = (p1_math/100) * (0.4*80)
math3 = (p2_math/100) * (0.3*80)
math_marks = math1 + math2 + math3 + p_math


t_phy=int(input("Enter your 10th marks(science):"))
p1_phy=int(input("Enter 12th pre board best marks(physics):"))
p2_phy=int(input("Enter 11th final best marks(physics):"))
p_phy=int(input("Enter practical marks(physics):"))

phy1 = (t_phy/100) * (0.3*70)
phy2 = (p1_phy/100) * (0.4*70)
phy3 = (p2_phy/100) * (0.3*70)
phy_marks = phy1 + phy2 + phy3 + p_phy

t_chem=int(input("Enter your 10th marks(science):"))
p1_chem=int(input("Enter 12th pre board best marks(chemistry):"))
p2_chem=int(input("Enter 11th final best marks(chemistry):"))
p_chem=int(input("Enter practical marks(chemistry):"))

chem1 = (t_chem/100) * (0.3*70)
chem2 = (p1_chem/100) * (0.4*70)
chem3 = (p2_chem/100) * (0.3*70)
chem_marks = chem1 + chem2 + chem3 + p_chem

t_beng=int(input("Enter your 10th marks(bengali):"))
p1_beng=int(input("Enter 12th pre board best marks(bengali):"))
p2_beng=int(input("Enter 11th final best marks(bengali):"))
p_beng=int(input("Enter practical marks(bengali):"))

beng1 = (t_beng/100) * (0.3*80)
beng2 = (p1_beng/100) * (0.4*80)
beng3 = (p2_beng/100) * (0.3*80)
beng_marks = beng1 + beng2 + beng3 + p_beng

t_eng=int(input("Enter your 10th marks(english):"))
p1_eng=int(input("Enter 12th pre board best marks(english):"))
p2_eng=int(input("Enter 11th final best marks(english):"))
p_eng=int(input("Enter practical marks(english):"))

eng1 = (t_eng/100) * (0.3*80)
eng2 = (p1_eng/100) * (0.4*80)
eng3 = (p2_eng/100) * (0.3*80)
eng_marks = eng1 + eng2 + eng3 + p_eng

t_com=int(input("Enter your 10th marks(computer):"))
p1_com=int(input("Enter 12th pre board best marks(computer):"))
p2_com=int(input("Enter 11th final best marks(computer):"))
p_com=int(input("Enter practical marks(computer):"))

com1 = (t_com/100) * (0.3*70)
com2 = (p1_com/100) * (0.4*70)
com3 = (p2_com/100) * (0.3*70)
comp_marks = com1 + com2 + com3 + p_com


print("|---------------------------------HERE IS YOUR PREDICTED RESULT---------------------------------|")
print("|______Engilsh------------------------:",eng_marks,"--------------------------------------------|")
print("|______Mathematics--------------------:",math_marks,"-------------------------------------------|")
print("|______Physics------------------------:",phy_marks,"--------------------------------------------|")
print("|______Chemistry----------------------:",chem_marks,"-------------------------------------------|")
print("|______Bengali------------------------:",beng_marks,"-------------------------------------------|")
print("|______Computer Science---------------:",comp_marks,"-------------------------------------------|")

total_m = eng_marks + math_marks + phy_marks + chem_marks + beng_marks + comp_marks
p = (total_m/600)*100
print("Total:-----",total_m)
print("Your percentage:----",p)









