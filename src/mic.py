def line_splitter(val, delimiter="\t"):
	if delimiter=="\t":
		return val.replace("\n", "").split(delimiter)
	else:
		return val.replace("\n", "").replace("\t", " ").split(delimiter)

def duplication_modifier(val):
	# rename duplicated column title
	val_idx = 0
	val_set = set()
	while val_idx < len(val):
		if val[val_idx] in val_set:
			tail = -1
			while val[val_idx] in val_set:
				tail += 1
				val[val_idx] = f"{val[val_idx]}_{str(tail)}"
		val_set.add(val[val_idx])
		val_idx += 1
	return val
