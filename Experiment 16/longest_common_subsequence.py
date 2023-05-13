def longest_common_subsequence(str1, str2):
	subsequences1 = generate_subsequences(str1)
	subsequences2 = generate_subsequences(str2)
	lcs = ""
	for subsequence1 in subsequences1:
		for subsequence2 in subsequences2:
			if subsequence1 == subsequence2 and len(subsequence1) > len(lcs):
				lcs = subsequence1
	return lcs

def generate_subsequences(s):
	subsequences = []
	generate_subsequences_helper(s, "", 0, subsequences)
	return subsequences

def generate_subsequences_helper(s, subsequence, index, subsequences):
	if index == len(s):
		subsequences.append(subsequence)
		return
	generate_subsequences_helper(s, subsequence, index + 1, subsequences)
	generate_subsequences_helper(s, subsequence + s[index], index + 1, subsequences)

if __name__ == '__main__':
	str1 = "RAGTABEMNF"
	str2 = "GTXAYBMUFF"
	lcs = longest_common_subsequence(str1, str2)
	print("Length of LCS is ", len(lcs))
