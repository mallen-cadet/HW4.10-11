

    return (a_count, e_count, i_count, o_count, u_count)



user_input = input("Enter a string: ")

a_count, e_count, i_count, o_count, u_count = count_vowels(user_input)

# total number of vowels
total_vowels = a_count + e_count + i_count + o_count + u_count
print(f"The total number of vowels in the input string is:",total_vowels)


#count of each vowel
# print("You used 'a'", a_count, "times")
# print("You used 'e'", e_count, "times")
# print("You used 'i'", i_count, "times")
# print("You used 'o'", o_count, "times")
# print("You used 'u'", u_count, "times")
# Calculate and display the counts and percentages
if total_vowels > 0:
    print(f"a: {a_count} ({(a_count / total_vowels) * 100:.2f}%)")
    print(f"e: {e_count} ({(e_count / total_vowels) * 100:.2f}%)")
    print(f"i: {i_count} ({(i_count / total_vowels) * 100:.2f}%)")
    print(f"o: {o_count} ({(o_count / total_vowels) * 100:.2f}%)")
    print(f"u: {u_count} ({(u_count / total_vowels) * 100:.2f}%)")
else:
    print("No vowels found in the input string.")
