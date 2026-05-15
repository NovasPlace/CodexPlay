import random
from dataclasses import dataclass


CHALLENGES = [
    "Patch failing tests without breaking existing behavior.",
    "Optimize memory usage in a multi-agent workflow.",
    "Defend the system against hallucinated tool calls.",
    "Repair a corrupted evolution vault entry.",
    "Stabilize an overloaded agent bus during combat.",
]


ATTACKS = {
    "creative": ["Creative Leap", "Wildcard Synthesis", "Idea Barrage"],
    "rigor": ["Ruthless Verification", "Logic Slam", "Constraint Crush"],
    "efficiency": ["Practical Refactor", "Rapid Compression", "Optimization Burst"],
}


@dataclass
class Agent:
    name: str
    style: str
    power: int
    wins: int = 0

    def attack(self):
        return random.choice(ATTACKS[self.style])

    def evolve(self, won: bool):
        gain = random.randint(1, 4)
        if won:
            self.power += gain
            self.wins += 1
        else:
            self.power += 1


class WhisGovernor:
    @staticmethod
    def judge(agents):
        weighted = []
        for agent in agents:
            variance = random.randint(-2, 5)
            score = agent.power + variance
            weighted.append((score, agent))

        weighted.sort(key=lambda x: x[0], reverse=True)
        return weighted[0][1]


agents = [
    Agent("GokuBuilder", "creative", 10),
    Agent("VegetaVerifier", "rigor", 10),
    Agent("BulmaOptimizer", "efficiency", 10),
]


def run_battle(rounds=5):
    print("=== CODEXPLAY: AGENT ARENA ===\n")

    for i in range(rounds):
        challenge = random.choice(CHALLENGES)

        print(f"ROUND {i+1}")
        print(f"Challenge: {challenge}\n")

        for agent in agents:
            print(f"{agent.name} launches {agent.attack()}!")

        print("\nWhisGovernor evaluates proposals...\n")

        winner = WhisGovernor.judge(agents)

        for agent in agents:
            agent.evolve(agent == winner)

        print(f"Winner: {winner.name}")
        print(f"{winner.name} gains a Zenkai boost!")
        print("Battle lesson stored in Evolution Vault.\n")
        print("-" * 50)

    print("\n=== FINAL POWER LEVELS ===")
    for agent in agents:
        print(f"{agent.name}: power={agent.power}, wins={agent.wins}")


if __name__ == "__main__":
    run_battle()
