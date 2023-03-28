import random


class Character:
    def __init__(self, name, HP, MP, ENG, BLF, ATK, INT, FTH, DEF, REP, AGI, VIT, REM, RST):
        self.name = name

        # 소모용
        self.max_HP = HP  # 최대체력
        self.HP = HP  # 체력
        self.max_MP = MP  # 최대마나
        self.MP = MP  # 마나
        self.max_ENG = ENG  # 최대기력
        self.ENG = ENG  # 기력
        self.max_BLF = BLF  # 최대믿음 /Holy Knight의 마나역할
        self.BLF = BLF  # 믿음

        # 고정스탯
        self.ATK = ATK  # 공격력
        self.INT = INT  # 지능/주문력
        self.FTH = FTH  # 신앙력
        self.DEF = DEF  # 방어력
        self.REP = REP  # 마법저항력
        self.AGI = AGI  # 민첩/회피율
        self.VIT = VIT  # 체력재생력
        self.RST = RST  # 기력재생력
        self.REM = REM  # 마나재생력

    def swordman_attack(self, target):
        if random.random() < self.AGI:
            return
        damage = self.ATK + random.randint(-50, 100)  # 랜덤으로 치명타 적용
        damage -= target.DEF  # 방어력으로 물리공격 상쇄
        if damage < 0:  # 뎀지가 0이 안될시에 공격이 안됨
            damage = 0
        target.hp -= damage
        print(f'대충{target.name}에게 {damage}를 입혔다는 내용')
        if target.hp <= 0:
            print(f'{target.name}이 대충 죽었다는 내용')

    def whirlwind(self, target):
        if random.random() < target.AGI:
            return
        damage = self.ATK*0.8
        damage -= target.DEF
        if damage < 0:
            damage = 0
        target.HP -= damage
        print(f'대충{target.name}에게 {damage}만큼 망가졌다!')
        if target.hp <= 0:
            print(f'{target.name}, 소용돌이로 가루가 되었다.')

        # 성기사
        # 성기사 평타
    def holy_attack(self, target):
        if random.random() < target.AGI:
            return
        damage = self.ATK + self.FTH*0.2 + \
            random.randint(-20, 150)  # 랜덤으로 치명타 적용
        damage -= target.DEF  # 방어력으로 물리공격 상쇄
        if damage < 0:  # 뎀지가 0이 안될시에 공격이 안됨
            damage = 0
        target.HP -= damage
        print(f'대충{target.name}에게 {damage}를 입혔다!')
        if target.hp <= 0:
            print(f'{target.name}이 성스로워졌다!')

        # 신성한불꽃
    def sacredfire(self, target):
        if random.random() < target.AGI:
            return
        damage = self.FTH*0.7
        if damage < 0:  # 뎀지가 0이 안될시에 공격이 안됨
            damage = 0
        target.HP -= damage
        print(f'대충{target.name}에게 {damage}만큼 뜨끈뜨끈해졌다!')
        if target.HP <= 0:
            print(f'{target.name}, 귀중한 단백질원이 되었다')


class Monster:
    def __init__(self, name, HP, ATK, INT, DEF, REP, AGI):
        self.name = name

        # 소모용
        self.max_HP = HP  # 최대체력
        self.HP = HP  # 체력

        # 고정스탯
        self.ATK = ATK  # 공격력
        self.INT = INT  # 지능/주문력
        self.DEF = DEF  # 방어력
        self.REP = REP  # 마법저항력
        self.AGI = AGI  # 민첩/회피율

    # Skeleton
        # 스켈레톤 평타

    def skeleton_attack(self, target):
        if random.random() < target.AGI:
            return
        damage = self.ATK + random.randint(-50, 70)  # 랜덤으로 치명타 적용
        damage -= target.DEF  # 방어력으로 물리공격 상쇄
        if damage < 0:  # 뎀지가 0이 안될시에 공격이 안됨
            damage = 0
        target.HP -= damage
        print(f'나는 {damage}만큼 데미지를 입었다!')

        # 화살
    def arrow(self, target):
        if random.random() < target.AGI:
            return
        damage = self.ATK
        damage -= target.DEF  # 방어력으로 물리공격 상쇄
        if damage < 0:  # 뎀지가 0이 안될시에 공격이 안됨
            damage = 0
        target.HP -= damage
        print(f'나는 화살을 맞아 {damage}만큼 데미지를 입었다!')
        if target.HP <= 0:
            print('아이고 이렇게 가면 이 세계는 누가지키나...')


# Giant Fly
        # 거대파리 평타


    def giantfly_attack(self, target):
        if random.random() < target.AGI:
            return
        damage = self.ATK + random.randint(-50, 100)  # 랜덤으로 치명타 적용
        damage -= target.DEF  # 방어력으로 물리공격 상쇄
        if damage < 0:  # 뎀지가 0이 안될시에 공격이 안됨
            damage = 0
        target.HP -= damage
        print(f'나는 {damage}만큼 데미지를 입었다!')
        if target.HP <= 0:
            print('아이고 이렇게 가면 이 세계는 누가지키나...')

        # 박치기
    def headattack(self, target):
        if random.random() < target.AGI:
            return
        damage = self.ATK + 30
        damage -= target.DEF  # 방어력으로 물리공격 상쇄
        if damage < 0:  # 뎀지가 0이 안될시에 공격이 안됨
            damage = 0
        target.HP -= damage
        print(f'나는 박치기 공격으로 {damage}만큼 데미지를 입었다!')
        if target.HP <= 0:
            print('아이고 이렇게 가면 이 세계는 누가지키나...')

