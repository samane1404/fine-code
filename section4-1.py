import unittest


# تابع مورد نظر برای تست
def find_unique_pairs(nums, target):
    seen = set()  # مجموعه برای ذخیره اعداد دیده‌شده
    pairs = set()  # مجموعه برای ذخیره جفت‌های غیر تکراری

    # پیمایش لیست
    for num in nums:
        complement = target - num

        # اگر تفاوت در مجموعه دیده‌شده باشد، یعنی جفت مورد نظر پیدا شده است
        if complement in seen:
            # برای جلوگیری از تکراری بودن، جفت را به صورت مرتب اضافه می‌کنیم
            pairs.add(tuple(sorted((complement, num))))

        # عدد فعلی را به مجموعه اضافه می‌کنیم
        seen.add(num)

    return list(pairs)


# کلاس تست واحد
class TestFindUniquePairs(unittest.TestCase):

    def test_case_1(self):
        # ورودی با جفت‌های مختلف
        nums = [2, 7, 11, 15, 6, 5, 3]
        target = 9
        expected = [(2, 7), (3, 6)]
        result = find_unique_pairs(nums, target)
        self.assertEqual(sorted(result), sorted(expected))

    def test_case_2(self):
        # ورودی بدون جفت‌های مجاز
        nums = [1, 2, 3, 4]
        target = 10
        expected = []
        result = find_unique_pairs(nums, target)
        self.assertEqual(result, expected)

    def test_case_3(self):
        # ورودی با تنها یک جفت
        nums = [1, 8, 11, 7]
        target = 9
        expected = [(1, 8)]
        result = find_unique_pairs(nums, target)
        self.assertEqual(sorted(result), sorted(expected))

    def test_case_4(self):
        # ورودی با تکرار اعداد
        nums = [5, 5, 5, 5, 5]
        target = 10
        expected = [(5, 5)]  # فقط یک جفت معتبر وجود دارد
        result = find_unique_pairs(nums, target)
        self.assertEqual(sorted(result), sorted(expected))

    def test_case_5(self):
        # ورودی با جفت‌های تکراری
        nums = [1, 2, 7, 2, 7]
        target = 9
        expected = [(2, 7)]
        result = find_unique_pairs(nums, target)
        self.assertEqual(sorted(result), sorted(expected))

    def test_case_6(self):
        # ورودی با هیچ عددی
        nums = []
        target = 9
        expected = []
        result = find_unique_pairs(nums, target)
        self.assertEqual(result, expected)

    def test_case_7(self):
        # ورودی با یک عدد هدف و یک عدد لیست
        nums = [5]
        target = 10
        expected = []
        result = find_unique_pairs(nums, target)
        self.assertEqual(result, expected)

    def test_case_8(self):
        # ورودی با جفت‌های ممکن ولی ترتیب مختلف
        nums = [3, 6, 7, 2, 3, 7]
        target = 9
        expected = [(2, 7), (3, 6)]
        result = find_unique_pairs(nums, target)
        self.assertEqual(sorted(result), sorted(expected))


# اجرای تست‌ها
if __name__ == '__main__':
    unittest.main()
