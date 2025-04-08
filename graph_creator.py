import subprocess

count=0
for i in range(20,41, 1):
    v, e=i,i
    count+=1
    with open(f"input_ET_BF/{count}-graph{20}{e}.txt", "w") as f:
        subprocess.run(["./graph-generator/generator.out",f"{20}",f"{e}"], stdout=f)