def median(iterable):
    items = sorted(iterable)
    median_index = (len(items)-1) / 2
    if len(items) % 2 == 0:
        raise ValueError("median args is empty")
    if len(items) % 2 != 0:
        return items[median_index]
    return (items[median_index] + items[median_index+1])/2

def main():
    try:
        median([])

    except ValueError as e:
        print("payload", e)

main()