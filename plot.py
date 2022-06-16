import matplotlib.pyplot as plt
import pickle

with open("losses.pkl", "rb") as losses_file:
    losses = pickle.load(losses_file)
with open("all_rewards.pkl", "rb") as all_rewards_file:
    all_rewards = pickle.load(all_rewards_file)
a,b = zip(*losses)
plt.plot(a, b)
plt.ylabel("Losses")
plt.show()
plt.savefig("losses.png")

a,b = zip(*all_rewards)
plt.plot(a, b)
plt.ylabel("All Rewards")
plt.show()
plt.savefig("all_rewards.png")    