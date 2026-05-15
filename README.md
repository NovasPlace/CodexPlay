# CodexPlay

A chaotic little playground for AI agent experiments.

This repo starts with **Agent Arena**, a toy simulation where agents battle over decisions, earn Zenkai-style upgrades from failure, and get judged by a deterministic governor before anything is allowed to win.

## What is this?

CodexPlay is meant to be a sandbox for:

- agent combat mechanics
- deterministic judging
- visibility logs
- skill evolution experiments
- silly stick-figure / Tournament of Power style visualizations later

## Run the arena

```bash
python -m codexplay.arena
```

Or install in editable mode first:

```bash
pip install -e .
python -m codexplay.arena
```

## Current prototype

The first version includes four agents:

- **GokuBuilder** — creative builder, high novelty
- **VegetaVerifier** — ruthless critic, high rigor
- **BulmaOptimizer** — practical optimizer, high efficiency
- **WhisGovernor** — deterministic judge, keeps the Saiyans from deleting production

Each round gives the agents a challenge. Agents generate a proposal profile, clash, receive scores, and evolve slightly based on the outcome.

## Example output

```txt
=== CODEXPLAY: AGENT ARENA ===
Challenge: Patch failing tests without breaking existing behavior.

GokuBuilder launches Creative Leap!
VegetaVerifier counters with Ruthless Verification!
BulmaOptimizer deploys Practical Refactor!

WhisGovernor evaluates proposals...
Winner: VegetaVerifier
Battle lesson stored: rigor beat novelty on safety-critical task.
```

## Design rule

No real-world autonomy. No self-propagation. No uncontrolled external access.

The arena is for bounded simulations, agent evaluation, and visible decision-making.
