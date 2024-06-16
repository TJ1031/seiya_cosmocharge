import numpy as np
import streamlit as st

def simulate_initial_hit_prob(high_prob_transition, num_simulations=100000):
    initial_spins = 7.16
    high_prob_spins = 5.43
    hit_prob = 1 / 70.53
    
    total_hits = 0
    total_spins = 0

    for _ in range(num_simulations):
        spins = initial_spins
        if np.random.rand() <= high_prob_transition / 100.0:  # 高確移行率をパーセンテージで受け取る
            for spin in range(int(np.ceil(high_prob_spins))):
                spins += 1
                if np.random.rand() <= hit_prob:
                    total_hits += 1
                    total_spins += spins
                    break
            else:
                # 7揃いが発生しなかった場合
                total_spins += spins
        else:
            # 高確に移行しなかった場合
            total_spins += initial_spins

    if total_hits > 0:
        average_spins_until_hit = total_spins / total_hits
        initial_hit_prob = 1 / average_spins_until_hit
    else:
        initial_hit_prob = 0  # 初当たりが発生しなかった場合

    return initial_hit_prob

st.title('星矢7揃い初当たり確率シミュレーション')
high_prob_transition = st.slider('コスモチャージへの移行確率 (%)', 0, 100, 50)  # 0から100のスライダー
if st.button('シミュレーションを実行'):
    prob = simulate_initial_hit_prob(high_prob_transition)
    if prob > 0:
        st.write(f"7揃いの初当たり確率: 1/{1/prob:.2f}")
    else:
        st.write("シミュレーション中に初当たりが発生しませんでした。試行回数を増やしてください。")