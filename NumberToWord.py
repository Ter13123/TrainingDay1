def number_to_words(n):
    
    ones = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    tens = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']

    def three_digits(n):
        if n < 10:
            return ones[n]
        elif n < 100:
            return two_digits(n)
        else:
            return ones[n // 100] + ' hundred ' + two_digits(n % 100) if n % 100 != 0 else ones[n // 100] + ' hundred'

    def two_digits(n):
        if n < 10:
            return ones[n]
        elif n < 20:
            return teens[n - 10]
        else:
            return tens[n // 10] + ' ' + ones[n % 10] if n % 10 != 0 else tens[n // 10]

    if n < 0 or n >= 1000000:
        return 'Number out of range'
    elif n < 10:
        return ones[n]
    elif n < 100:
        return two_digits(n)
    elif n < 1000:
        return three_digits(n)
    elif n < 1000000:
        return number_to_words(n // 1000) + ' thousand ' + three_digits(n % 1000) if n % 1000 != 0 else number_to_words(n // 1000) + ' thousand'

n = int(input("Enter a number between 1 and 1000000: "))

print(number_to_words(n))