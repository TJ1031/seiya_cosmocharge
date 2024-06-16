import numpy as np
from scipy.stats import poisson

def simulate_seven_hit_prob(high_prob_transition, num_simulations=100000):
    # 7.04回転を行う
    initial_spins = 7.04
    
    # 7揃い高確への移行確率
    transition_prob = high_prob_transition
    
    # 7揃い高確中の試行数
    high_prob_spins = 5.43
    
    # 7揃いの確率
    hit_prob = 1 / 70.53
    
    # シミュレーションの実行
    hit_count = 0
    for _ in range(num_simulations):
        # 高確への移行判定
        if np.random.rand() <= transition_prob:
            # 高確中の7揃い判定
            lambda_poisson = high_prob_spins * hit_prob
            if np.random.poisson(lambda_poisson) > 0:
                hit_count += 1
    
    # 7揃いが発生する確率
    hit_probability = hit_count / num_simulations
    return hit_probability

# 高確への移行確率を設定（例：50%）
high_prob_transition = 0.50

# シミュレーションの実行
prob = simulate_seven_hit_prob(high_prob_transition)
print(f"7揃いが発生する確率: {prob:.2%}")