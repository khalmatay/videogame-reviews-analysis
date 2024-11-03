def algo_question() -> None:
    with open('input.txt', 'r') as file:
        t = int(file.readline().strip())
        for _ in range(t):
            n, k = map(int, file.readline().strip().split())
            n_even = n - (k - 1)
            if n_even > 0 and n_even % 2 == 1:
                print("YES")
                s = ""
                for j in range(k-1):
                    s += " 1"
                print(str(n_even) + s)
                continue
            n_odd = n - 2 * (k - 1)
            if n_odd > 0 and n_odd % 2 == 0:
                print("YES")
                s =""
                for j in range(k-1):
                    s += " 2"
                print(str(n_even) + s)
                continue
            print("NO")
algo_question()
