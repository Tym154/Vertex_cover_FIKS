import subprocess

def create_input(dir):
    count=0
    for i in range(0,100, 1):
        v, e=i,i
        count+=1
        with open(f"{dir}/{count}-graph{v}{3*e}.txt", "w") as f:
            subprocess.run(["./graph-generator/generator.out",f"{v}",f"{3*e}"], stdout=f)

create_input("inputs/input_VT_shared")