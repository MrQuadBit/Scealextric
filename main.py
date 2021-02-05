import pandas as pd
from random import randint
import numpy as np

F_MIDPOINTS = "Veale's script midpoints.xlsx"
F_NOC_LIST = "Veales The NOC List.xlsx" 
F_ACTIONS = "Veale's category actions.xlsx"

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

def substituteMidPoints(midpoints, df):
	column_when_subject = np.array(df["When Subject"])
	positions = []
	for tup in midpoints:
		pos = []
		for index, item in enumerate(column_when_subject):
			if not isinstance(item, float):
				if tup[0] in item:
					pos.append(index)
		if not pos:
			column_when_object = np.array(df["When Object"])
			for index, item in enumerate(column_when_object):
				if not isinstance(item, float):
					if tup[0] in item:
						pos.append(index)
			pos.append("Object")
		else:
			pos.append("Subject")
		positions.append(pos)
	return positions

def main():
	df_midpoints = pd.read_excel(F_MIDPOINTS, engine="openpyxl") #use openpyxl bc the default engine does not support xlsx formmats
	skeleton_midpoints = getSkeleton(df_midpoints, 4)

	df_category_actions = pd.read_excel(F_ACTIONS, engine="openpyxl")
	skeleton_characters = substituteMidPoints(skeleton_midpoints, df_category_actions)
	for index, item in enumerate(skeleton_midpoints):
		print(skeleton_midpoints[index], skeleton_characters[index])


if __name__ == "__main__":
	main()