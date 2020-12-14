def latest(scores):
    """retorna el ultimo resultado"""
    return scores[-1]


def personal_best(scores):
    """retorna el resultado mas alto"""
    return max(scores)


def personal_top_three(scores):
    """retorna los tres resultados mas altos"""
    return sorted(scores, reverse=True)[:3]
