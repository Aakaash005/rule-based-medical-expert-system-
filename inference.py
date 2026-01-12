def forward_chaining(facts, rules):
    inferred = True
    reasoning_log = []

    while inferred:
        inferred = False
        for rule in rules:
            if all(condition in facts for condition in rule["if"]):
                if rule["then"] not in facts:
                    facts.add(rule["then"])
                    reasoning_log.append(
                        f"Rule Fired → IF {rule['if']} THEN {rule['then']}"
                    )
                    inferred = True

    return facts, reasoning_log
