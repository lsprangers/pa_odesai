
from iacorpus import load_dataset

dataset = load_dataset('fourforums')
print(dataset.dataset_metadata)
for discussion in dataset:
    print(discussion)
    for post in discussion:
        print(post)
