def trapped_cell(n: int, m: int) -> int:
    def valeurs(posi):
        x, y = posi
        if x == y == 0:
            return 0
        abs_x, abs_y = abs(x), abs(y)
        if y <= -abs_x:
            start = (2 * y + 1) ** 2 - x + 3 * abs_y - 1
        elif x <= -abs_y:
            start = (2 * x + 1) ** 2 + y + 5 * abs_x - 1
        elif y >= abs_x:
            start = (2 * y - 1) ** 2 + x + 7 * abs_y - 1
        elif x >= abs_y:
            start = (2 * x - 1) ** 2 - y + abs_x - 1
        return start

    visited = set()
    pos = (0, 0)

    def cases():
        return [(pos[0] + x, pos[1] + y) for x, y in [(m, n), (m, -n), (n, -m), (-n, -m), (-m, -n), (-m, n), (-n, m), (n, m)]]

    visited.add(pos)
    possibilites = cases()

    while possibilites:
        pos = min(possibilites, key=lambda elt: valeurs(elt))
        if pos in visited:
            break
        visited.add(pos)
        possibilites = [new_pos for new_pos in cases() if new_pos not in visited]

    return valeurs(pos)

print(trapped_cell(1, 2))
