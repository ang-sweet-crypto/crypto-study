from sage.all import *
import time

def generate_hnp_instance(n_bits, k_bits, d_samples):
    """
    生成 HNP 实例 (模拟 Oracle)
    """
    p = next_prime(2^n_bits)
    x = randint(1, p-1)
    inputs = []
    outputs = []
    
    # 掩码用于计算区间
    diff = p >> k_bits
    
    for _ in range(d_samples):
        t = randint(1, p-1)
        val = (x * t) % p
        # 模拟 MSB 泄露：取区间中点作为近似值 u
        # 这能最大化减少误差 |val - u| <= p / 2^{k+1}
        u = val - (val % diff) + (diff // 2)
        inputs.append(t)
        outputs.append(u)
        
    return p, x, inputs, outputs

def solve_hnp_with_lattice(p, inputs, outputs, k_bits):
    """
    使用 Kannan Embedding 技术 + LLL 求解 HNP
    """
    d = len(inputs)
    # [关键修正] 权重设置
    # 目标向量 v = (e_1, ..., e_d, x, W)
    # 我们希望各分量平衡。e_i 约为 p/2^k。
    # 如果 W 设为 p，则最后一维太大，LLL 会忽略它。
    # 应将 W 设为与 expected_error 同数量级。
    
    expected_error = p // (2**k_bits)
    W = expected_error 
    
    # 构造矩阵 M (d+2) x (d+2)
    # Row 0..d-1: p * I_d
    # Row d:      (t1, ..., td, 1, 0)
    # Row d+1:    (-u1, ..., -ud, 0, W)
    
    mat_size = d + 2
    M = Matrix(ZZ, mat_size, mat_size)
    
    for i in range(d):
        M[i, i] = p
        
    for i in range(d):
        M[d, i] = inputs[i]
    M[d, d] = 1
    
    for i in range(d):
        M[d+1, i] = -outputs[i]
    M[d+1, d+1] = W
    
    # 执行 LLL
    try:
        L_reduced = M.LLL()
    except:
        return None
    
    # 搜索解向量
    for row in L_reduced:
        # 检查最后一维是否为 ±W
        if abs(row[d+1]) == W:
            potential_x = row[d]
            if row[d+1] < 0: # 符号修正
                potential_x = -potential_x
            
            potential_x = potential_x % p
            
            # 验证：取第一个样本检查误差
            t0 = inputs[0]
            u0 = outputs[0]
            diff_val = (potential_x * t0) % p - u0
            # 模 p 距离
            if diff_val > p//2: diff_val -= p
            elif diff_val < -p//2: diff_val += p
            
            if abs(diff_val) <= expected_error * 2: # 允许少量松弛
                return potential_x
    return None

def run_experiment_loop():
    print("=== HNP Diffie-Hellman MSB 攻击复现与统计 ===")
    print(f"{'Config':<30} | {'Trials':<8} | {'Time(s)':<10} | {'Success Rate'}")
    print("-" * 70)
    
    # 实验参数组
    # 1. 论文复现级：n=128, k=MSB位数。
    # 根据论文，需要 d*k > n。
    params = [
        # [A] 极高泄露 (Easy): k=64 (一半), d=5 (2.5倍冗余)
        {"n": 128, "k": 64, "d": 5},
        
        # [B] 典型场景 (Medium): k=32 (1/4), d=10 (2.5倍冗余)
        {"n": 128, "k": 32, "d": 10},
        
        # [C] 论文边界 (Hard): k=8, d=25 (总信息 200 bit > 128 bit)
        # 维度 d+2 = 27, LLL 仍然有效但开始有压力
        {"n": 128, "k": 8,  "d": 25},
        
        # [D] 高维度测试 (Very Hard): k=4, d=50 (总信息 200 bit)
        # 维度 d+2 = 52, LLL 可能会失败，测试成功率
        {"n": 128, "k": 4,  "d": 50},
    ]
    
    MAX_TRIALS = 100 # 单组最大尝试次数
    
    for param in params:
        n, k, d = param["n"], param["k"], param["d"]
        desc = f"n={n}, k={k}, d={d}"
        
        success = False
        trials = 0
        total_time = 0
        
        while not success and trials < MAX_TRIALS:
            trials += 1
            p, real_x, inputs, outputs = generate_hnp_instance(n, k, d)
            
            t0 = time.time()
            rec_x = solve_hnp_with_lattice(p, inputs, outputs, k)
            t1 = time.time()
            
            total_time += (t1 - t0)
            
            if rec_x == real_x:
                success = True
        
        # 统计输出
        if success:
            rate = 100.0 / trials
            avg_time = total_time / trials
            print(f"{desc:<30} | {trials:<8} | {avg_time:<10.4f} | {rate:.1f}%")
        else:
            print(f"{desc:<30} | >{MAX_TRIALS:<7} | N/A        | 0%")

if __name__ == "__main__":
    run_experiment_loop()

