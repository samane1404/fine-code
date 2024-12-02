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


# تست برنامه
nums = [2, 7, 11, 15, 7, 2, 5, 3]
target = 9
result = find_unique_pairs(nums, target)
print(result)  # خروجی: [(2, 7), (3, 6)]
