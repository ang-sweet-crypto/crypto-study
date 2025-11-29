from hashlib import sha256

def parse_data(path="data.txt"):
    with open(path, "r") as f:
        lines = [line.strip() for line in f if line.strip()]
    P = int(lines[0].split("=")[1])
    e = int(lines[1].split("=")[1])
 
    pairs = []
    for line in lines[3:]:
        n_str, M_str = line.split(",", 1)
        pairs.append((int(n_str), int(M_str)))
    return P, e, pairs

def valid_prefix(c, r, pairs):
    """检查 r 比特前缀 c 是否可行"""
    mask_r = (1 << r) - 1
    for n, M in pairs:
        # 奇偶性约束：需要 M + t*n 与 c 同奇偶；n 为奇数 => t 的奇偶可选
        need_odd = (M - c) & 1  # 1 则 t=1；0 则 t ∈ {0,2}
        t_list = [1] if need_odd else [0, 2]
        ok = False
        for t in t_list:
            # 只用到低 r+1 比特即可判断 (B & c)==0 的低 r 比特
            D_low = (M + t * n - c) & ((1 << (r + 1)) - 1)
            B_low = (D_low >> 1) & mask_r
            if (B_low & c) == 0:
                ok = True
                break
        if not ok:
            return False
    return True

def recover_C(pairs, bits):
    """按位从低到高恢复 C"""
    cands = [0]
    for r in range(1, bits + 1):
        next_cands = []
        for c in cands:
            for add in (0, 1 << (r - 1)):
                cand = c | add
                if valid_prefix(cand, r, pairs):
                    next_cands.append(cand)
        # 通常会收敛到唯一候选
        cands = sorted(set(next_cands))
        if not cands:
            raise ValueError("No candidate for C at bit %d" % r)
    if len(cands) != 1:
        # 若仍有多个，用 C < P 过滤（理论上这里应唯一）
        return min(cands)
    return cands[0]

def main():
    P, e, pairs = parse_data("data.txt")
    C = recover_C(pairs, P.bit_length())  # 逐位恢复 C
    # 求 d = e^{-1} mod (P-1) （Python 3.8+ 支持 pow 的模逆）
    d = pow(e, -1, P - 1)
    msg = pow(C, d, P)
    print("C =", C)
    print("msg =", msg)
    print("flag = SYC{%s}" % sha256(str(msg).encode()).hexdigest())

if __name__ == "__main__":
    main()