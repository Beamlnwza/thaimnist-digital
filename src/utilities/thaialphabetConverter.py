def convert_to_thai_alphabet(num):
    if num < 0 or num > 43:
        return "Invalid number"

    thai_alphabets = "กขฃคฅฆงจฉชซฌญฎฏฐฑฒณดตถทธนบปผฝพฟภมยรฤลฦวศษสหฮ"
    return thai_alphabets[num]
