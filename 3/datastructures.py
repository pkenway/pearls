
letter_definitions = {
    'A' : [
        '1*4- ,2-A,4- ',
        '1*3- ,4-A,3- ',
        '1*2- ,2-A,2- ,2-A,2- ',
        '1*1- ,8-A-1- ',
        '2*2-A,6- ,2-A'],
    'I' : [
        '3*6-I',
        '3*2- ,2-I,2- ',
        '3*6-I'],
    }


def banner(letter):

    if letter not in letter_definitions:
        return None

    definition = letter_definitions[letter]
    rows = []
    for block in definition:
        print(block)
        block_count = int(block[0])
        chars = block[2:]
        for row in range(0,block_count):
            row_text = ''
            for charset in chars.split(','):
                print(charset)
                set_parts = charset.split('-')
                row_text += set_parts[1] * int(set_parts[0])
            rows.append(row_text)
    
    for row in rows:
        print(row)


days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def date_diff(date1, date2):
    # just dealing with month/day here
    return abs(get_day_of_year(date1) - get_day_of_year(date2))

def get_day_of_year(date):
    date_parts = date.split('/')
    month, day = int(date_parts[0]), int(date_parts[1])
    year_day = 0
    for i in range(0, month - 1):
        year_day += days_per_month[i]
    return year_day + day

if __name__ == '__main__':
    print(date_diff('3/15','2/1'))