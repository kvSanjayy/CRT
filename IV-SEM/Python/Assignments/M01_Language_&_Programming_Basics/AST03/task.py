def Student_Grade_System(name: str, n1: int, n2: int, n3: int) -> str:
    avg = (n1 + n2 + n3) / 3

    if avg >= 40:
        status = "Pass"
        return f"Average grade: {avg:.1f}, Status: {status}"
    else:
        status = "fail"
        avg = int(avg * 100) / 100   # truncate to 2 decimals
        return f"Average grade: {avg:.2f}, Status: {status}"


if __name__ == '__main__':
    name = input()
    n1, n2, n3 = list(map(int, input().split()))
    print(Student_Grade_System(name, n1, n2, n3))