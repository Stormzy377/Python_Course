full_dot = '●'
empty_dot = '○'

def create_character(name, strength, intelligence, charisma):
    # 3. Validações do nome
    if not isinstance(name, str):
        return "The character name should be a string"
    if name == "":
        return "The character should have a name"
    if len(name) > 10:
        return "The character name is too long"
    if " " in name:
        return "The character name should not contain spaces"
        
    # 4. Validações dos atributos
    stats = [strength, intelligence, charisma]
    for stat in stats:
        # No Python, bool é subclasse de int, por isso excluímos booleanos explicitamente
        if not isinstance(stat, int) or isinstance(stat, bool):
            return "All stats should be integers"
        if stat < 1:
            return "All stats should be no less than 1"
        if stat > 4:
            return "All stats should be no more than 4"
            
    if sum(stats) != 7:
        return "The character should start with 7 points"
        
    # 5. Formatação da string de saída com os pontos cheios (●) e vazios (○)
    str_bar = "●" * strength + "○" * (10 - strength)
    int_bar = "●" * intelligence + "○" * (10 - intelligence)
    cha_bar = "●" * charisma + "○" * (10 - charisma)
    
    return f"{name}\nSTR {str_bar}\nINT {int_bar}\nCHA {cha_bar}"