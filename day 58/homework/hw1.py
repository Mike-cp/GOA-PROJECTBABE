increase_staff_count = lambda x: x + 5

staff_productivity = lambda x, y: x * y

is_staff_id_even = lambda x: x % 2 == 0

convert_staff_temps = lambda temps: list(map(lambda c: (c * 9/5) + 32, temps))

staff_name_starts_with_a = lambda s: s.startswith('A')

add_ten_to_staff_scores = lambda scores: list(map(lambda x: x + 10, scores))

staff_names_uppercase = lambda names: list(map(lambda s: s.upper(), names))

staff_name_lengths = lambda names: list(map(len, names))

square_staff_ratings = lambda ratings: list(map(lambda x: x ** 2, ratings))

staff_ids_to_strings = lambda ids: list(map(str, ids))

greet_staff_members = lambda names: list(map(lambda name: "Hello " + name, names))

deduct_five_from_scores = lambda scores: list(map(lambda x: x - 5, scores))

triple_staff_points = lambda points: list(map(lambda x: x * 3, points))

convert_staff_temps_v2 = lambda temps: list(map(lambda c: (c * 9/5) + 32, temps))

staff_scores_above_50 = lambda scores: list(map(lambda x: x > 50, scores))

filter_even_staff_ids = lambda ids: list(filter(lambda x: x % 2 == 0, ids))

filter_scores_above_10 = lambda scores: list(filter(lambda x: x > 10, scores))

filter_long_staff_names = lambda names: list(filter(lambda s: len(s) > 5, names))

remove_blank_staff_names = lambda names: list(filter(lambda s: s != "", names))

positive_staff_ratings = lambda ratings: list(filter(lambda x: x > 0, ratings))

staff_names_a = lambda names: list(filter(lambda name: name.startswith('A'), names))

staff_ids_divisible_by_3 = lambda ids: list(filter(lambda x: x % 3 == 0, ids))

staff_names_with_e = lambda names: list(filter(lambda name: 'e' in name, names))

remove_missing_staff = lambda staff: list(filter(lambda x: x is not None, staff))

staff_scores_below_equal_50 = lambda scores: list(filter(lambda x: x <= 50, scores))

# Example usages
print(increase_staff_count(10))
print(staff_productivity(3, 4))
print(is_staff_id_even(8))
print(convert_staff_temps([0, 100, -40]))
print(staff_name_starts_with_a("Alice"))
print(add_ten_to_staff_scores([1, 2, 3]))
print(staff_names_uppercase(["john", "sara"]))
print(staff_name_lengths(["john", "samantha"]))
print(square_staff_ratings([1, 2, 3]))
print(staff_ids_to_strings([101, 102, 103]))
print(greet_staff_members(["Alice", "Bob"]))
print(deduct_five_from_scores([10, 15, 20]))
print(triple_staff_points([1, 2, 3]))
print(convert_staff_temps_v2([0, 100, -40]))
print(staff_scores_above_50([10, 60, 30]))
print(filter_even_staff_ids([1, 2, 3, 4]))
print(filter_scores_above_10([5, 15, 25]))
print(filter_long_staff_names(["short", "longername"]))
print(remove_blank_staff_names(["john", "", "doe"]))
print(positive_staff_ratings([-1, 0, 1, 2]))
print(staff_names_a(["Alice", "Bob", "Anna"]))
print(staff_ids_divisible_by_3([3, 4, 9, 10]))
print(staff_names_with_e(["Peter", "Mike", "Tom"]))
print(remove_missing_staff([1, None, 2, None, 3]))
print(staff_scores_below_equal_50([10, 60, 30]))