# 자식클래스
# Sword Master Class


class Sword_Master(Character):
    def __init__(self, name, HP, MP, ENG, BLF, ATK, INT, FTH, DEF, REP, AGI, VIT, REM, RST):
        super().__init__(name, HP, MP, ENG, BLF, ATK,
                         INT, FTH, DEF, REP, AGI, VIT, REM, RST)

        # 소모용
        self.max_HP = HP  # 최대체력
        self.HP = HP  # 체력

        # 고정스탯
        self.ATK = ATK  # 공격력
        self.DEF = DEF  # 방어력
        self.REP = REP  # 마법저항력
        self.AGI = AGI  # 민첩/회피율
        self.VIT = VIT  # 체력재생력

        HP = 500
        ATK = 150
        DEF = 80
        REP = 60
        AGI = 0.2
        VIT = 10
        self.skills = [self.swordman_attack,
                       self.whirlwind]

    def attack(self, target):
        print("Choose your skill:")
        for i, skill in enumerate(self.skills):
            print(f"{i+1}: {skill.__name__}")  # 스킬 번호와 이름 출력
        choice = int(input()) - 1  # 스킬 번호 입력 받기 (인덱스는 0부터 시작하므로 1을 뺌)
        selected_skill = self.skills[choice]  # 선택한 스킬의 함수 객체 가져오기
        selected_skill(target)  # 선택한 스킬 사용하기


class Holy_Knight(Character):
    def __init__(self, name, HP, MP, ENG, BLF, ATK, INT, FTH, DEF, REP, AGI, VIT, REM, RST):
        super().__init__(name, HP, MP, ENG, BLF, ATK,
                         INT, FTH, DEF, REP, AGI, VIT, REM, RST)

        # 소모용
        self.max_HP = HP  # 최대체력
        self.HP = HP  # 체력
        self.max_BLF = BLF  # 최대믿음 /Holy Knight의 마나역할
        self.BLF = BLF  # 믿음

        # 고정스탯
        self.ATK = ATK  # 공격력
        self.FTH = FTH  # 신앙력
        self.DEF = DEF  # 방어력
        self.REP = REP  # 마법저항력
        self.AGI = AGI  # 민첩/회피율
        self.VIT = VIT  # 체력재생력

        HP = 480
        BLF = 200
        ATK = 90
        FTH = 50
        DEF = 60
        REP = 80
        AGI = 0.1
        VIT = 8
        self.skills = [self.holy_attack,
                       self.sacredfire]

    def attack(self, target):
        print("Choose your skill:")
        for i, skill in enumerate(self.skills):
            print(f"{i+1}: {skill.__name__}")  # 스킬 번호와 이름 출력
        choice = int(input()) - 1  # 스킬 번호 입력 받기 (인덱스는 0부터 시작하므로 1을 뺌)
        selected_skill = self.skills[choice]  # 선택한 스킬의 함수 객체 가져오기
        selected_skill(target)  # 선택한 스킬 사용하기


class Sekelton(Monster):
    def __init__(self, name, HP, ATK, INT, DEF, REP, AGI):
        super().__init__(name, HP, ATK, INT, DEF, REP, AGI)
        self.name = name

        # 소모용
        self.max_HP = HP  # 최대체력
        self.HP = HP  # 체력

        # 고정스탯
        self.ATK = ATK  # 공격력
        self.DEF = DEF  # 방어력
        self.REP = REP  # 마법저항력
        self.AGI = AGI  # 민첩/회피율

        HP = 250
        ATK = 100
        DEF = 50
        REP = 100
        AGI = 0.5
        self.skills = [self.skeleton_attack, self.arrow]

    def attack(self, target):
        for _ in range(3):
            self.skeleton_attack(target)
        self.arrow(target)

# Giant Fly


class Giant_Fly(Monster):
    def __init__(self, name, HP, ATK, INT, DEF, REP, AGI):
        super().__init__(name, HP, ATK, INT, DEF, REP, AGI)
        self.name = name

        # 소모용
        self.max_HP = HP  # 최대체력
        self.HP = HP  # 체력

        # 고정스탯
        self.ATK = ATK  # 공격력
        self.DEF = DEF  # 방어력
        self.REP = REP  # 마법저항력
        self.AGI = AGI  # 민첩/회피율

        HP = 200
        ATK = 70
        DEF = 60
        REP = 120
        AGI = 0.8
        self.skills = [self.giantfly_attack, self.headattack]

    def attack(self, target):
        for _ in range(3):
            self.giantfly_attack(target)
        self.headattack(target)


def battle(player, enemy):
    classes = {
        1: Sword_Master,
        2: Holy_Knight,
    }
    print("대충 오프닝멘트")
    print("이름을 입력하세요")
    player_name = input()
    print(f'난세에 태어난 영웅, {player_name}은 대충 거시기 해서 거시기 한다.')
    print('영웅을 선택하시오')

    if input() in classes.keys():
        selected_class = classes[int(input())]
        player = selected_class
        print(f'{player}영웅을 선택하였습니다.')
    else:
        print("잘못된 선택입니다.")
