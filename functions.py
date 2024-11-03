def algo_question(file_name: str) -> str:
    with open(file_name, 'r') as file:
        t = int(file.readline().strip())
        result = []
        for _ in range(t):
            n, k = map(int, file.readline().strip().split())
            n_even = n - (k - 1)
            if n_even > 0 and n_even % 2 == 1:
                result.append("YES")
                result.append(f"{n_even}" + " 1" * (k - 1))
                continue
            n_odd = n - 2 * (k - 1)
            if n_odd > 0 and n_odd % 2 == 0:
                result.append("YES")
                result.append(f"{n_odd}" + " 2" * (k - 1))
                continue
            result.append("NO")
    return "\n".join(result)


