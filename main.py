import pandas as pd
from random import randint

F_MIDPOINTS = "Veale's script midpoints.xlsx"

def getOnestringFromStrings(strings):
	string_list = strings.split()
	new_string = string_list[randint(0, len(string_list)-1)]
	return new_string.replace(",","")

def getTupleFromDataframe(df, index):
	before_midpoint = getOnestringFromStrings(df.iloc[index][df.columns[0]])
	midpoint = getOnestringFromStrings(df.iloc[index][df.columns[1]])
	after_midpoint = getOnestringFromStrings(df.iloc[index][df.columns[2]])
	new_tuple = (before_midpoint, midpoint, after_midpoint)
	return new_tuple

def getSkeleton(df, num_tuples):
	skeleton = []
	#Firts tupple
	first_index = randint(0, df.shape[0]-3)
	first_tuple = getTupleFromDataframe(df, first_index)
	skeleton.append(first_tuple)
	#Helpers
	after_midpoint = first_tuple[2]
	num_tuples -= 1
	#Remaining tuples
	for i in range(num_tuples):
		new_df = df[df["Before Midpoint"] == after_midpoint]
		new_index = randint(0, new_df.shape[0]-1)
		new_tuple = getTupleFromDataframe(new_df, new_index)
		skeleton.append(new_tuple)
		after_midpoint = new_tuple[2]
	return skeleton

def main():
	df_midpoints = pd.read_excel(F_MIDPOINTS, engine="openpyxl") #use openpyxl bc the default engine does not support xlsx formmats
	skeleton = getSkeleton(df_midpoints, 4)
	for tup in skeleton:
		print(tup)

if __name__ == "__main__":
	main()