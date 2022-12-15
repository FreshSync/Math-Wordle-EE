from tqdm import tqdm

list = [1, 2, 3, 4, 5, 6]

for i in tqdm (range(len(list)), desc="Loading...", ascii=False, ncols=75):
    print(i)