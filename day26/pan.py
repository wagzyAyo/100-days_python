import pandas as pd

student_dict = {
    "student": ["Angela", "James", "Lilly"],
    "score": [56, 76, 98]
}


new_data_panda_frame = pd.DataFrame(student_dict)

# for (key, value) in new_data_panda_frame.items():
# print(value)

for (index, value) in new_data_panda_frame.iterrows():
    if value.score >= 70:
        print(value)
