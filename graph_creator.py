import subprocess

count=0
for i in range(80,301, 10):
    v, e=i,i
    count+=1
    with open(f"input/{count}-graph{v}{2*e}.txt", "w") as f:
        subprocess.run(["./graph-generator/generator.out",f"{v}",f"{2*e}"], stdout=f)