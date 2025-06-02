import random
import statistics
import numpy as np
import matplotlib.pyplot as plt
from enum import Enum

HOUSE_EDGE = .99  # House edge reduces payouts
WIN_PROBABILITY = 0.5  # Probability of winning a round

class Strategy(Enum):
    ALL_IN = 1
    CONSTANT = 2
    BAL_RATIO = 3 
    DOBL_ON_LOSS = 4
    HALF_ON_LOSS = 5

def apply_strategy(strat, bal, bet, initial_bet, bal_ratio, last_round_won):
    """Apply the bet adjustment strategy based on the current balance and whether the last round was won."""
    if strat == Strategy.ALL_IN:
        bet = bal  # Bet everything each round
    elif strat == Strategy.CONSTANT:
        bet = initial_bet  # Keep bet constant for CONSTANT strategy
    elif strat == Strategy.BAL_RATIO:
        bet = bal * bal_ratio  # Calculate bet based on a portion of balance for BAL_RATIO strategy
    elif strat == Strategy.DOBL_ON_LOSS and not last_round_won:
        bet = bet * 2  # Double bet on loss, but not more than balance
    elif strat == Strategy.HALF_ON_LOSS and not last_round_won:
        bet = bet / 2  # Halve bet on loss
    elif strat in [Strategy.DOBL_ON_LOSS, Strategy.HALF_ON_LOSS] and last_round_won:
        bet = initial_bet  # Reset bet after win for Martingale strategies

    bet = max(bet, 1)       # set to at least 1
    bet = min(bet, bal)     # Can't bet more than we have
    return bet

def game_run_until_broke(strat, bal, init_bet_bal_ratio, debug=False):
    """Will always go broke assuming a house_edge < 1"""
    initial_bet = bal * init_bet_bal_ratio 
    bet = initial_bet
    rounds_count = 0
    rounds_won = 0
    rounds_lost = 0
    wagered = 0
    max_bal = bal
    last_round_won = False  # Tracks if the last round was won

    while bal > 0:
        if random.random() < WIN_PROBABILITY:  # Parameterized win probability
            payout = bet / WIN_PROBABILITY * HOUSE_EDGE - bet
            rounds_won += 1
            max_bal = max(max_bal, bal)
            last_round_won = True  # Set last_round_won to True on win
        else:
            payout = -bet
            rounds_lost += 1
            last_round_won = False  # Set last_round_won to False on loss

        if debug:
            print(f"Round {rounds_count}: Balance = {bal}, Bet = {bet}, Payout = {payout}")

        bal += payout
        rounds_count += 1
        wagered += bet

        # Apply strategy logic (reset bet if the last round was won)
        bet = apply_strategy(strat, bal, bet, initial_bet, init_bet_bal_ratio, last_round_won)

    return rounds_count, rounds_won, rounds_lost, round(wagered), round(max_bal)

def print_strategy_statistics(strat, games):
    rounds_count, _, _, wagered, max_bal = zip(*games)
    
    def calculate_mode(data):
        try:
            return statistics.mode(data)
        except statistics.StatisticsError:
            return '-'
    
    stats = {
        "Rounds": rounds_count,
        "Wagered": wagered,
        "Max Bal": max_bal
    }
    
    print(f"Strategy: {strat.name}")
    print("-" * 50)
    print(f"{'Metric':<10}{'Mean':>10}{'Mode':>10}|{'Min':>10}{'Q1':>10}{'Median':>10}{'Q3':>10}{'Max':>10}")
    print("-" * 50)
    
    for key, values in stats.items():
        mean_val = int(statistics.mean(values))
        mode_val = calculate_mode(values)
        q1, median, q3 = np.percentile(values, [25, 50, 75])
        min_val, max_val = min(values), max(values)
        print(f"{key[:10]:<10}{mean_val:>10}{mode_val:>10}|{min_val:>10}{int(q1):>10}{int(median):>10}{int(q3):>10}{max_val:>10}")
    
    print("-" * 50)
    print()

def strategy_run(strat=Strategy.ALL_IN, num_games=10000, bal_init=10000, init_bet_bal_ratio=1, bal_ratio=None):
    games = []
    for _ in range(num_games):
        games.append(game_run_until_broke(strat, bal_init, init_bet_bal_ratio, bal_ratio))
    
    print_strategy_statistics(strat, games)
    return games  # Return the game results for later plotting

import matplotlib.pyplot as plt

def plot_all_strategy_results(all_games):
    """Aggregate strategy data and plot histograms for rounds, wagered, and max balance."""
    
    # Define colors for strategies
    strategy_colors = {
        Strategy.ALL_IN: 'blue',
        Strategy.CONSTANT: 'green',
        Strategy.BAL_RATIO: 'orange',
        Strategy.DOBL_ON_LOSS: 'red',
        Strategy.HALF_ON_LOSS: 'purple'
    }

    # Aggregate data from all strategies
    data = {metric: [] for metric in ["rounds", "wagered", "max_balance"]}
    labels = []

    for strat, games in all_games.items():
        rounds_count, _, _, wagered, max_bal = zip(*games)
        data["rounds"].append(rounds_count)
        data["wagered"].append(wagered)
        data["max_balance"].append(max_bal)
        labels.append(strat.name)

    # Create subplots
    fig, axs = plt.subplots(3, 1, figsize=(10, 8))
    metrics = ["rounds", "wagered", "max_balance"]
    titles = ["Rounds", "Wagered", "Max Bal"]
    
    for i, metric in enumerate(metrics):
        # axs[i].hist(data[metric], bins=50, alpha=0.5, label=labels)
        axs[i].boxplot(data[metric], labels=labels, patch_artist=True, showfliers=False)
        axs[i].set_title(titles[i])
        # axs[i].set_xlabel(metric.replace("_", " ").title())
        # axs[i].set_ylabel("Frequency")
        # axs[i].legend(loc="best")
        axs[i].grid(True)
        # axs[i].set_xlim(0, bal_init**2)  # Set x-axis limits
        # axs[i].set_xlim(0, np.percentile(data[metric], 95))  # Set x-axis limits

    plt.tight_layout()
    plt.show()

# Run simulations and collect game data
num_games = 100
bal_init = 100
all_games = {
    Strategy.ALL_IN: strategy_run(Strategy.ALL_IN, num_games, bal_init, 1),
    Strategy.CONSTANT: strategy_run(Strategy.CONSTANT, num_games, bal_init, 0.1),
    Strategy.BAL_RATIO: strategy_run(Strategy.BAL_RATIO, num_games, bal_init, 0.5),  # Add BAL_RATIO with ratio 0.5
    Strategy.DOBL_ON_LOSS: strategy_run(Strategy.DOBL_ON_LOSS, num_games, bal_init, 0.1),
    Strategy.HALF_ON_LOSS: strategy_run(Strategy.HALF_ON_LOSS, num_games, bal_init, 0.1),
}

# Plot the results for all strategies at once
plot_all_strategy_results(all_games)
