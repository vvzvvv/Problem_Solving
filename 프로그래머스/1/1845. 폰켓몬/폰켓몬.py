def solution(nums):
    answer = 0
    select = len(nums) // 2  # 마리 수
    pokemon = []
    for i in nums:
        if i not in pokemon and len(pokemon) != select:
            pokemon.append(i)
    answer = len(pokemon)
    return answer