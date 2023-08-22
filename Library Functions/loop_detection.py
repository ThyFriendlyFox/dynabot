def detect_loop(memory: list) -> bool:
    tortoise = hare = 0
    while hare < len(memory) and hare + 1 < len(memory):
        tortoise += 1
        hare += 2
        if memory[tortoise] == memory[hare]:
            return True
    return False
