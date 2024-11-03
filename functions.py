def algo_question(file_name: str) -> str:
    """
    minimum sun of k even numbers:
    S = k * 1
    n >= Smin_odd = k
    n_odd = n - (k - 1) * 1 and n_odd mod 2 = 1 so we can be n  represented as the sum k odd positive numbers
    n = (1+1+....+1) * (k-1) + n_odd
    similarly with even
    Smin_even = k * 2
    n >= Smin_even = k
    n_even = n - (k - 1) * 2 and n_even mod 2 = 0 so we can be n  represented as the sum k even numbers
    n = (2+2+....+2) * (k-1) + n_odd


    """
    with open(file_name, 'r') as file:
        t = int(file.readline().strip())
        result = []
        for _ in range(t):
            n, k = map(int, file.readline().strip().split())
            n_odd = n - (k - 1)
            if n_odd > 0 and n_odd % 2 == 1:
                result.append("YES")
                result.append(f"{n_odd}" + " 1" * (k - 1))
                continue
            n_even = n - 2 * (k - 1)
            if n_even > 0 and n_even % 2 == 0:
                result.append("YES")
                result.append(f"{n_even}" + " 2" * (k - 1))
                continue
            result.append("NO")
    return "\n".join(result)


